# Task-Spec 3.6.0 — Critical Evaluation

## A. Metadata

- **run ID:** unassigned
- **provider:** deepseek
- **exact model:** deepseek-v4-pro (identifier taken from the runtime-declared model field; treat as machine-reported, not independently verified)
- **date:** 2026-08-12
- **web research used:** yes (web search + firecrawl attempted; the public URL 404s and web results were unrelated — the canonical repo resolved to the local checkout)
- **sources accessed:** `/Users/luanmorenomaciel/GitHub/task-spec@ad511d3` — `README.md`, `spec/task-spec-v3.md`, `docs/concepts/{task-spec-format,decomposition,eval-driven-development,conformance-levels,signed-off}.md`, `docs/guides/multi-harness.md`, `docs/runbooks/dark-factory-as-task-spec.md`, `release/evidence.json`, `TODO.md`, `CHANGELOG.md`, `spec/conformance/`, `src/dispatch/ref-executor.sh`

## B. Reveal Card

- **central thesis:** Atomic tasks become fundamental because Task-Spec makes one unit of work self-verifying, tamper-evident, and vendor-portable — executable and checkable without a human in the loop.
- **killer insight:** The task carries its own definition of done, so any harness can execute it and any gate can verify it.
- **five breakthroughs:** (1) Executable done-condition: bash evals, not prose, decide success. (2) Bidirectional B-N⇄eval traceability, hard-failed both directions. (3) HMAC v2 seal: authority is tamper-evident before delegation. (4) POST-gate acceptance: the executor never grades itself. (5) Conformance L0–L2 plus a reference executor, certifying executors by observation.
- **ecosystem role:** The portable payload and conformance boundary sitting beneath schedulers and above harnesses — a unit-of-work standard that complements, not replaces, orchestration, sandboxes, and models.
- **6–12 month bet:** Self-verifying atomic tasks become the interchange layer for routing and dark factories; sealed holdout evals and real multi-engine CI decide whether trust scales.
- **greatest limitation:** HMAC is symmetric (no per-author identity), evals are gameable, and acceptance is local — trust stops before production, sandboxing, and fleet scheduling.
- **confidence score:** 70

## C. Atomicity Comparison

| Unit | Granularity | Done condition | Write scope | Verifiable | Delegable |
|---|---|---|---|---|---|
| TODO | ad-hoc item | none (prose) | implicit | no | no |
| Issue | feature/bug | human judgement | repo-wide | no | no |
| Prompt | one call | model's own claim | unbounded | no | yes (but unaudited) |
| Workflow step | pipeline stage | upstream stage's exit code | shared | partially | partially |
| Task-Spec | one PR-sized leaf | executable Exit Check | bounded (`touches/creates_paths`) | yes (evals + gate) | yes (sealed) |

The differentiator is **executability + bounded scope + independent verification**: a TODO/issue is *readable*; a Task-Spec is *checkable*.

## D. Backend Alignment

| layer | responsibility | examples | owned by Task-Spec | not owned by Task-Spec |
|---|---|---|---|---|
| Format / unit | define atomic change, done-condition, write scope | Task-Spec v3, TaskPlan/v1, TaskHandoff/v1 | format, schema, validation | execution |
| Orchestration | route, parallelize, queue, schedule | Temporal, Inngest, Trigger.dev, LangGraph, anthive | declares `depends_on` + ready frontier only | worker scheduling, retries at fleet scale |
| Harness / model | run model, apply edits | Codex, Claude, Kimi, Gemini, Copilot, Grok, Droid | `agent_contract` each must honor; adapters | invoking models, producing changes |
| Sandbox | isolate process/network/FS | E2B, Daytona, git worktrees | declares `sandbox_type` | enforcing isolation |
| Routing | choose model per task | model gateways, routers | `execution_backend` field | selection policy |
| Tracker / backlog | issues, PRs, status sync | GitHub, Linear, Jira, Symphony | `tracker_ref` backlink; A2A state mapping | tracker mechanics (MCP adapters = P2-3) |
| Inter-agent protocol | pass tasks between agents | A2A Task, MCP Tasks | A2A `TaskState` mapping today; MCP server = roadmap | the protocol itself |

## E. Forecast

| prediction | confidence | confirmation signal | failure condition |
|---|---|---|---|
| Model routers treat the Task-Spec backend field + conformance level as a routing signal | 75 | routers consume `TaskHandoff/v1` for backend selection | specs stay manually dispatched; routing ignores the payload |
| Persistent agents / dark factories adopt self-verifying task payloads to decouple scheduler from executor | 60 | a shipped factory's done-criteria live in evals, not scheduler prose | factories keep verification inside the driver prompt |
| Sandboxed execution becomes mandatory for unattended dispatch | 70 | Tier-1 unsupervised dispatch requires sandbox doctrine (P1-5 ships) | unattended runs on host sandboxes persist |
| Sealed holdout evals + graded checks close the eval-gaming gap | 55 | format v4 holdout block ships; mutation matrix rejects gameable evals | workers keep optimizing against readable evals |

