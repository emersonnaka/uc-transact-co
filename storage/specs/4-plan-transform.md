# 4 — Sketch Plan: Transform (medallion over `raw.*`)

- **Author:** architect (judgment, no hands) · **Status:** sketch — awaits human
  confirmation at its checkpoint
- **Basis:** `3-technical-brief.md` (handoff to construction) · evidence
  `E1`–`E12` from `1-context.md` · decisions `D1`–`D4` from `2-ontology.md`
- **Writes authorized at execution:** `dbt/models/staging/` — the intermediate
  and marts layers require a scope extension at their own checkpoint.

| # | Item | Evidence | State |
| - | --- | --- | --- |
| 1 | `stg_customers` — types, key `customer_id`, no business rule | E1, E2 (5,000 rows) | clear |
| 2 | `stg_products` — types, key `product_id` | E1, E2 (400 rows) | clear |
| 3 | `stg_orders` — preserves the three clocks (`ordered_at`, `updated_at`, `ingested_at`) and the six statuses, ungrouped | E3, E5 | clear |
| 4 | `stg_payments` — preserves `paid_at` and the two statuses (`captured`, `refunded`) | E4, E6 | clear |
| 5 | `int_orders_payments_reconciled` — left join order↔payment; keeps the 2,204 orders without payment as explicit coverage, not as zero | E7 (0 divergences), E8 | clear |
| 6 | `int_returns_refunds` — refund↔return mirror, counted, never subtracted | E9 (3,049 = 3,049) | clear |
| 7 | `mart_daily_gross_ordered` — sum by `ordered_at`, non-cancelled orders; grain = UTC calendar day, labeled as a technical window | brief, candidate 1 (R$ 1,403,044.31 / 868 orders) | clear; business-day grain **BLOCKED — D4, Finance** |
| 8 | `mart_daily_captured_payments` — sum by `paid_at`, `status='captured'`; same technical grain | brief, candidate 2 (R$ 980,870.44 / 632 payments) | clear; same D4 block |
| 9 | `mart_daily_delivered` — the schema carries no delivery clock; using `ordered_at` as a proxy is choosing the recognition event | brief, candidate 3 (R$ 0.00) | **BLOCKED — D2, Finance** |
| 10 | Any model, mart, or single metric named `revenue` | `2-ontology.md`, controlled refusal | **BLOCKED — D1–D4, Finance** |

Exit gate at execution: `make dbt-check` and `make test` with raw output. No
aggregate from items 7–8 may be renamed to "Revenue".
