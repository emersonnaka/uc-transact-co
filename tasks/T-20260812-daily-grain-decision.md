---
id: T-20260812-daily-grain-decision
title: "Halt on the business day grain decision"
status: ready
format_version: 3
profile: standard
effort: S
budget_iterations: 15
agent: architect
parent: (none)
depends_on: [T-20260812-stg-daily-captured-payments]
touches_paths: []
creates_paths: []
source_note: "storage/specs/4-plan-transform.md#items-7-8-d4-block"
created: "2026-08-12T00:00:00Z"
tags: [escalation, semantics, d4]
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

# Halt on the business day grain decision

> **Why:** D4 is unresolved, so choosing a business-day grain here would be an agent deciding business meaning that storage/specs/2-ontology.md assigns to Finance.

## Goal

Escalate the business day grain question to its named owner.

## Context

Scope reduction applies to the two models under review. They live in dbt/models/staging/ as stg_ models rather than mart_ models, per the Day 2 contract. Item 7 is not a unit of this manifest, since the backlog already carries T-20260812-daily-gross-ordered, which creates dbt/models/staging/stg_daily_gross_ordered.sql under the same rules; only item 8 is authored here, so depends_on names only the captured-payments unit while this review still inspects both daily models. This unit writes no model, which is why its write surface is empty. It confirms both daily models still declare a UTC calendar-day technical window, confirms no aggregate has been renamed Revenue, then stops at the D4 block. The verdict belongs to Finance; the architect role writes nothing.

## Behavior

- **B-1** — GIVEN D1 to D4 recorded unresolved in storage/specs/2-ontology.md WHEN the staging tree is inspected after items 7 plus 8 land THEN no business-day grain exists anywhere in staging, no model or column is named revenue, both daily models still parse

## Success Criteria

```bash
# eval_1: staging carries no business-day grain plus no revenue naming
eval_1() {
  ! grep -riE "business_day|business day|revenue" dbt/models/staging/ && make dbt-check && make test
}

```

## Validation Card

```yaml
success_criteria:
  - id: eval_1
    description: "staging carries no business-day grain plus no revenue naming"
    runnable: bash
    check_type: deterministic
    verifies: [B-1]
    terminal: true
    expected_duration_sec: 240
retry_policy:
  max_iterations: 15
  circuit_breaker_no_progress: 3
  on_terminal_failure: park_with_context
agent_contract:
  version: 2
  read: [intent, behavior, contract, guardrails]
  produce: [escalation]
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

Nothing to revert, since this unit writes no files. Park it with the owner name if D4 stays open.

## Observability Hooks

(none — no runtime observability required)

## Anti-Patterns

- Do not implement a business-day calendar before Finance resolves D4.
- Do not present candidate 1 or candidate 2 as the revenue number.
- Do not close this unit by choosing a grain; close it by recording the owner's answer.

## Do-Not-Touch

- `src/transactco/control`
- `storage/specs`
- `dbt/models/staging/_raw_sources.yml`

## Open Questions

D4 — is the daily grain a store-timezone business day or a UTC calendar day? Owner is Finance. D4 — which currency handling applies to a multi-currency day? Owner is Finance. D1, D2, plus D3 also stay unresolved, so no aggregate from items 7 to 8 may be renamed Revenue. Owner is Finance, per storage/specs/2-ontology.md.
