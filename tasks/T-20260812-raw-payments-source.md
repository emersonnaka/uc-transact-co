---
id: T-20260812-raw-payments-source
title: "Declare the raw payments source"
status: ready
format_version: 3
profile: standard
effort: S
budget_iterations: 15
agent: developer
parent: (none)
depends_on: []
touches_paths: [dbt/models/staging/_raw_sources.yml]
creates_paths: []
source_note: "storage/specs/4-plan-transform.md#items-5-8"
created: "2026-08-12T00:00:00Z"
tags: [transform, staging, sources]
owner: (none)
priority: P1
severity: feature
due_date: (none)
precondition: (none)
blocked_reason: (none)
security_class: (none)
source_action_item: (none)
tracker_ref: (none)
execution_backend: claude
signed_off: false
signed_off_by: (none)
signed_off_at: (none)
accepted: false
accepted_by: (none)
accepted_at: (none)
---

# Declare the raw payments source

> **Why:** _raw_sources.yml declares only raw.orders today, so every unit for items 5, 6, plus 8 fails to parse until raw.payments exists as a declared source.

## Goal

Declare the raw.payments source table that items 5 to 8 read.

## Context

Scope reduction recorded for this manifest. Items 5 to 8 name int_ plus mart_ models, but the Day 2 contract authorizes writes only under dbt/models/staging/, so every model below carries an stg_ name inside the staging layer. The intermediate layer plus the marts layer need their own checkpoint. This unit is the shared prerequisite, plus the only unit that writes _raw_sources.yml, which keeps that file free of concurrent writers. Column list from infra/postgres/init/01_schema.sql — payment_id, order_id, amount, method, status, paid_at, ingested_at.

## Behavior

- **B-1** — GIVEN a DuckDB raw mirror carrying public.payments with seven columns WHEN dbt parses the staging directory THEN source('raw', 'payments') resolves with its seven columns declared

## Success Criteria

```bash
# eval_1: dbt parses the project with the payments source declared
eval_1() {
  make dbt-check && grep -q "name: payments" dbt/models/staging/_raw_sources.yml && grep -q "name: paid_at" dbt/models/staging/_raw_sources.yml
}

```

## Validation Card

```yaml
success_criteria:
  - id: eval_1
    description: "dbt parses the project with the payments source declared"
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

- Do not add a source for a table absent from infra/postgres/init/01_schema.sql.
- Do not create a model file in this unit.

## Do-Not-Touch

- `src/transactco/control`
- `storage/specs`

## Open Questions

(none — the physical payments schema is evidenced in infra/postgres/init/01_schema.sql)
