# Reveal — Task-Spec 3.6.0 as the Atomic Unit of Agentic Work

## A. METADATA

- run ID: unassigned
- provider: openrouter
- exact model: minimax/minimax-m3 (MiniMax-M3)
- date: 2026-08-12
- web research used: yes (corroboration only; primary source is the pinned repo)
- sources accessed: `luanmorenommaciel/task-spec@ad511d3` — `README.md`, `spec/task-spec-v3.md`, `docs/concepts/{decomposition,eval-driven-development,conformance-levels,signed-off,six-zones,profiles,agent-contract}.md`, `docs/guides/multi-harness.md`, `docs/runbooks/dark-factory-as-task-spec.md`, `release/evidence.json`, `spec/conformance/README.md`, `TODO.md`, `docs/roadmap.md`

## B. REVEAL CARD

- **central thesis (≤30):** Task-Spec 3.6.0 is a vendor-neutral, HMAC-sealed, self-verifying unit of work — one PR's worth of change packed into a portable contract any conformant executor can run and only an independent gate can accept.
- **killer insight (≤20):** "Done" is not narration; it is the green exit of a sealed bash eval run by a gate that did not write the code.
- **five breakthroughs (≤20 each):**
  1. B-N ⇄ `verifies:` bidirectional Behavior↔eval traceability enforced by the validator.
  2. HMAC v2 envelope binds body, write scope, dependencies, budget, and backend — not just bytes.
  3. Sealed `TaskHandoff/v1` is credential-free and engine-agnostic; same digest, every harness.
  4. Three-tier PRE-gate (T1 crypto / T2 structural-only / T3 hard-fail) binds absence of a key to supervision.
  5. Conformance L0/L1/L2 with vendored fixtures and a reference executor — the standard is testable, not asserted.
- **ecosystem role (≤30):** A unit-of-work format that sits below orchestrators (Converge, taskship, Temporal) and above any agent that can run bash; the missing link between LLM intent and deterministic acceptance.
- **6–12 month bet (≤30):** Atomic, sealed, self-verifying tasks become the agent hand-off lingua franca, forcing every harness to expose a conformance level and every fleet to expose a POST-gate.
- **greatest limitation (≤30):** The pyramid rests on the quality of deterministic bash evals; semantic, subjective, or multi-agent outputs still need a human or a graded oracle Task-Spec does not yet ship.
- **confidence score: 62/100** — high on in-repo claims, low on ecosystem-level predictions.

## C. ATOMICITY COMPARISON

| Aspect | TODO | Issue | Prompt | Workflow step | Task-Spec |
|---|---|---|---|---|---|
| Unit of meaning | line item | stateful discussion | intent | one fixed transformation | one PR's worth of work |
| Success criterion | no | implicit | no | implicit | runnable bash evals + Exit Check |
| Authorization | no | no | no | rarely | HMAC v2 (`signed_off_sig`) |
| Write surface | no | no | no | runner-dependent | `touches_paths` + `creates_paths` + Do-Not-Touch |
| Dependency graph | no | tracker-only | no | yes (DAG) | `depends_on` + `parent`, validated |
| Independent acceptance | no | no | no | partial | yes — POST-gate, separate from executor |
| Status lifecycle | done / won't fix | tracker enum | n/a | state machine | ready → in-progress → done / parked / blocked |
| Structural blocks | none | labels | none | none | `status: blocked` + `blocked_reason` + Open Questions zone |
| Cross-harness portability | n/a | tracker-coupled | no | no | yes — same digest, every conformant engine |

## D. BACKEND ALIGNMENT

| Layer | Responsibility | Owned by Task-Spec | Not owned by Task-Spec |
|---|---|---|---|
| Intent / spec | write the contract | six-zone anatomy, Behavior B-N, validation card | debate, prioritization |
| Decomposition | break FEATURE into atoms | `TaskPlan/v1`, `depends_on`, XL/XXL, hole-as-blocker | resource allocation |
| Authorization | seal the contract | PRE-gate, T1/T2/T3 envelopes, HMAC v2 | per-author identity (asymmetric sigs) |
| Dispatch | pick ready leaves, route | `taskspec handoff`, ready frontier | parallelism policy, cross-DAG retries |
| Execution | the one PR | sealed handoff, normalized `agent_contract` | model selection, prompt strategy |
| Acceptance | prove done | `accept --stamp --gold-sanity`, blast-radius, seal re-verify | deployment, production health |
| Operation | backlog, lint, metrics | readiness, dependency, write-conflict detection | scheduling, cost dashboards, fleet |
| Orchestration | strategy, loops, PR | none — explicitly someone else's job | loops, tracker projection, fleet autonomy |

## E. FORECAST

