#!/usr/bin/env python3
"""Read-only MCP server handing the CFO the measurements TransactCo can defend.

Every number here is produced by a staging model that passed the five
acceptance gates at Tier 1. The server reports each measurement with its
physical basis and the spec that authorized it, and it refuses to answer what
Revenue is, because that decision is Finance's and is still open.

Run: uv run python scripts/cfo_mcp.py    (stdio JSON-RPC, MCP 2025-06-18)
"""

from __future__ import annotations

import json
import pathlib
import sys

import duckdb

ROOT = pathlib.Path(__file__).resolve().parent.parent
WAREHOUSE = ROOT / "warehouse.duckdb"

# Each measurement names the clock it is measured on and the accepted spec that
# built it. "What it is not" exists so a reader cannot promote a measurement
# into a business meaning by accident.
MEASUREMENTS = {
    "gross_ordered": {
        "model": "main.stg_daily_gross_ordered",
        "date_column": "ordered_date_utc",
        "amount_column": "gross_ordered_amount",
        "count_column": "order_count",
        "basis": "Sum of order total_amount, excluding status 'cancelled', "
                 "grouped by the UTC calendar day of ordered_at.",
        "clock": "order placement (ordered_at), UTC",
        "is_not": "Not Revenue. Placing an order is not known to be the "
                  "recognition event; decision D2 is open.",
        "spec": "T-20260812-daily-gross-ordered",
    },
    "captured_payments": {
        "model": "main.stg_daily_captured_payments",
        "date_column": "captured_date_utc",
        "amount_column": "captured_payment_amount",
        "count_column": "captured_payment_count",
        "basis": "Sum of payment amount where status = 'captured', grouped by "
                 "the UTC calendar day of paid_at.",
        "clock": "payment capture (paid_at), UTC",
        "is_not": "Not Revenue, and not net of refunds. Refunds are reported "
                  "separately; decisions D2 and D3 are open.",
        "spec": "T-20260812-stg-daily-captured-payments",
    },
}

OPEN_DECISIONS = [
    {
        "id": "D2",
        "question": "Which event recognizes income: order placed, payment "
                    "captured, or delivery?",
        "owner": "Finance",
        "spec": "T-20260812-daily-grain-decision",
        "status": "unresolved",
        "consequence": "Until D2 is answered, gross_ordered and "
                       "captured_payments are two measurements, not two "
                       "candidate values of one number.",
    },
    {
        "id": "D3",
        "question": "Do refunds subtract in-period, subtract at-origin, or "
                    "report separately?",
        "owner": "Finance",
        "status": "unresolved",
        "consequence": "No model subtracts refunds. The returned/refunded "
                       "mirror counts both sides instead.",
    },
]


def _db() -> duckdb.DuckDBPyConnection:
    return duckdb.connect(str(WAREHOUSE), read_only=True)


def _accepted(spec_id: str) -> dict:
    """Provenance straight off the accepted spec's frontmatter."""
    path = ROOT / "tasks" / "done" / f"{spec_id}.md"
    if not path.exists():
        return {"accepted": False, "note": "no accepted spec found"}
    out: dict = {}
    for line in path.read_text().splitlines():
        for key in ("accepted", "accepted_by", "accepted_at", "signed_off_by"):
            if line.startswith(f"{key}: "):
                out[key] = line.split(": ", 1)[1].strip()
        if line.strip() == "---" and out:
            break
    return out


def list_measurements() -> dict:
    con = _db()
    items = []
    for name, m in MEASUREMENTS.items():
        total, count, days = con.execute(
            f"select sum({m['amount_column']}), sum({m['count_column']}), count(*) "
            f"from {m['model']}"
        ).fetchone()
        items.append({
            "name": name,
            "total_amount": str(total),
            "row_count": int(count),
            "days_covered": int(days),
            "basis": m["basis"],
            "clock": m["clock"],
            "what_it_is_not": m["is_not"],
            "provenance": {"spec": m["spec"], **_accepted(m["spec"])},
        })
    con.close()
    return {"measurements": items, "open_decisions": [d["id"] for d in OPEN_DECISIONS]}


def daily_series(measurement: str, start: str | None = None, end: str | None = None) -> dict:
    if measurement not in MEASUREMENTS:
        return {"error": f"unknown measurement: {measurement}",
                "available": sorted(MEASUREMENTS)}
    m = MEASUREMENTS[measurement]
    where, params = "", []
    if start:
        where += f" where {m['date_column']} >= ?"
        params.append(start)
    if end:
        where += (" and" if where else " where") + f" {m['date_column']} <= ?"
        params.append(end)
    con = _db()
    rows = con.execute(
        f"select {m['date_column']}, {m['count_column']}, {m['amount_column']} "
        f"from {m['model']}{where} order by 1",
        params,
    ).fetchall()
    con.close()
    return {
        "measurement": measurement,
        "clock": m["clock"],
        "what_it_is_not": m["is_not"],
        "rows": [{"date": str(d), "count": int(c), "amount": str(a)} for d, c, a in rows],
    }


