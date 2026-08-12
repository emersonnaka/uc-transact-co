# Task-Spec 3.6.0 — Independent Analysis

## A. METADATA

- run ID: unassigned
- provider: OpenRouter (harness-reported)
- exact model: qwen/qwen3.8-max (harness string `openrouter/qwen/qwen3.8-max`)
- date: 2026-08-12
- web research used: no — raw.githubusercontent fetch returned 404; used a local clone verified at pinned commit `ad511d3eda64f29c6d1a86e45ada28d6175d8f31` (clean tree).
- sources accessed: README.md; spec/task-spec-v3.md; docs/concepts/{task-spec-format, decomposition, eval-driven-development, conformance-levels}.md; docs/guides/multi-harness.md; docs/runbooks/dark-factory-as-task-spec.md; release/evidence.json; TODO.md; docs/roadmap.md; docs/examples/task-plan.yaml; adapters/engines/; spec/conformance/.
- independence: no other model's response was read.

## B. REVEAL CARD

- **central thesis:** An atomic task becomes the ecosystem's unit of exchange when it carries bounded scope, sealed authority, and executable proof any gate can check.
- **killer insight:** Move "done" from scheduler prose into the task as executable, sealed checks; every component becomes swappable.
- **five breakthroughs:**
  1. Executable done: bash evals + Exit Check make completion an exit code, not a progress report.
  2. Bidirectional B-N ⇄ `verifies:` traceability; no dangling promise, no scope-creep test, validator-enforced.
  3. PRE-gate HMAC v2 seal over authority fields (paths, deps, budgets, backend) before delegation.
  4. Independent POST-gate: executor never grades itself; evals, blast radius, and seal re-verified.
  5. Credential-free TaskHandoff/v1 plus L0–L2 conformance with a reference executor.
- **ecosystem role:** the unit-of-work layer under protocols (A2A/MCP), orchestrators (Temporal/LangGraph), sandboxes (E2B), and executors (Codex/Claude): define, authorize, verify one task — nothing else.
- **6–12 month bet (forecast):** real multi-engine CI lands; sealed holdout evals and MCP exposure follow; atomic specs become the verifiable payload between trackers, orchestrators, and fleets.
- **greatest limitation:** eval quality is the oracle ceiling — bash can't judge intent-fidelity, gaming is mitigated not eliminated, and multi-engine proof is still unfinished.
- **confidence score:** 72/100 (format claims: high; ecosystem thesis: moderate).

## C. ATOMICITY COMPARISON (Q1)

| Artifact | Write surface | Done means | Who verifies | Portable/authorized |
|---|---|---|---|---|
| TODO | none declared | human feels it is done | human memory | no |
| Issue | none declared | closed by someone | human judgment, prose | tracker-bound |
| Prompt | implicit, unbounded | model stops talking | vibes | none; no seal |
| Workflow step | engine-defined | step callback returns | the engine that runs it | engine-locked |
| Task-Spec | declared union of paths | Exit Check exits 0 | independent POST-gate | sealed, any conformant harness |

The difference: scope, done, authority, and verification are validator-enforced fields, not conventions a human must remember.

## D. BACKEND ALIGNMENT (Q5)

| layer | responsibility | examples | owned by Task-Spec | not owned by Task-Spec |
|---|---|---|---|---|
| Unit of work | scope, done, authority for one change | Task-Spec | fully: format, gates, seals, handoff | — |
| Agent protocols | task state between agents | A2A Tasks, MCP Tasks | status→A2A TaskState mapping; payload alignment roadmap (P2-2) | transport, discovery |
| Orchestration | scheduling, retries, durability | Temporal, Inngest, Trigger.dev, LangGraph | DAG validation, ready frontier, concurrency groups | dispatch, queues, durable execution |
| Execution environments | isolation, workspaces | E2B, Daytona, git worktrees | workspace + write-scope declaration, blast-radius check | provisioning, network/process isolation |
| Executors | doing the work | Codex, Claude, Gemini, Kimi, Copilot, Droid | portable handoff, adapters (codex/claude/kimi/gemini/custom), conformance L0–L2 | model calls, credentials |
| Systems of record | tracking, reporting | GitHub, Linear, Symphony | `tracker_ref` backlinks, status transitions; MCP tracker adapters roadmap (P2-3) | issue lifecycle, dashboards |

### Q6 — Two representations (illustrative sketches, grounded in this repo)

Ready — dbt staging model:

```yaml
id: T-20260812-stg-orders
status: ready
effort: S
depends_on: []
creates_paths: [dbt/models/staging/stg_orders.sql, dbt/models/staging/_stg_orders__models.yml]
# B-1 GIVEN raw orders mirrored WHEN dbt builds THEN stg_orders passes schema tests
# eval_1: dbt build --select stg_orders+0  → exit 0   (verifies B-1)
# Do-Not-Touch: src/transactco/control/**, storage/specs/**
```

Blocked — semantics owned by Finance:

```yaml
id: T-20260812-int-revenue
status: blocked
blocked_reason: "Revenue definition (statuses, timestamp) unresolved; owner: Finance"
depends_on: []
# Open Questions: which statuses/timestamps count as Revenue?
# Fallback: none — executor must not guess. Gate never runs; blocked ≠ ready.
```

