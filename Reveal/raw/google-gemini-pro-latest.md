# Task-Spec 3.6.0: Critical Evaluation

## A. METADATA

- run ID: unassigned
- provider: google
- exact model: gemini-pro-latest
- date: 2026-08-12
- web research used: no
- sources accessed: 
  - `README.md`
  - `spec/task-spec-v3.md`
  - `docs/concepts/decomposition.md`
  - `docs/concepts/eval-driven-development.md`
  - `docs/guides/multi-harness.md`
  - `docs/runbooks/dark-factory-as-task-spec.md`
  - `release/evidence.json`
  - `TODO.md`
  - `docs/concepts/conformance-levels.md`
  - `docs/concepts/agent-contract.md`
  - `docs/trust/index.md`

## B. REVEAL CARD

- central thesis: Task-Spec is a vendor-neutral, self-verifying, atomic unit of work that decouples execution from verification and orchestration via runnable bash evals and HMAC-sealed authorization envelopes.
- killer insight: The `eval` decides "done", not the agent's prose report.
- five breakthroughs:
  1. Executable bash evals define "done".
  2. HMAC v2 seals scope/authorization pre-execution.
  3. L0-L2 conformance testing for executors.
  4. TaskPlan explicitly graphs dependencies (DAG).
  5. Decouples execution from fleet scheduling.
- ecosystem role: The standard protocol (wire format) for agentic work units, enabling interoperability across diverse models, executors, and dispatchers without vendor lock-in.
- 6–12 month bet: We will see the emergence of L2-conformant independent executors routing tasks to optimal models based on verifiable budget and effort declarations.
- greatest limitation: The "Goodhart's Law" problem: Agents gaming evals instead of solving the underlying intent; requires strict discriminating evals and human PR review.
- confidence score: 85

## C. ATOMICITY COMPARISON

| Feature | TODO | Issue | Prompt | Workflow Step | Task-Spec |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Format** | Free text | Prose/Markdown | Free text / Template | Platform specific | Structured Markdown + YAML |
| **Verification** | Manual | Human review / CI | Output review | Step success/fail | Runnable bash evals |
| **Boundaries** | None | Implicit | Best-effort | Explicit context | HMAC-sealed write scope |
| **Dependencies** | Mental | Linked issues | None | Graph/DAG | Explicit `depends_on` |
| **Execution** | Human | Human/Agent | LLM | Orchestrator | Any conformant executor (L0-L2) |
| **Portability** | Universal | Tracker specific | Tool specific | Platform locked | Vendor-neutral |

## D. BACKEND ALIGNMENT

| layer | responsibility | examples | responsibility owned by Task-Spec | responsibility not owned by Task-Spec |
| :--- | :--- | :--- | :--- | :--- |
| **Orchestration** | Fleet scheduling, queuing | Temporal, Inngest | DAG definition, status transitions (`in-progress`, `blocked`, `parked`) | Actually running the queue, resource allocation |
| **Execution** | Running the LLM, sandbox | Claude, Codex, Kimi | The contract the executor MUST follow, conformance tests | Model weights, prompt engineering, container lifecycle |
| **Definition** | What needs to be done | Linear, Jira, PRD | Bounded write surface, success criteria (bash), auth seal | Writing the PRD, gathering context |
| **Verification** | Deciding if it works | GitHub Actions, CI | Local bash evals, blast-radius checks (POST-gate) | Full multi-platform production CI, deployment |

## E. FORECAST

| prediction | confidence | confirmation signal | failure condition |
| :--- | :--- | :--- | :--- |
| Task-Spec adoption drives a market of decoupled L2 executors. | 75 | Multiple open-source or commercial executors boast "Task-Spec L2 Conformance." | Ecosystem remains fragmented with bespoke executor-scheduler monoliths. |
| The format will expand to include "sandbox policy" formally. | 90 | Format v4 includes declarative sandbox requirements (e.g., `requires.network: false`). | Execution remains strictly `host` based without isolation. |
| "Gaming the eval" will cause at least one major publicized incident. | 80 | A post-mortem details an agent passing an eval via a deceptive workaround. | Evals prove completely robust against agent shortcuts. |
| A2A integration makes Task-Spec the dominant payload for Agent-to-Agent handoffs. | 70 | Major platforms natively consume Task-Spec payloads over A2A protocols. | A2A defines its own competing executable specification format. |

## F. CURRENT VERSUS ROADMAP

### Implemented or demonstrated today:
- TaskPlan/v1 explicit dependency graph (`depends_on:`).
- Executable leaves (XS/S/M/L) and composition nodes (XL/XXL).
- One coherent done condition per task (via bash evals).
- Bounded write surfaces (`touches_paths`, `do_not_touch`).
- Bidirectional traceability between behaviors and evaluations (`verifies:`).
- Blocked states and open questions as structural elements.
- Effort, budget (`budget_iterations`), and authority limits.
- PRE-gate before delegation (`safe-to-delegate.sh`).
- POST-gate and acceptance after execution (`accept-task.sh`).
- Portability across different agent harnesses (via `TaskHandoff/v1` and adapter architecture).
- Conformance levels (L0, L1, L2) and a reference executor (`ref-executor.sh`).
- HMAC v2 authorization envelope (tamper evidence).

### Unproven, unfinished, or planned:
- Sealed holdout evaluations (HMAC-sealed second eval block) [Roadmap P1-1].
- Graded `check_type` (model-judged rubric) [Roadmap P1-2].
- Full multi-engine CI proof matrix (running multiple real engines in CI) [Roadmap P0-1].
- Key management (rotation, per-author identity) [Roadmap P1-4].
- MCP server exposing engine as tools [Roadmap P2-1].
- Environment contract (declared setup/teardown hooks) [Roadmap P2-4].
- Fleet metrics dashboards [Roadmap P3-3].

## G. VERDICT

- **strongest argument:** Task-Spec solves the "trust" problem in agentic workflows by replacing agent-authored progress reports with deterministic, locally verifiable, and mathematically sealed (HMAC) contracts, decoupling the definition of work from the specific execution engine.
- **strongest counterargument:** The reliance on bash evals creates a vulnerability to Goodhart's Law; agents are highly capable of finding the path of least resistance to make an exit code `0` without fulfilling the actual intent (gaming the eval).
- **missing evidence:** Empirical data demonstrating that the "Goodhart guard" (discriminating evals, `--gold-sanity` baseline checks) is practically effective at scale against advanced models attempting to shortcut tasks.
- **final conclusion:** Task-Spec 3.6.0 successfully defines a robust, vendor-neutral protocol for agentic work. By treating "done" as an executable state rather than a linguistic claim, and enforcing this via conformance levels, it provides the necessary foundation for true multi-agent, multi-engine autonomous systems, provided the ecosystem can manage the inherent risks of eval-gaming.

## H. AUDIENCE EXPLANATION

Imagine you hire a contractor to build a fence. A normal task list is like telling them, "Build a good fence," and trusting them when they say they're done. Task-Spec is different. It's a sealed contract that says, "Build the fence here, do not touch the garden, and you are only done when this specific weight hangs from the gate without breaking it." 

For AI agents, Task-Spec does exactly this. It takes a piece of work and attaches a mini-program—a bash script—that acts as the judge. The AI isn't done when it *says* it's done; it's done when that script runs and passes. Furthermore, the whole package is cryptographically sealed, so the AI can't rewrite the rules or expand its scope while you aren't looking. This means you can use any AI model you want—Claude, Codex, whatever comes next—because the contract, the boundaries, and the test are all bundled together, completely independent of the AI running it.
