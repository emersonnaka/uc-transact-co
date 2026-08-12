# A. METADATA

- run ID: unassigned
- provider: OpenAI
- exact model: unknown-model — the runtime identifies this agent as Codex/GPT-5-based but exposes no exact model identifier
- date: 2026-08-12
- web research used: yes
- sources accessed: pinned commit [`ad511d3`](https://github.com/luanmorenommaciel/task-spec/tree/ad511d3), specifically `README.md`, `spec/task-spec-v3.md`, all seven requested docs/evidence/roadmap files, plus schemas and gate/executor code; primary documentation for [A2A](https://a2a-protocol.org/latest/specification/), [MCP Tasks](https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/tasks), [Temporal](https://docs.temporal.io/), [Inngest](https://www.inngest.com/docs/learn/how-functions-are-executed), [Trigger.dev](https://trigger.dev/docs/how-it-works), [LangGraph](https://langchain-ai.github.io/langgraph/index.html), [E2B](https://e2b.dev/docs/sdk-reference/js-sdk/v2.10.5/sandbox), [Daytona](https://www.daytona.io/docs/en/sandboxes/), [Git worktrees](https://git-scm.com/docs/git-worktree.html), [Codex](https://developers.openai.com/codex/cli), [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [Kimi](https://www.kimi.com/help/kimi-code/cli-getting-started), [Copilot](https://docs.github.com/en/copilot/how-tos/use-copilot-agents), [Droid](https://factory.ai/news/factory-is-ga), [GitHub Issues](https://docs.github.com/en/issues), [Linear](https://linear.app/docs/assigning-issues), and [Symphony](https://github.com/openai/symphony/blob/main/SPEC.md).

# B. REVEAL CARD

- central thesis: Atomic tasks can become an agentic ecosystem interface when intent, authority, dependencies, execution limits, and independent proof travel together.
- killer insight: Portability comes from moving “done” into the task, not standardizing the agent.
- five breakthroughs:
  1. Explicit task DAG with executable leaves, non-executable composition nodes, and structural blockers.
  2. Given/When/Then behaviors linked bidirectionally to runnable evaluations.
  3. Bounded write authority sealed before delegation and rechecked afterward.
  4. PRE authorization, execution, and POST acceptance are separate responsibilities.
  5. Credential-free handoff plus testable L0–L2 executor conformance.
- ecosystem role: A task-level ABI between trackers/orchestrators, coding harnesses, workspaces, and verifiers; not a scheduler, sandbox, model, or service.
- 6–12 month bet: Routers will dispatch sealed atomic contracts to specialized persistent agents in ephemeral sandboxes, while independent verifiers—not executors—control completion.
- greatest limitation: Executable checks measure proxies; weak or incomplete evals can certify the wrong outcome, and semantic ownership cannot be automated away.
- confidence score: 84

# C. ATOMICITY COMPARISON

| unit | primary purpose | usual “done” | authority/dependencies | key distinction |
|---|---|---|---|---|
| TODO | Reminder | Checked box | Usually absent | Tiny prose marker, not an execution contract. |
| Issue | Coordinate and track work | Human/workflow status | Optional relations and permissions | May contain discussion, priority, or many outcomes; usually not independently executable. |
| Prompt | Invoke a model | Model responds | Session/tool permissions | Transient instruction; typically lacks stable identity, graph position, sealed scope, and external acceptance. |
| Workflow step | Durable program action | Runtime return/state | Orchestrator-defined | Owns execution/retry semantics inside Temporal, Inngest, Trigger.dev, or LangGraph; often infrastructure-coupled. |
| Task-Spec | Portable repository-change contract | Runnable exit check plus POST acceptance | Explicit DAG, write scope, budgets, seal | One bounded leaf carries behavior, proof, authority, failure state, and handoff across harnesses. Semantic quality remains human-authored. |

# D. BACKEND ALIGNMENT

| layer | responsibility | examples | responsibility owned by Task-Spec | responsibility not owned by Task-Spec |
|---|---|---|---|---|
| Work contract | Define one authorized, verifiable change | Task-Spec | Goal, DAG edges, leaf/node type, scope, behaviors/evals, limits, gates, handoff | Priority and business meaning |
| Agent transport | Exchange state, messages, artifacts, deferred results | A2A Tasks, MCP Tasks | Potential payload/state mapping | Discovery, wire transport, polling, authentication |
| Durable orchestration | Schedule, persist, retry, coordinate | Temporal, Inngest, Trigger.dev, LangGraph | Exposes dependencies/readiness and retry budget | Queues, timers, leases, fleet concurrency, durable state |
| Execution environment | Isolate filesystem/process/network | E2B, Daytona, worktrees | Declares workspace and allowed paths | Provisioning, isolation enforcement, credentials, network policy |
| Executor | Reason, edit, run tools | Codex, Claude, Gemini, Kimi, Copilot, Droid | Normalized consumer contract and conformance tests | Model inference, tool loop, implementation quality |
| Work system/factory | Intake, ownership, dispatch, review | GitHub, Linear, Symphony | Can attach a precise executable contract/receipt | Portfolio tracking, scheduling, PR lifecycle, factory operations |

# E. FORECAST

These are forecasts, not current Task-Spec capabilities.

| prediction | confidence | confirmation signal | failure condition |
|---|---:|---|---|
| Routers select models per atom using risk, effort, cost, and eval history. | 82% | Same sealed digest succeeds across vendors with measurable quality/cost gains. | Routing adds variance or cost without better acceptance. |
| Persistent agents plus factory schedulers consume tracker queues and escalate only blocked/failed atoms. | 68% | Multi-day unattended batches produce independently accepted changes and auditable resumptions. | Agents still require prompt-by-prompt supervision or lose context. |
| Ephemeral sandboxes or constrained worktrees become the default execution boundary. | 86% | Handoffs bind reproducible images, network/secret policy, and disposable workspaces. | Host execution remains dominant or isolation overhead outweighs safety. |
| Independent verifiers add mutation tests, hidden checks, receipts, and different-model review. | 78% | False-green rates fall and acceptance predicts human/production outcomes. | Goodhart gaming persists or verifier cost exceeds saved rework. |

# F. CURRENT VERSUS ROADMAP

## Implemented or demonstrated today

- `TaskPlan/v1` schema and CLI represent approved units, `depends_on` edges, XS–L executable leaves, and write-free XL/XXL composition nodes; backlog code detects cycles, dangling edges, overlaps, and the ready frontier.
- Format v3 declares one coherent result, bounded `touches_paths`/`creates_paths`, effort, iteration/token limits, backend/agent authority, blocked reason, and Open Questions. Coherence itself is a review judgment, not mechanically proved.
- Standard/full tasks require B-N Given/When/Then behavior and both directions of behavior↔eval coverage. Runnable bash and Exit Check coverage are validated.
- PRE-gate validates and optionally HMAC-v2 seals body plus authority. `TaskHandoff/v1` rejects nodes, unsigned specs, backend conflicts, and credential-bearing keys.
- POST-gate independently reruns evals, checks changed paths and do-not-touch, verifies the seal, then stamps acceptance; gold-sanity is optional.
- L0–L2 conformance tooling and a deliberately dumb L2 reference executor exist. `release/evidence.json` reports `make check`, clean-room, 26/26 experience, and install passes; I inspected that evidence record but did not rerun gates.

Example ready physical dbt leaf:

```yaml
id: T-20260812-stage-payments
status: ready
effort: S
depends_on: []
creates_paths: [dbt/models/staging/stg_payments.sql]
goal: Materialize source-faithful payment fields without defining Revenue.
behavior: "B-1 Given raw payments, when dbt builds, then physical rows and types match the approved source contract."
eval_1: "make dbt-check  # verifies B-1"
```

Example semantic hole:

```yaml
id: T-20260812-define-revenue
status: blocked
blocked_reason: Finance must choose amount, statuses, and timestamp for Revenue.
touches_paths: []
open_question: "Finance: what exactly counts as Revenue?"
```

It must not be sealed, delegated, or given an invented eval; after Finance answers, a new/updated leaf can encode that authorized meaning.

## Unproven, unfinished, or planned

- No hosted service, fleet scheduler, model execution, sandbox enforcement, credential store, or production-health proof. HMAC is shared-key tamper evidence, not individual identity/non-repudiation.
- Multi-harness adapters/installers demonstrate design portability, not real cross-vendor reliability. The ≥2-real-engine CI matrix remains P0.
- Sealed holdout evals, graded/human checks, mutation matrix, key rotation/per-author signing, stronger untrusted-text controls, sandbox doctrine, MCP server, deeper A2A alignment, tracker adapters, environment contracts, conformance badges, and fleet metrics are roadmap items.

# G. VERDICT

- strongest argument: Task-Spec creates a narrow, inspectable interface where schedulers can swap executors and environments without changing authorized intent or acceptance. That decoupling is valuable precisely because model and harness performance will keep moving.
- strongest counterargument: It can standardize the envelope while leaving the hardest problem—writing discriminating, non-gameable evaluations—unsolved. For design, exploration, and contested semantics such as Revenue, forced atomicity creates false certainty.
- missing evidence: repeated real-engine runs; third-party L2 implementations; comparative trials against ordinary issues/prompts; authoring-cost and false-green measurements; security red-teaming; and evidence that local acceptance predicts review, deployment, and production health. The thesis is falsified if these show no net reliability/throughput gain or persistent oracle gaming.
- final conclusion: Task-Spec 3.6.0 is a credible implemented reference for bounded, evaluable repository work, not yet an ecosystem standard. Atomic tasks could become fundamental as a task-level ABI, but only where human-owned meaning can be converted honestly into executable observations.

# H. AUDIENCE EXPLANATION

A normal ticket tells an agent what someone wants. Task-Spec tries to package the whole safe handoff: what may change, what must not change, what depends on what, how much effort is authorized, and which executable checks prove the result. It seals that contract before work and has a separate gate rerun the checks afterward. That makes the task portable between Codex, Claude, Kimi, or another conformant executor, while schedulers and sandboxes remain replaceable infrastructure. The important caveat is that checks are only as wise as their authors. Task-Spec cannot decide what Revenue means, prove production health from a local test, identify an HMAC signer, or run an autonomous fleet. Its thesis becomes real only if multi-engine evidence shows better reliability than good tickets plus CI.
