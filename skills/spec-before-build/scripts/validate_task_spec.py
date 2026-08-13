#!/usr/bin/env python3
"""Structural validator for one atomic Task-Spec.

Checks the invariants a human is meant to hold, without needing the taskspec
CLI installed: the sizing rule, the two halves of done, the bidirectional
behaviour/eval binding, and a forbidden-term boundary.

usage: validate_task_spec.py <spec.md> [<spec.md> ...] [--forbid TERM]
exit 0 with CHECK_TASK_SPEC=PASS, otherwise 1 with CHECK_TASK_SPEC=FAIL.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

EFFORT_LEAF = {"XS", "S", "M", "L"}
EFFORT_NODE = {"XL", "XXL"}
ID_RE = re.compile(r"^T-\d{8}-[a-z0-9]+(?:-[a-z0-9]+)*$")


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    out: dict[str, str] = {}
    for line in text[3:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" in line and not line.startswith((" ", "\t", "-")):
            k, _, v = line.partition(":")
            out[k.strip()] = v.strip()
    return out


def section(text: str, *headings: str) -> str:
    """Return the body of the first heading that exists.

    Zone 2 is emitted as "## Behavior" by taskspec batch but written as
    "## Behaviors" by hand in some material; accept either spelling.
    """
    for heading in headings:
        m = re.search(rf"^##\s+{re.escape(heading)}\s*$", text, re.M)
        if not m:
            continue
        nxt = re.search(r"^##\s+", text[m.end():], re.M)
        return text[m.end(): m.end() + nxt.start()] if nxt else text[m.end():]
    return ""


def check(path: Path, forbid: str) -> list[str]:
    errs: list[str] = []
    text = path.read_text(encoding="utf-8")
    fm = frontmatter(text)

    if not fm:
        return ["no YAML frontmatter"]

    spec_id = fm.get("id", "")
    if not ID_RE.match(spec_id):
        errs.append(f"id {spec_id!r} is not T-YYYYMMDD-<kebab-slug>")

    for required in ("status", "effort", "depends_on"):
        if required not in fm:
            errs.append(f"frontmatter missing {required}")

    effort = fm.get("effort", "").strip()
    creates = fm.get("creates_paths", "[]")
    touches = fm.get("touches_paths", "[]")
    writes = (creates.strip() not in ("[]", "", "(none)")) or (
        touches.strip() not in ("[]", "", "(none)")
    )
    if effort in EFFORT_NODE:
        if "children" not in fm:
            errs.append(f"effort {effort} is a composition node and must declare children")
        if writes:
            errs.append(f"effort {effort} must not own a write surface")
    elif effort and effort not in EFFORT_LEAF:
        errs.append(f"effort {effort!r} is not one of XS/S/M/L/XL/XXL")

    title = fm.get("title", "").strip().strip('"').strip("'")
    if re.search(r"\band\b", title, re.I):
        errs.append(f'title contains "and" — split it into two specs: {title!r}')

    # ── the two halves of done ─────────────────────────────────────────────
    behaviors = section(text, "Behavior", "Behaviors")
    b_ids = sorted(set(re.findall(r"\*\*(B-\d+)\*\*", behaviors)))
    if not b_ids:
        errs.append("no **B-N** behaviour found under ## Behavior")

    criteria = section(text, "Success Criteria")
    eval_ids = sorted(set(re.findall(r"^(eval_\d+)\s*\(\)", criteria, re.M)))
    if not eval_ids:
        errs.append("no eval_N() function found under ## Success Criteria")

    card = section(text, "Validation Card")
    # map eval id -> verifies list, tolerating both inline and block YAML
    verified: dict[str, list[str]] = {}
    cur = None
    for line in card.splitlines():
        m = re.match(r"\s*-\s*id:\s*(eval_\d+)", line)
        if m:
            cur = m.group(1)
            verified.setdefault(cur, [])
            continue
        m = re.match(r"\s*verifies:\s*\[(.*?)\]", line)
        if m and cur:
            verified[cur] = re.findall(r"B-\d+", m.group(1))
            continue
        m = re.match(r"\s*-\s*(B-\d+)\s*$", line)
        if m and cur:
            verified[cur].append(m.group(1))
    if not verified:
        errs.append("## Validation Card declares no success_criteria entries")

    for e in eval_ids:
        if e not in verified:
            errs.append(f"{e} has no Validation Card entry")
        elif not verified[e]:
            errs.append(f"{e} carries no verifies: [B-N] — it tests something unpromised")

    claimed = {b for v in verified.values() for b in v}
    for b in b_ids:
        if b not in claimed:
            errs.append(f"{b} is not verified by any eval — an unverified behaviour is a hole")
    for e, vs in verified.items():
        for b in vs:
            if b not in b_ids:
                errs.append(f"{e} verifies {b}, which is not declared under ## Behavior")

    exit_check = section(text, "Exit Check")
    if not exit_check.strip():
        errs.append("## Exit Check is missing or empty")
    else:
        named = set(re.findall(r"eval_\d+", exit_check))
        missing = [e for e in eval_ids if e not in named]
        if missing:
            errs.append(f"## Exit Check omits {', '.join(missing)}")

    # ── the boundary ───────────────────────────────────────────────────────
    if forbid:
        for field in ("id", "title", "creates_paths", "touches_paths"):
            if forbid.lower() in fm.get(field, "").lower():
                errs.append(f'forbidden term "{forbid}" appears in {field} — that decision has an owner')
    return errs


def main(argv: list[str]) -> int:
    forbid = "revenue"
    args: list[str] = []
    i = 0
    while i < len(argv):
        if argv[i] == "--forbid":
            forbid = argv[i + 1] if i + 1 < len(argv) else ""
            i += 2
            continue
        args.append(argv[i])
        i += 1

    if not args:
        print("usage: validate_task_spec.py <spec.md> [...] [--forbid TERM]")
        print("CHECK_TASK_SPEC=USAGE_ERROR")
        return 2

    failed = 0
    for a in args:
        p = Path(a)
        if not p.is_file():
            print(f"FAIL {a}: not a file")
            failed += 1
            continue
        errs = check(p, forbid)
        if errs:
            failed += 1
            print(f"FAIL {p}")
            for e in errs:
                print(f"       - {e}")
        else:
            print(f"OK   {p}")

    print()
    if failed:
        print(f"{failed} of {len(args)} spec(s) failed")
        print("CHECK_TASK_SPEC=FAIL")
        return 1
    print(f"{len(args)} spec(s) structurally valid; a human still signs the behaviour.")
    print("CHECK_TASK_SPEC=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
