# 2 — Ontology Note: Data Is Not Meaning

- **Captured:** 2026-08-11 · revision `5143f85` · ontology `TransactCo 0.1.0`
- **Structural validation:** `uv run transactco ontology validate` →
  `ONTOLOGY=VALID` · pending human review. Structural validity is not
  semantic approval.

## Postgres versus ontology

| Physical fact (Postgres proves) | Semantic question (ontology records) |
| --- | --- |
| `orders.total_amount` sums to a precise number | Is an ordered amount revenue before anything else happens? |
| `payments.amount` with `status = 'captured'` sums to a different number | Is capture the recognition event? |
| `orders.status` has six values | Which statuses contribute — and does `returned` subtract? |
| Three clocks per order, one per payment | Which clock defines "yesterday", in which timezone? |

Postgres can produce candidate aggregates and show how they differ. It cannot
choose between them. The ontology does not produce a better number — it
formalizes the missing decisions and their owner.

## Revenue — status: `unresolved` · owner: Finance

Candidate physical inputs, all evidenced in `1-context.md`:

1. `sum(orders.total_amount)` over non-cancelled orders by `ordered_at`;
2. `sum(payments.amount)` where `status='captured'` by `paid_at`;
3. `sum(orders.total_amount)` where `status='delivered'` by a delivery clock
   the schema does not carry.

Open decisions (all four required before any revenue model may exist):

| # | Decision | Candidates | Status |
| - | --- | --- | --- |
| D1 | Contributing statuses | all non-cancelled · delivered only · captured-paid only | unresolved |
| D2 | Recognition event | order placed · payment captured · delivery | unresolved |
| D3 | Adjustments | refunds subtract in-period · at-origin · reported separately | unresolved |
| D4 | Currency & business day | store tz vs UTC · calendar vs business day | unresolved |

## Controlled refusal

While `Revenue` is `unresolved`, the correct system behavior is a refusal that
names this note and its owner. Entities Customer, Product, Order, and Payment
are evidenced and buildable; the concept Revenue is not.
