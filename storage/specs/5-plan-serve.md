# 5 — Sketch Plan: Serve (API/MCP over the gold layer) — enumerated only

- **Author:** architect (judgment, no hands) · **Status:** enumeration — the
  build belongs to the end of the week, at its own checkpoint
- **Basis:** `3-technical-brief.md` · `4-plan-transform.md` · decisions
  `D1`–`D4` from `2-ontology.md`
- **Prerequisite:** nothing here is built before the marts in plan 4 pass their
  gates.

| # | Item | Evidence | State |
| - | --- | --- | --- |
| 1 | Read-only surface over the marts from plan 4; no write path, no direct access to `public.*` | harness contract, `analytics_ro` | clear |
| 2 | Resource `candidate_daily_gross_ordered` — returns the aggregate under the name of its physical basis | brief, candidate 1 | clear |
| 3 | Resource `candidate_daily_captured_payments` — same treatment | brief, candidate 2 | clear |
| 4 | Order↔payment coverage resource, including the orders without payment | E7, E8 (2,204) | clear |
| 5 | Returns and refunds resource, reported separately, never netted | E9 (3,049 = 3,049) | clear |
| 6 | Every response carries provenance: evidence IDs, capture revision, and mirror timestamp | E10, revision `5143f85` | clear |
| 7 | Freshness notice: the fixture is time-relative and `make bootstrap` invalidates the numbers; the response must expose the capture, never assume it | `1-context.md`, capture note | clear |
| 8 | Controlled-refusal handler: any request for "Revenue" returns a refusal naming `2-ontology.md` and the Finance owner | `2-ontology.md`, controlled refusal | clear |
| 9 | The "yesterday" parameter — requires an explicit UTC window from the caller; interpreting "yesterday" is choosing a timezone and a business day | brief, open question | **BLOCKED — D4, Finance** |
| 10 | Any endpoint or MCP tool named `revenue`, or any single number presented as Revenue | `2-ontology.md` | **BLOCKED — D1–D4, Finance** |

Nothing in this list is authorized to be built at this checkpoint.
