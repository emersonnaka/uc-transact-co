---
id: T-20260812-daily-gross-ordered
title: Aggregate non-cancelled order totals by ordered_at
status: done
effort: S
budget_iterations: 15
agent: any
depends_on: []
touches_paths: []
creates_paths: [dbt/models/staging/stg_daily_gross_ordered.sql]
source_note: storage/specs/4-plan-transform.md
created: 2026-08-12
tags: [dbt, staging, transactco]
signed_off: true
signed_off_by: luanmorenomaciel
signed_off_at: 2026-08-14T01:41:33Z
signed_off_sig: hmac-sha256-v3:ed0abaaf:6259fbdf3f477754efadb67d6592520e73bfa076a66f136e227caa24a5a2ffb7
accepted: true
accepted_by: luanmorenomaciel
accepted_at: 2026-08-14T17:48:15Z
accepted_tier: 1
accepted_attempt_id: 02a276bd-e977-402c-b210-bd8a82557eed
accepted_authorization_ref: hmac-sha256-v3:ed0abaaf:6259fbdf3f477754efadb67d6592520e73bfa076a66f136e227caa24a5a2ffb7
acceptance_record_digest: sha256:9516382870b2c2470acbd247bc33095fbf8c98ac1c6295d651d2887906560ea2
blocked_reason: (none)
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
- **B-1** — GIVEN raw orders carrying six distinct statuses
  WHEN `stg_daily_gross_ordered` aggregates `total_amount` by `ordered_at`
  THEN orders with status `cancelled` are excluded from the total.
- **B-2** — GIVEN the aggregate is published
  WHEN anyone reads its name or its labels
  THEN it is described by its physical basis and never as "Revenue".

## Success Criteria

```bash
# eval-1 (verifies B-1): the model exists and the project parses
eval_1() { make dbt-check >/dev/null 2>&1; }

# eval-2 (verifies B-1): the exclusion is expressed in the model
eval_2() { grep -q "cancelled" dbt/models/staging/stg_daily_gross_ordered.sql; }

# eval-3 (verifies B-2): the boundary holds — nothing here is named revenue
eval_3() { ! grep -ril "revenue" dbt/models/ | grep -q . ; }
```

## Validation Card

```yaml
success_criteria:
  - id: eval_1
    description: The model exists and the dbt project parses
    runnable: bash
    terminal: true
    expected_duration_sec: 20
    verifies: [B-1]
  - id: eval_2
    description: Cancelled orders are excluded in the model
    runnable: bash
    terminal: true
    expected_duration_sec: 1
    verifies: [B-1]
  - id: eval_3
    description: No model under dbt/models/ is named revenue
    runnable: bash
    terminal: true
    expected_duration_sec: 1
    verifies: [B-2]

retry_policy:
  max_iterations: 15
  circuit_breaker_no_progress: 3
  on_terminal_failure: park_with_context

agent_contract:
  version: 2
  read: [intent, behavior, contract, guardrails, operations]
  produce: [dbt/models/staging/stg_daily_gross_ordered.sql]
  required_tools: [bash, dbt]
  timeout_minutes: 15
  sandbox_type: host
  emit: [pass, fail, retry_with_reason, parked_with_context]
  backend_metadata: {}
```


## Exit Check

```bash
eval_1 && eval_2 && eval_3
```

## Anti-Patterns
- **Don't name it revenue** — Revenue is unresolved and owned by Finance.
  Label the aggregate by its physical basis instead.
- **Don't net returns into the total** — refunds are counted, never subtracted.

## Do-Not-Touch
- `storage/specs/` — Day 1 and Day 2 evidence, read-only tonight
- `src/transactco/control/` — instructor surface

## Open Questions
(none — this task is fully specified)