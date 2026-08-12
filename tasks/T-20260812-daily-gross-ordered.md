---
id: T-20260812-daily-gross-ordered
title: Aggregate non-cancelled order totals by ordered_at
status: ready
effort: S
budget_iterations: 15
agent: any
depends_on: []
touches_paths: []
creates_paths: [dbt/models/staging/stg_daily_gross_ordered.sql]
source_note: storage/specs/4-plan-transform.md
created: 2026-08-12
tags: [dbt, staging, transactco]
---

## Goal
Produce one daily aggregate of non-cancelled order totals, labeled by its
physical basis and never as Revenue.

## Context
Reads `stg_orders` (Day 2, committed). Sums `total_amount` grouped by the UTC
calendar day of `ordered_at`. Excludes `cancelled`.
Lands in `dbt/models/staging/`: item 7 names a *mart*, but the Day 2 contract
authorizes `dbt/models/staging/` only, and `4-plan-transform.md` states the
marts layer needs a scope extension at its own checkpoint. This spec scopes
down rather than widening the contract.
Evidence: `4-plan-transform.md` item 7 · brief candidate 1
(R$ 1,403,044.31 / 868 orders).

## Behaviors
(written at checkpoint 03)

## Success Criteria
(written at checkpoint 03)

## Validation Card
(written at checkpoint 03)

## Exit Check
(written at checkpoint 03)

## Anti-Patterns
- **Don't name it revenue** — Revenue is unresolved and owned by Finance.
  Label the aggregate by its physical basis instead.
- **Don't net returns into the total** — refunds are counted, never subtracted.

## Do-Not-Touch
- `storage/specs/` — Day 1 and Day 2 evidence, read-only tonight
- `src/transactco/control/` — instructor surface

## Open Questions
(none — this task is fully specified)