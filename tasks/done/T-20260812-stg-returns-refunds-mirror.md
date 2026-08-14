---
id: T-20260812-stg-returns-refunds-mirror
title: "Mirror returned orders against refunded payments"
status: done
format_version: 3
profile: standard
effort: M
budget_iterations: 15
agent: developer
parent: (none)
depends_on: [T-20260812-raw-payments-source]
touches_paths: []
creates_paths: [dbt/models/staging/stg_returns_refunds.sql]
source_note: "storage/specs/4-plan-transform.md#item-6"
created: "2026-08-12T00:00:00Z"
tags: [transform, staging, item-6]
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
signed_off_at: 2026-08-14T01:25:50Z
accepted: true
accepted_by: luanmorenomaciel
accepted_at: 2026-08-14T17:50:58Z
signed_off_sig: hmac-sha256-v3:ed0abaaf:3850002e4dbe52c062f0077201e44b36cff90d2ae1abeff24f126da9c07cd18d
accepted_tier: 1
accepted_attempt_id: 0fb3d77f-9c10-45e9-bfca-2bb387ee98ef
accepted_authorization_ref: hmac-sha256-v3:ed0abaaf:3850002e4dbe52c062f0077201e44b36cff90d2ae1abeff24f126da9c07cd18d
acceptance_record_digest: sha256:aca414099da0f9e2638fab6936d60f7ce02461c65c7e290a3d48550e32e4b72a
---

# Mirror returned orders against refunded payments

> **Why:** E9 reports 3,049 refunded payments equal to 3,049 returned orders. That equality is a measurement to publish, never an adjustment to apply.

## Goal

Build the refunded to returned mirror as two counted sides.

## Context

Scope reduction. Item 6 names int_returns_refunds; under the staging-only contract this model becomes stg_returns_refunds. Observed in infra/postgres/init/01_schema.sql — the database carries four tables, customers, products, orders, payments. There is no returns table plus no refunds table, so the mirror compares orders.status = 'returned' from the E5 vocabulary against payments.status = 'refunded' from the E6 vocabulary. D3, which decides whether refunds subtract plus in which period, is unresolved under Finance, so this unit only counts both sides side by side.

## Behavior

- **B-1** — GIVEN 3,049 refunded payments facing 3,049 returned orders WHEN the mirror model is parsed THEN both sides appear as counted columns, with no subtraction applied to any amount

## Success Criteria

```bash
# eval_1: the mirror parses, counts both sides, subtracts nothing
eval_1() {
  make dbt-check && grep -qi "returned" dbt/models/staging/stg_returns_refunds.sql && grep -qi "refunded" dbt/models/staging/stg_returns_refunds.sql && ! grep -qiE "amount[[:space:]]*-|-[[:space:]]*sum" dbt/models/staging/stg_returns_refunds.sql
}

```

## Validation Card

```yaml
success_criteria:
  - id: eval_1
    description: "the mirror parses, counts both sides, subtracts nothing"
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

- Do not net refunds against order or payment amounts, since D3 is unresolved.
- Do not present the mirror as a correction to any daily total.

## Do-Not-Touch

- `src/transactco/control`
- `storage/specs`
- `dbt/models/staging/_raw_sources.yml`

## Open Questions

D3 — do refunds subtract in-period, subtract at-origin, or report separately? Owner is Finance, per storage/specs/2-ontology.md. This unit does not need D3 answered, since it only counts. Any model that subtracts does.
