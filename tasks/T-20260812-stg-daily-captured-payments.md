---
id: T-20260812-stg-daily-captured-payments
title: "Sum captured payments per UTC calendar day"
status: ready
format_version: 3
profile: standard
effort: M
budget_iterations: 15
agent: developer
parent: (none)
depends_on: [T-20260812-raw-payments-source]
touches_paths: []
creates_paths: [dbt/models/staging/stg_daily_captured_payments.sql]
source_note: "storage/specs/4-plan-transform.md#item-8"
created: "2026-08-12T00:00:00Z"
tags: [transform, staging, item-8]
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
signed_off_at: 2026-08-14T01:41:51Z
accepted: false
accepted_by: (none)
accepted_at: (none)
signed_off_sig: hmac-sha256-v3:ed0abaaf:d98f381f41c7cff4d225a0f1e431b50a6389c51e54029895c23492183bbd31c2
---

# Sum captured payments per UTC calendar day

> **Why:** Candidate 2 in the technical brief, R$ 980,870.44 over 632 payments, has to stay reproducible beside candidate 1, which is what makes the two numbers comparable instead of contradictory.

## Goal

Aggregate captured payment amounts by paid_at in UTC.

## Context

Scope reduction. Item 8 names mart_daily_captured_payments; under the staging-only contract this model becomes stg_daily_captured_payments. Item 4 (stg_payments) does not exist, so this model reads source('raw', 'payments') directly. Same UTC calendar-day technical window as item 7. This unit does not claim capture is the recognition event, since D2 is unresolved under Finance.

## Behavior

- **B-1** — GIVEN payments carrying the two-value status vocabulary captured plus refunded WHEN the daily model is parsed THEN it groups on paid_at cast to a UTC date, filters status to captured, exposes no column named revenue

## Success Criteria

```bash
# eval_1: the model parses on the paid_at grain filtered to captured
eval_1() {
  make dbt-check && grep -q "paid_at" dbt/models/staging/stg_daily_captured_payments.sql && grep -q "captured" dbt/models/staging/stg_daily_captured_payments.sql && ! grep -qi "revenue" dbt/models/staging/stg_daily_captured_payments.sql
}

```

## Validation Card

```yaml
success_criteria:
  - id: eval_1
    description: "the model parses on the paid_at grain filtered to captured"
    runnable: bash
    check_type: deterministic
    verifies: [B-1]
    terminal: true
    expected_duration_sec: 120
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
eval_1
```

## Rollback Plan

Revert only the declared write surface and park the task with context.

## Observability Hooks

(none — no runtime observability required)

## Anti-Patterns

- Do not label this aggregate as recognized revenue, since D2 is unresolved.
- Do not subtract refunded payments, since D3 is unresolved.

## Do-Not-Touch

- `src/transactco/control`
- `storage/specs`
- `dbt/models/staging/_raw_sources.yml`

## Open Questions

D2 — is the recognition event order placed, payment captured, or delivery? Owner is Finance, per storage/specs/2-ontology.md. This unit publishes a capture-clock measurement without asserting it is the recognition event.
