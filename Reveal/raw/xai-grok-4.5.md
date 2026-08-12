# Task-Spec 3.6.0 — Independent Technical Analysis

## A. Metadata

- **run ID:** unassigned
- **provider:** xAI
- **exact model:** Grok 4.5
- **date:** 2026-08-12
- **web research used:** no (primary sources only; public unauthenticated API 404; local checkout at `ad511d3`)
- **sources accessed:** `README.md`, `spec/task-spec-v3.md`, `docs/concepts/task-spec-format.md`, `docs/concepts/decomposition.md`, `docs/concepts/eval-driven-development.md`, `docs/concepts/conformance-levels.md`, `docs/guides/multi-harness.md`, `docs/runbooks/dark-factory-as-task-spec.md`, `release/evidence.json`, `TODO.md` @ `ad511d3eda64f29c6d1a86e45ada28d6175d8f31`

---

## B. Reveal card

| Field | Content |
|---|---|
| **central thesis** | Atomic, sealed, eval-proven work units can become the portable substrate between intent systems, harnesses, and independent gates. |
| **killer insight** | Done is an exit code, not a narrative the agent writes about itself. |
| **breakthrough 1** | Runnable bash evals as the contract of “done,” not prose criteria. |
| **breakthrough 2** | Bidirectional B-N ↔ `verifies:` traceability enforced by validation. |
| **breakthrough 3** | Separated PRE-gate (HMAC v2) and POST-gate (independent acceptance). |
| **breakthrough 4** | Leaves vs composition nodes with explicit write-surface bounds. |
| **breakthrough 5** | Credential-free `TaskHandoff/v1` plus L0–L2 executor conformance. |
| **ecosystem role** | Unit-of-work format and local referee—not a runtime, fleet, or model host. |
| **6–12 month bet** | **Forecast:** sealed contracts win only if multi-engine CI and holdouts become routine evidence. |
| **greatest limitation** | Local/structural green ≠ production proof; multi-engine CI and anti-gaming holdouts unfinished. |
| **confidence score** | 78 |

---

## C. Atomicity comparison

| Dimension | TODO | Issue | Prompt | Workflow step | Task-Spec |
|---|---|---|---|---|---|
| Unit | Informal note | Ticket + discussion | Instruction blob | DAG/flow step | Sealed PR-sized atom |
| Done | Human checkbox | Human close | Model self-report | Orchestrator transition | Runnable evals + Exit Check |
| Write scope | Implicit | Often none | Unbounded | Env-defined | `touches_paths` ∪ `creates_paths` |
| Authority | None | Assignees | Session trust | Workflow IAM | HMAC v2 PRE-gate |
| Dependencies | Ad hoc | Links/epics | Context stuffing | Explicit edges | `depends_on` / nodes / TaskPlan |
| Failure | Forgotten | Stale open | Hallucinated success | Retry/policy | fail-closed; `blocked`/`parked` |
| Portability | Local list | Tracker-bound | Harness-bound | Platform-bound | Markdown+YAML+bash |

---

## D. Backend alignment

| layer | responsibility | examples | owned by Task-Spec | not owned by Task-Spec |
|---|---|---|---|---|
| Work unit | Atomic work, evals, scope, budgets | Task-Spec v3, TaskPlan/v1 | Format, validation, DoD, seals, handoff | Business priority, product meaning |
| Protocol | Interop task state | A2A Tasks, MCP tools | Status↔A2A mapping; blocked→input-required | Full transport; MCP server (roadmap) |
| Orchestration | Schedule, durable flows | Temporal, Inngest, Trigger.dev, LangGraph | Ready frontier / dependency lint | Fleet multi-worker runtime |
| Environment | Isolate compute | E2B, Daytona, worktrees | Declares `sandbox_type` | Actual network/process isolation |
| Harness | Produce code | Codex, Claude, Gemini, Kimi, Copilot, Droid | Handoff + skill install doors | Model inference, tools |
| Tracker | Human backlog | GitHub, Linear, Symphony | Optional `tracker_ref` | Issue lifecycle, prioritization |

---

## E. Forecast

*Forecasts only—not demonstrated capabilities.*

| prediction | confidence | confirmation signal | failure condition |
|---|---|---|---|
| Routing uses sealed effort/backend/budget fields, not free-form prompts | medium | Pipelines select backend only from `TaskHandoff/v1` | Private per-vendor prompt packs persist |
| Sandboxed leaves become default for unattended Tier-1 | medium-high | CI requires sandbox + sealed scope for T1 | Unattended host runs with HMAC as “security” |
| Independent POST-gate / holdouts become procurement bar | medium | Sealed holdouts (P1-1) in real CI | “Agent said done” or weak presence checks remain |
| Dark factories work only where evals own “done” | medium | Drivers shrink to schedule + Task-Spec evals | Scheduler prose re-absorbs stall criteria |

