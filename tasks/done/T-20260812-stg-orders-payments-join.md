---
id: T-20260812-stg-orders-payments-join
title: "Join orders to payments keeping every order"
status: done
format_version: 3
profile: standard
effort: M
budget_iterations: 15
agent: developer
parent: (none)
depends_on: [T-20260812-raw-payments-source]
touches_paths: []
creates_paths: [dbt/models/staging/stg_orders_payments_reconciled.sql, dbt/models/staging/_stg_reconciled.yml]
source_note: "storage/specs/4-plan-transform.md#item-5"
created: "2026-08-12T00:00:00Z"
tags: [transform, staging, item-5]
owner: (none)
priority: P2
severity: feature
due_date: (none)
precondition: (none)
blocked_reason: (none)
security_class: (none)
source_action_item: (none)
tracker_ref: (none)
execution_backend: claude
signed_off: true
signed_off_by: luanmorenomaciel
signed_off_at: 2026-08-14T01:25:39Z
accepted: true
accepted_by: luanmorenomaciel
accepted_at: 2026-08-14T17:50:05Z
signed_off_sig: hmac-sha256-v3:ed0abaaf:3c8232395e64132ccddd5a260cc2eec21f5e6fd8ab3cf5b08c3a92b6e98ba7d6
accepted_tier: 1
accepted_attempt_id: 2574a9ff-9436-4736-9995-0aeaf28d7f58
accepted_authorization_ref: hmac-sha256-v3:ed0abaaf:3c8232395e64132ccddd5a260cc2eec21f5e6fd8ab3cf5b08c3a92b6e98ba7d6
acceptance_record_digest: sha256:6678d57aee78b648b7e65d90726426612ddfa1e3f688d3e505936246f68fc958
---

# Join orders to payments keeping every order

> **Why:** E7 reports 0 amount mismatches where a payment exists, plus E8 counts 2,204 orders with no payment row. Both facts survive only under a left join that leaves the missing side null.

## Goal

Build the order to payment left join at one row per order.

## Context

Scope reduction. Item 5 names int_orders_payments_reconciled; under the Day 2 staging-only contract this model becomes stg_orders_payments_reconciled inside dbt/models/staging/. Prerequisite recorded, not assumed — item 4 (stg_payments) does not exist, since dbt/models/staging/ currently holds only stg_orders.sql plus _raw_sources.yml. This unit therefore reads source('raw', 'payments') directly, the same way stg_orders reads source('raw', 'orders'). Repointing to ref('stg_payments') once item 4 lands is a separate unit. No aggregation here.

## Behavior

- **B-1** — GIVEN 8,000 order rows facing the raw payments table WHEN the reconciled model is parsed THEN the SQL is a left join anchored on orders, carrying no filter on payment status
- **B-2** — GIVEN the 2,204 orders that E8 shows carry no payment row WHEN the reconciled model is read THEN those rows expose a null payment amount beside an explicit has_payment flag, never 0.00

## Success Criteria

```bash
# eval_1: the model parses as a left join anchored on orders
eval_1() {
  make dbt-check && grep -qi "left join" dbt/models/staging/stg_orders_payments_reconciled.sql && ! grep -qi "inner join" dbt/models/staging/stg_orders_payments_reconciled.sql && ! grep -qi "group by" dbt/models/staging/stg_orders_payments_reconciled.sql
}

# eval_2: missing payments stay null behind an explicit has_payment flag, with coalesce forbidden outright in this model
eval_2() {
  ! grep -qi "coalesce" dbt/models/staging/stg_orders_payments_reconciled.sql && grep -q "has_payment" dbt/models/staging/stg_orders_payments_reconciled.sql && grep -q "has_payment" dbt/models/staging/_stg_reconciled.yml
}

```

## Validation Card

```yaml
success_criteria:
  - id: eval_1
    description: "the model parses as a left join anchored on orders"
    runnable: bash
    check_type: deterministic
    verifies: [B-1]
    terminal: false
    expected_duration_sec: 120
  - id: eval_2
    description: "missing payments stay null behind an explicit has_payment flag, with coalesce forbidden outright in this model"
    runnable: bash
    check_type: deterministic
    verifies: [B-2]
    terminal: true
    expected_duration_sec: 30
retry_policy:
  max_iterations: 15
  circuit_breaker_no_progress: 3
  on_terminal_failure: park_with_context
agent_contract:
  version: 2
  read: [intent, behavior, contract, guardrails]
  produce: [code, tests]
  required_tools: [git, bash]
  timeout_minutes: 30
  sandbox_type: host
  output_artifacts: []
  mcp_dependencies: []
  emit: [pass, fail, retry_with_reason, parked_with_context]
  backend_metadata: {}
```

## Exit Check

```bash
eval_1 && eval_2
```

## Rollback Plan

Revert only the declared write surface and park the task with context.

## Observability Hooks

(none — no runtime observability required)

## Anti-Patterns

- Do not use an inner join, which silently drops the 2,204 unpaid orders.
- Do not coalesce a missing payment amount to 0.00.
- Do not aggregate in this unit.

## Do-Not-Touch

- `src/transactco/control`
- `storage/specs`
- `dbt/models/staging/_raw_sources.yml`

## Open Questions

(none — the join is a physical reconciliation, carrying no business rule)