| Prediction | Confidence | Confirmation signal | Failure condition |
|---|---|---|---|
| Each serious agent harness (Codex, Claude, Kimi, Grok, Droid) ships a Task-Spec conformance badge within 12 months. | Medium | Public `L1`/`L2` self-tests in vendor ADRs; `VENDORED_FROM` rows re-vendored. | Harnesses ship ad-hoc formats; Task-Spec remains one of many. |
| MCP-server dispatch (P2-1) becomes the dominant hand-off surface. | Medium-high | `taskspec mcp` server in `bin/`; agents consume `claim/eval/submit` natively. | Per-harness adapters remain the norm; MCP stays a thin wrapper. |
| A2A `TaskState` mapping proves real interop, not paper alignment. | Medium | Production A2A dispatcher ingests `status: blocked` as `input-required`. | Converge-only deployments; no external dispatcher reads `ts_a2a_state`. |
| Sealed holdout evals (P1-1) become the differentiator once shipped. | High signal value, low chance of 12-month landing | `--reveal-holdout` flag at accept time. | Roadmap stalls; graded `check_type` (P1-2) is needed first. |

## F. CURRENT VERSUS ROADMAP

**Implemented today (v3.6.0, `ad511d3`):**
- Six-zone anatomy with `Behavior` B-N and `Contract` (validation card + Exit Check); bidirectional traceability enforced by `validate-task-spec.sh`.
- HMAC v2 envelope, three tiers, Tier-2 supervised-only policy.
- `taskspec` CLI: `init / plan / batch / validate / dod / gate --stamp / handoff / run / accept --stamp --gold-sanity / conformance`.
- `TaskPlan/v1`, `TaskHandoff/v1`, `AuthoringEvidence/v1`; size-bounded leaves (XS/S/M/L) and non-runnable composition nodes (XL/XXL).
- Multi-harness adapters (Codex, Claude, Kimi, Grok, custom), credential-free.
- Conformance L0/L1/L2 with `run_conformance.sh` and `ref-executor.sh`; `make check` lands at `CHECK=READY`; experience suite 26/26.
- Bug-class detection: `--gold-sanity`, dual-creation, overlapping writes, cycles, dangling deps.

**Unproven, unfinished, or planned (`TODO.md`, `docs/roadmap.md`):**
- P0-1: real multi-engine CI matrix (only credential-free `make check` proven; vendor engines not yet gated).
- P1-1: sealed holdout evals (format v4) — strongest integrity upgrade on the table.
- P1-2: graded `check_type` (`graded`, `human`) — subjective correctness unsolved.
- P1-3: mutation matrix (generalize `--gold-sanity`).
- P1-4: key rotation, per-author signing identity, asymmetric signatures.
- P1-5: security pass; T1-only for unsupervised dispatch.
- P2-1/2/3: MCP server, deeper A2A, tracker adapters via MCP.
- P3-3: fleet metrics dashboards.
- Live research providers (Firecrawl/Tavily/Exa) — explicitly not advertised; only fake adapters ship.

## G. VERDICT

- **Strongest argument:** Authority is pinned to bytes, not to a chatbot. HMAC v2 plus an independent POST-gate means tampering with eval, scope, dependency, or backend breaks the seal — the gate does not share the executor's memory.
- **Strongest counterargument:** Everything reduces to `bash eval returns 0`. The Goodhart guard is acknowledged but not solved; semantic correctness, design taste, and multi-agent coherence are explicitly outside the contract.
- **Missing evidence:** No published independent benchmark showing real engines at `L1`/`L2` against the conformance fixtures; no runtime data beyond the 26/26 experience suite; no measurement of duplicate-pick, write-conflict, or acceptance-rate regressions in a real fleet.
- **Final conclusion:** Credible attempt to make one atomic unit of agent work vendor-neutral, tamper-evident, and independently verified — on the structure. Production-strength claim unproven until P0-1 ships and ≥2 engines run the conformance suite green in CI. Treat as a serious primitive, not a finished standard.

## H. AUDIENCE EXPLANATION

~45 seconds:

> "Today, when you ask a coding agent to ship a change, you mostly trust it. Task-Spec says: don't trust — verify. It turns one piece of work into a small Markdown contract: what may change, what bash command proves it worked, and who signed off — sealed with a cryptographic signature that breaks on any later edit. Any conformant engine picks up the same sealed task, does the work, and an independent gate, separate from the engine, reruns those bash checks before declaring the task done. The interesting claim isn't that this is clever. It's that this might be the right *unit* for the agentic ecosystem — the way a commit is the unit of version control, or a package is the unit of distribution. The format is open, the conformance suite is vendorable, and the boundaries are honest: it doesn't schedule a fleet, doesn't run a model, doesn't claim its seal proves identity. The honest prediction is that atomic, self-verifying tasks become the way agents hand work to each other. The honest caveat is that we lack evidence from a real multi-engine CI matrix, and the whole edifice rests on the quality of the bash evals you write. Treat it as a serious primitive — not a finished standard."