def reconciliation() -> dict:
    """Where the two clocks disagree, stated rather than smoothed over."""
    con = _db()
    gross = con.execute("select sum(gross_ordered_amount) from main.stg_daily_gross_ordered").fetchone()[0]
    captured = con.execute("select sum(captured_payment_amount) from main.stg_daily_captured_payments").fetchone()[0]
    unpaid = con.execute(
        "select count(*) from main.stg_orders_payments_reconciled where not has_payment"
    ).fetchone()[0]
    mirror = con.execute("select * from main.stg_returns_refunds").fetchone()
    con.close()
    return {
        "gross_ordered_amount": str(gross),
        "captured_payment_amount": str(captured),
        "difference": str(gross - captured),
        "orders_with_no_payment_row": int(unpaid),
        "returned_orders": {"count": int(mirror[0]), "amount": str(mirror[1])},
        "refunded_payments": {"count": int(mirror[2]), "amount": str(mirror[3])},
        "reading": "The difference is not an error and not a loss. The two "
                   "figures are measured on different clocks, and D2 decides "
                   "which clock the business means.",
    }


def open_decisions() -> dict:
    return {"open_decisions": OPEN_DECISIONS}


def revenue() -> dict:
    return {
        "answer": "unavailable",
        "reason": "Revenue is not defined in this repository. It is a business "
                  "decision, not a measurement, and it is unresolved.",
        "owner": "Finance",
        "blocking_decision": "D2",
        "what_you_can_have_instead": sorted(MEASUREMENTS),
        "next_step": "Answer D2 (T-20260812-daily-grain-decision). Once the "
                     "recognition event is named, one of the measurements "
                     "above becomes the basis for Revenue and a new spec can "
                     "build it under that name.",
    }


TOOLS = [
    {"name": "list_measurements",
     "description": "Every defensible daily measurement, with its physical basis, the clock it is measured on, and the accepted spec that built it.",
     "inputSchema": {"type": "object", "properties": {}}},
    {"name": "daily_series",
     "description": "The day-by-day series for one measurement.",
     "inputSchema": {"type": "object", "required": ["measurement"], "properties": {
         "measurement": {"type": "string", "enum": sorted(MEASUREMENTS)},
         "start": {"type": "string", "description": "inclusive YYYY-MM-DD"},
         "end": {"type": "string", "description": "inclusive YYYY-MM-DD"}}}},
    {"name": "reconciliation",
     "description": "Why the two clocks give different totals, and the returned/refunded mirror.",
     "inputSchema": {"type": "object", "properties": {}}},
    {"name": "open_decisions",
     "description": "The business decisions that are still unresolved, and who owns them.",
     "inputSchema": {"type": "object", "properties": {}}},
    {"name": "revenue",
     "description": "Asks for Revenue. Returns the reason it cannot be answered and who owns it.",
     "inputSchema": {"type": "object", "properties": {}}},
]

HANDLERS = {
    "list_measurements": lambda a: list_measurements(),
    "daily_series": lambda a: daily_series(a.get("measurement", ""), a.get("start"), a.get("end")),
    "reconciliation": lambda a: reconciliation(),
    "open_decisions": lambda a: open_decisions(),
    "revenue": lambda a: revenue(),
}


def handle(request: dict) -> dict | None:
    method = request.get("method", "")
    if method == "initialize":
        result = {"protocolVersion": "2025-06-18",
                  "capabilities": {"tools": {}},
                  "serverInfo": {"name": "transactco-cfo", "version": "1.0.0"}}
    elif method == "tools/list":
        result = {"tools": TOOLS}
    elif method == "tools/call":
        params = request.get("params", {})
        name = params.get("name", "")
        handler = HANDLERS.get(name)
        if not handler:
            return {"jsonrpc": "2.0", "id": request.get("id"),
                    "error": {"code": -32601, "message": f"unknown tool: {name}"}}
        try:
            payload = handler(params.get("arguments") or {})
            result = {"content": [{"type": "text", "text": json.dumps(payload, indent=2)}]}
        except Exception as exc:  # surface the failure, never a fabricated number
            result = {"content": [{"type": "text", "text": json.dumps({"error": str(exc)})}],
                      "isError": True}
    elif method.startswith("notifications/"):
        return None
    else:
        return {"jsonrpc": "2.0", "id": request.get("id"),
                "error": {"code": -32601, "message": f"unsupported method: {method}"}}
    return {"jsonrpc": "2.0", "id": request.get("id"), "result": result}


def main() -> int:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        response = handle(json.loads(line))
        if response is not None:
            print(json.dumps(response), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