## F. Current Versus Roadmap

**Implemented or demonstrated today** (verified in-repo): v3 six-zone format with profiles (lite/standard/full); `TaskPlan/v1` with explicit `depends_on`/`parent` DAG; XS/S/M/L leaves + XL/XXL composition nodes; runnable bash evals + single-command Exit Check; bidirectional B-N⇄`verifies:` traceability (validator hard-fails); bounded write surface (`touches_paths`/`creates_paths`/Do-Not-Touch); `blocked`/`blocked_reason`/Open Questions as structural holes; effort/budget/authority limits (`effort`, `budget_iterations`, `retry_policy`, `agent_contract`); PRE-gate `taskspec gate --stamp` with HMAC v2 + Tier 1/2/3; credential-free `TaskHandoff/v1`; POST-gate `taskspec accept --stamp --gold-sanity` → `accepted: true`; conformance L0/L1/L2 with `ref-executor.sh` (self-certified L2) and conformance fixtures; adapters for 7 engines + install doors for Codex/Kimi/Claude/Grok; A2A `TaskState` mapping; evidence.json gates (`make_check` pass, experience suite 26/26, `CHECK=READY`).

**Unproven, unfinished, or planned:** real multi-engine CI matrix (P0-1 — only credential-free `make check` runs today, no claude/codex engines); sealed holdout evals / format v4 (P1-1); graded + human `check_type` (P1-2); mutation matrix for eval quality (P1-3); per-author identity via asymmetric signatures (P1-4); sandbox doctrine for unattended execution (P1-5); MCP server (P2-1); A2A payload alignment (P2-2); tracker MCP adapters (P2-3); conformance badge program (P2-6); v3.6.0 tag not yet published (curl/npm install doors `pending_release_tag`).

**Q6 — representing the dbt/Revenue case:**

```yaml
# ready leaf — dbt staging model
id: T-20260812-stg-orders
status: ready
effort: S
depends_on: []
touches_paths: [dbt/models/staging/stg_orders.sql, dbt/models/staging/schema.yml]
source_note: storage/specs/orders-source.md
---
## Behaviors
- B-1 — GIVEN the dbt project runs WHEN stg_orders is built THEN it materializes and all its tests pass.
## Success Criteria
eval_1() { dbt build --select stg_orders; }
eval_2() { dbt test --select stg_orders; }
```

```yaml
# blocked leaf — Revenue definition belongs to Finance
id: T-20260812-revenue-mart
status: blocked
blocked_reason: "Revenue definition unresolved — owner: Finance"
effort: M
depends_on: [T-20260812-stg-orders]
---
## Open Questions
1. Which statuses and timestamp constitute Revenue? (owner: Finance — escalates, no executor may guess)
```

The `blocked` leaf is withheld from the backlog picker and the gate; it becomes `ready` only after Finance answers. This is the format's core anti-silent-wrong mechanism.

## G. Verdict

- **strongest argument:** It separates "the agent claims done" from "done is proven" — executable, independently re-checkable evals plus tamper-evident authority is precisely the missing trust primitive for autonomous agents.
- **strongest counterargument:** Goodhart's law — an eval is only as honest as its author, and a worker reads the very evals it is graded on. HMAC gives no identity, and the format enforces no sandbox and schedules nothing, so the real autonomy risk lives outside its boundary.
- **missing evidence:** real-engine adoption (same sealed spec green on Codex *and* Claude in CI), third-party executors certified L2, and evals surviving adversarial mutation.
- **final conclusion:** A coherent, unusually honest unit-of-work standard. "Atomic task as fundamental unit" is a defensible design claim backed by working mechanism, not yet an ecosystem fact — the adoption and anti-gaming evidence is the open question.

## H. Audience Explanation

Imagine every piece of software work as a small sealed envelope. Inside is a precise description of one change: exactly which files may be touched, what must be true for the job to count as finished, and a tamper-proof signature proving a human approved that exact job. An AI can open the envelope, do the work, and hand it back — but it cannot stamp its own "done." A separate, independent check re-runs the proof tests and verifies nothing was changed without permission. That is the whole idea: make work small enough to verify, wrap it in a signature, and separate doing from checking. If it works, you can let many different AIs, from many companies, share the same envelopes — and trust the results without watching every step.