Key move: an open semantic question is a machine-enforced blocker (A2A `input-required`), not a footnote.

## E. FORECAST (Q7 — explicitly forecasts)

| prediction | confidence | confirmation signal | failure condition |
|---|---|---|---|
| Model routing shifts to capability-priced dispatch of sealed atomic tasks; specs carry backend hints, routers pick executors | 55% | routers accepting TaskHandoff-like payloads; per-task price quotes | routing stays prompt-level; specs need bespoke translation |
| Persistent agents keep ledgers of atomic tasks; `blocked`/`parked` become standard resume states across sessions | 60% | ≥2 major harnesses persisting task state natively | agents remain session-scoped, re-deriving context |
| Sandboxed execution pairs with declared write surfaces; acceptance checks diff against scope inside sandboxes | 65% | sandboxes exposing scope-aware acceptance hooks | sandboxes stay scope-blind; blast radius checked nowhere |
| Independent verification separates from execution (dark factories): schedulers shrink to dispatch+eval-run | 50% | public fleets publishing acceptance-rate metrics from gates | executors keep self-grading; no third-party acceptance demand |

## F. CURRENT VERSUS ROADMAP

Implemented or demonstrated today (claims checked at ad511d3):

- ✓ TaskPlan/v1 (`taskspec.dev/v1`) with explicit `depends_on` graph; backlog analysis detects cycles, dangling deps, dual creation, overlapping writes, write-disjoint concurrency groups.
- ✓ Runnable leaves XS/S/M/L (one coherent done-condition; L gated on long-horizon backends); XL/XXL composition nodes own no writes, never delegated.
- ✓ B-N Given/When/Then behaviors with validator-enforced bidirectional eval traceability.
- ✓ Bounded write surface (`touches_paths`+`creates_paths`, Do-Not-Touch), enforced at acceptance as blast-radius check.
- ✓ `blocked`/`parked` states, `blocked_reason`, open questions as first-class holes (A2A input-required mapping).
- ✓ effort sizing, `budget_iterations` (cap 30), iteration/wall-clock/token budgets in handoff; HMAC v2 seal over authority fields.
- ✓ PRE-gate (`gate --stamp` → DELEGATE/TIER), credential-free TaskHandoff/v1, POST-gate (`accept --stamp`; only acceptance writes `accepted*`, `done` requires it).
- ✓ Multi-harness adapters (codex, claude-code, kimi, gemini, anthive, taskship, custom); L0–L2 conformance with reference executor `ref-executor.sh`; `make check` → CHECK=READY; experience suite 26/26.

Unproven, unfinished, or planned:

- ✗ Real multi-engine CI matrix (P0-1): credential-free CI + badge exist; runs with ≥2 real engines remain TODO.
- ✗ Sealed holdout evals (P1-1, format v4), graded `check_type` (P1-2), mutation matrix (P1-3), key rotation/identity (P1-4), security/sandbox doctrine pass (P1-5).
- ✗ MCP server exposure (P2-1), A2A payload alignment (P2-2), MCP tracker adapters (P2-3), environment contract (P2-4), versioned distribution (P2-5), conformance badge program (P2-6).
- ✗ Tag-dependent installs pending `v3.6.0` tag (curl/npm doors `pending_release_tag` in evidence.json).
- Declared limits confirmed: not a hosted service; not a fleet scheduler; does not execute models; HMAC ≠ individual identity; `accepted: true` ≠ deployment/production health (`production_evidence: not_claimed`).

## G. VERDICT

- **Strongest argument:** author / executor / verifier are separated and enforced mechanically. "Done" is sealed before delegation and re-proven after by a gate the executor cannot write. That is the minimum trust substrate a multi-agent ecosystem needs, and no mainstream tracker/orchestrator provides it.
- **Strongest counterargument:** structural validation is not semantic truth. The oracle is only as good as hand-written bash evals: Goodhart-gaming is mitigated, not eliminated; intent-fidelity is unjudgeable in bash (graded checks are roadmap); all evidence is local-suite, single-repo, and the multi-engine proof is still missing. Adoption claims (adopters list) are asserted, not independently verified here.
- **Missing evidence (Q8):** confirm = real-engine CI green on every push; third-party executors publishing certified L2; acceptance-rate metrics from unattended runs; holdout/mutation evals shipping. Falsify = multi-engine matrix never lands; no external adopter passes conformance; gaming incidents show evals pass while intent fails; A2A/MCP ecosystems standardize a competing unit of work.
- **Conclusion:** Task-Spec 3.6.0 delivers its format and gate claims — implemented, internally evidenced, honestly bounded. The atomic-unit thesis is a reasonable extrapolation from real separation-of-powers design, but remains a forecast: production and multi-vendor evidence do not exist yet.

## H. AUDIENCE EXPLANATION (~45s)

Today, when we hand work to an AI agent, "done" is whatever the agent says it is. Task-Spec flips that: each task is one file that declares exactly which files it may touch, carries its own runnable pass/fail checks, and gets digitally sealed by a human before any agent touches it. One gate checks the contract before work; a separate gate re-runs the checks after. The agent never grades itself, and the same task can be handed to Codex, Claude, or Kimi unchanged. It's not a scheduler or a model — it's the missing unit of work. Ecosystem adoption remains an open bet.
