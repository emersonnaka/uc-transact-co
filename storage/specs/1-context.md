# 1 — Context Inventory

- **Question:** How much Revenue did TransactCo make yesterday, and why should
  the CFO trust that number?
- **Captured:** 2026-08-11 · revision `5143f85` · role `analytics_ro` /
  DuckDB `raw.*` mirror
- **Note:** the fixture is time-relative; `make bootstrap` invalidates every
  number below. Recapture before reuse.

## Approved sources

Each source earned its place; nothing else entered the investigation.

| # | Source | Kind | Purpose | Authority | Limits |
| - | --- | --- | --- | --- | --- |
| S1 | `README.md` · System model section | doc | four entities, time vocabulary | descriptive | not a schema |
| S2 | `infra/postgres/init/01_schema.sql` | DDL | intended physical shape | design intent | may drift from live |
| S3 | `src/transactco/operational/seed.py` | code | generator behavior, status flows | mechanical truth | not business policy |
| S4 | `src/transactco/operational/postgres.py` | code | the access path | mechanical truth | — |
| S5 | live `public.*` via `analytics_ro` (mirrored to `raw.*`) | data | current physical evidence | physical only | carries no meaning |

Excluded until their own checkpoint: dbt, analytics models, `_control`,
injection, scoring, instructor surfaces.

## Evidence ledger

| ID | Kind | Claim | Evidence |
| -- | --- | --- | --- |
| E1 | fact | Four operational tables exist | catalog: customers, products, orders, payments |
| E2 | fact | Row counts at capture | 5,000 customers · 400 products · 63,169 orders · 60,965 payments |
| E3 | fact | Orders carry three clocks | `ordered_at`, `updated_at`, `ingested_at` (tz-aware) |
| E4 | fact | Payments carry their own clock | `paid_at` ≠ `ordered_at` — two event times per sale |
| E5 | fact | Order status vocabulary | delivered, shipped, returned, cancelled, processing, pending |
| E6 | fact | Payment status vocabulary | captured, refunded |
| E7 | fact | Payment↔order amounts reconcile | 0 mismatches on `amount` vs `total_amount` where a payment exists |
| E8 | fact | Not every order has a payment | 2,204 orders without any payment row |
| E9 | fact | Refunds mirror returns | 3,049 refunded payments = 3,049 returned orders |
| E10 | fact | Mirror is current | `raw.*` landed 2026-08-11 09:09 −03, counts match Postgres two ways |
| E11 | inference | "Revenue" has at least three physical candidates | ordered totals, captured payments, delivered totals — different events, different clocks |
| E12 | question | Which event recognizes the amount? | not answerable from the catalog — see `2-ontology.md` |

## Reconciliation

Two-way check between Postgres `public.*` and DuckDB `raw.*`: identical row
counts on all four tables at capture time (E10). The analytical copy may be
used as evidence for physical claims.

## Limits

The inventory proves availability, shape, and internal consistency. It cannot
decide meaning: statuses, recognition events, adjustment handling, currency,
and the business day remain open — recorded in `2-ontology.md`.
