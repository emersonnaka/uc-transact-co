# 3 — Technical Brief

- **Status: PENDING HUMAN REVIEW** — remains pending until the Finance owner
  resolves the semantic questions in `2-ontology.md`.
- **Question:** How much Revenue did TransactCo make yesterday, and why should
  the CFO trust that number?
- **Captured:** 2026-08-11 · revision `5143f85` · window = last complete UTC
  calendar day (technical window only; the business day is decision D4)

## What the evidence supports

Yesterday, measured three defensible ways — three different numbers, because
they measure three different events:

| Candidate | Basis | Measured value |
| --- | --- | ---: |
| Gross ordered | non-cancelled orders by `ordered_at` (868 orders) | R$ 1,403,044.31 |
| Captured payments | `status='captured'` by `paid_at` (632 payments) | R$ 980,870.44 |
| Delivered | `status='delivered'` by `ordered_at` | R$ 0.00 |

The spread is not an error. Orders placed yesterday were still `pending`,
`processing`, or `shipped` (E5) — capture lags order placement, and delivery
lags both; no order placed yesterday had been delivered at capture time. Each
candidate is precise; none of them is "Revenue" until Finance decides D1–D4.

## Claims ledger

| Kind | Claim |
| --- | --- |
| fact | The three candidate aggregates above, at revision `5143f85` |
| fact | Payment amounts reconcile 1:1 with order totals where present (E7) |
| fact | 3,049 refunds mirror 3,049 returned orders exactly (E9) |
| inference | Capture-based and order-based views will converge as the cohort settles, minus cancellations and refunds |
| decision (open) | D1–D4 in `2-ontology.md` — owner: Finance |
| question | Does the CFO's "yesterday" mean UTC, store-local, or business day? |

## Why the CFO can trust this

Not because one number is right — because the method is inspectable: approved
sources only (`1-context.md`), read-only access, every claim tied to an
evidence ID, and the one decision the system cannot legitimately make is
explicitly withheld and owned.

## Handoff to construction

Buildable now: staging over the four entities, order↔payment reconciliation,
daily aggregates per candidate — each labeled as its physical basis, never as
"Revenue". Blocked until D1–D4 land: any model, mart, metric, or endpoint
named Revenue.