---

## F. Current versus roadmap

### Implemented or demonstrated today (3.6.0 / `ad511d3`)

- **TaskPlan/v1** with explicit dependencies (`plan` / `batch --plan`)
- **Leaves** (XS/S/M/L) and **nodes** (XL/XXL: no writes, never delegated)
- One coherent done-condition per leaf; bounded write surface; cycle/overlap lint
- **B-N** Given/When/Then; bidirectional `verifies:` (hard-fail on standard/full)
- `status: blocked` + `blocked_reason` + Open Questions as structural holes
- Effort, `budget_iterations`, agent_contract budgets; HMAC **v2** authority envelope
- **PRE-gate** stamp and **POST-gate** `accepted: true` (executor does not self-grade)
- Credential-free **TaskHandoff/v1**; multi-harness install/handoff doors
- Conformance L0–L2 + reference executor self-test; `make check` / experience 26/26
- Non-goals in `evidence.json`: not hosted, not fleet scheduler, no production claim

### Unproven, unfinished, or planned

- Real multi-engine CI with ≥2 live engines (**TODO P0-1** remaining)
- Sealed holdout evals; graded/human checks; mutation matrix (**P1-1–P1-3**)
- Per-author identity / key rotation / remote fleet verify (**P1-4**)
- MCP server; deeper A2A payload; tracker MCP adapters (**P2**)
- Live research providers not advertised; tag-dependent install doors pending
- Local acceptance ≠ deployment/production health (standing limitation)

### Claims check

| Claim | Verdict |
|---|---|
| TaskPlan/v1 + dependency graph | Implemented |
| Leaves + composition nodes | Implemented |
| One coherent done condition | Implemented (leaves) |
| Bounded writes | Implemented |
| B-N behaviors + bidirectional evals | Implemented (profile-gated) |
| Blocked / open questions structural | Implemented |
| Effort/budget/authority | Implemented; HMAC ≠ identity |
| PRE-gate; TaskHandoff/v1; POST-gate | Implemented |
| Multi-harness portability | Design+install+handoff yes; multi-engine CI incomplete |
| Conformance + ref executor | Implemented / self-tested |
| Not hosted/fleet/model-host; accept≠prod; holdouts roadmap | Confirmed |

---

## G. Verdict

**Strongest argument.** Agentic failure is often ambient trust plus narrative “done.” Task-Spec packages scope, behaviors, executable observations, budgets, and a seal that breaks if those change after human sign-off—portable across harnesses without credentials. Ready vs blocked work can be structural (e.g. dbt staging vs Finance-owned Revenue) without inventing business meaning.

**Strongest counterargument.** Weak oracles dominate: bash evals are Goodhart-vulnerable; HMAC does not sandbox or identify authors; `accepted: true` is local, not ops truth. Multi-engine CI and holdouts unfinished means “vendor-neutral” and “unattended-safe” are stronger as architecture than field evidence. Authoring cost may exceed value for subjective work.

**Missing evidence.** Production case studies; live multi-engine green matrices; merge-error reduction; third-party L2 badges; adversarial eval resistance.

**Final conclusion.** Task-Spec 3.6.0 is a serious, bounded *unit-of-work standard* with real local gates—not a factory runtime. Atomic tasks become fundamental only if contracts + independent verification are treated as infrastructure. Thesis is plausible and well-scoped; not yet falsification-proof.

### Format-faithful sketches (illustrative)

**Ready — dbt staging:** `status: ready`, `effort: S`, `touches_paths: [dbt/models/staging/stg_orders.sql]`, B-1 build / B-2 physical column contracts (no Revenue definition), evals via scoped `dbt`/`make dbt-check`, blast radius rejects non-staging writes.

**Blocked — Revenue:** `status: blocked`, `blocked_reason: "Revenue definition owned by Finance; unresolved"`, Open Questions on statuses/timestamp/gross-vs-net; no PRE-gate until `blocked → ready`.

---

## H. Audience explanation (~45s)

Task-Spec is not another chat prompt and not a robot army. It is a reviewable contract for one coding change: what may be written, which bash checks prove success, and a human seal before any agent runs. Afterward, a separate gate re-runs those checks. If Finance still owns Revenue, the task stays blocked—structure forces an answer instead of a silent guess. That is why atomic tasks might become the agentic unit of work: authority and proof travel with the package, while models, schedulers, and sandboxes stay replaceable. The idea is strong; production-scale proof is still catching up.
