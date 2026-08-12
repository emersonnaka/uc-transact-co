# Task-Spec 3.6.0 — Independent Critical Evaluation

## A. METADATA

- run ID: 05 (per `Reveal/manifest.yaml`)
- provider: Moonshot AI (Kimi Code CLI 0.31.1)
- exact model: `kimi-for-coding` per CLI config (a `-highspeed` profile exists; serving profile not disambiguated — recorded as a limitation)
- date: 2026-08-12
- web research used: no — canonical repository only
- sources accessed: clone of `github.com/luanmorenommaciel/task-spec` at `ad511d3eda64f29c6d1a86e45ada28d6175d8f31` — all nine prioritized files, plus conformance-levels.md, signed-off.md, docs/examples/*, one diamond-6 fixture, spec/conformance/README.md, .github/workflows/ci.yml

## B. REVEAL CARD

- central thesis: One task becomes a sealed, portable contract — bounded writes, executable done-criteria, independent acceptance — so any conformant agent executes it and no executor grades itself.
- killer insight: "Done" is an exit code produced by a separate gate, not the agent's self-report.
- five breakthroughs:
  1. Runnable bash evals embedded in the spec make completion mechanically decidable.
  2. Validator-enforced bidirectional B-N behavior↔eval traceability kills unverified promises and scope-creep tests.
  3. HMAC v2 seals body plus authority fields — paths, dependencies, budgets, backend — before delegation.
  4. PRE-gate sign-off and POST-gate acceptance are separate moments; execution never certifies itself.
  5. Credential-free TaskHandoff/v1 freezes one transfer boundary across Codex, Claude, Kimi, Grok, custom engines.
- ecosystem role: The unit-of-work contract layer — below trackers and schedulers, above sandboxes, agnostic to models: the noun their verbs operate on.
- 6–12 month bet (forecast): Task-shaped contracts with embedded evals get absorbed into A2A/MCP payloads and tracker-to-agent pipelines; conformance suites decide the winner.
- greatest limitation: Cross-engine portability rests on design plus local suites; the real multi-engine CI matrix is unfinished, and weak evals stay gameable.
- confidence score: 62

## C. ATOMICITY COMPARISON

| Unit | "Done" defined by | Write authority | Verified by | Portability |
|---|---|---|---|---|
| TODO | reader's memory | none | nobody | a text line |
| Issue | discussion, human judgment | repo permissions | human review | one tracker |
| Prompt | model's self-report | unbounded | the prompter's eyeballs | one harness |
| Workflow step | the runner's exit status | job-scoped credentials | rerun the step | one orchestrator |
| Task-Spec | executable evals + Exit Check | sealed `touches_paths`/`creates_paths` | independent PRE/POST gates | any conformant executor |

Q1: a TODO is intent without verification; an issue's done is social; a prompt is ephemeral and self-graded; a workflow step's done lives in its scheduler. The atomic Task-Spec carries done-condition, write boundary, and authorization inside the unit, so executor and verifier can both be swapped.

### The format on real work (Q6)

Ready leaf — dbt staging model (load-bearing fields only):

```yaml
id: T-20260812-stg-orders
status: ready
effort: S                      # runnable leaf, ≤2 paths
depends_on: []
touches_paths: [dbt/models/staging/stg_orders.sql]
creates_paths: [dbt/models/staging/_stg_orders.yml]
# B-1: GIVEN raw.orders WHEN dbt build THEN rowcount = control sum; evals carry verifies: [B-1]
# sealed via `taskspec gate --stamp` (HMAC v2)
```

Blocked atom — semantic hole owned by Finance:

```yaml
id: T-20260812-gold-daily-revenue
status: blocked                # maps to A2A input-required
blocked_reason: "Revenue definition unresolved — owner: Finance"
depends_on: [T-20260812-stg-orders]
touches_paths: []              # nothing delegated while the hole is open
# Open Questions: "Which statuses and timestamps count as Revenue? Ask Finance. Fallback: none."
```

The blocked task is structurally withheld — the gate never runs on it — not a prose "TBD" an executor might ignore.

## D. BACKEND ALIGNMENT

| layer | responsibility | examples | responsibility owned by Task-Spec | responsibility not owned by Task-Spec |
|---|---|---|---|---|
| Trackers | queue, priority, triage | GitHub, Linear, Symphony | `tracker_ref` backlink; tracker adapters roadmap (P2-3) | ordering, priority, issue lifecycle |
| Protocol | inter-agent state transport | A2A Tasks, MCP Tasks | status→A2A `TaskState` mapping today; payload embedding roadmap (P2-1/P2-2) | transport, sessions, streaming |
| Orchestration | scheduling, retries, durable runs | Temporal, Inngest, Trigger.dev, LangGraph | explicit `depends_on` DAG, ready frontier; deliberately no scheduler | dispatch, parallelism, cron, sagas |
| Sandboxes | isolation, environments | E2B, Daytona, worktrees | declares `sandbox_type`; acceptance checks local blast radius | actual isolation — HMAC is not a sandbox |
| Agent harnesses | doing the work | Codex, Claude, Gemini, Kimi, Copilot, Droid | one sealed handoff any conformant executor consumes (adapter docs: codex, claude-code, gemini, kimi, custom; none observed for Copilot/Droid) | prompting, tools, internal loop |
| Models | reasoning, routing | — | nothing; never invokes or selects a model | everything |

Q5: below trackers and schedulers, beside A2A/MCP as payload, above sandboxes, in front of harnesses as their contract.

## E. FORECAST

All rows are forecasts, not capabilities.

| prediction | confidence | confirmation signal | failure condition |
|---|---|---|---|
| Model routing becomes a policy layer above sealed tasks; handoff backend selection is today's seam | medium | routing policy appears in TaskHandoff or releases | single hard-coded backends persist |
| Sandboxed execution binds to the handoff (worktree/E2B per leaf) | high | `sandbox_type` values beyond `host` enforced, not just declared | field stays advisory prose |
| Independent verification deepens: sealed holdout evals (P1-1) ship in format v4 | medium-high | v4 spec with hidden eval block released | evals stay worker-visible and gamed |
| Dark factories move done-criteria from scheduler prose into tasks; multi-engine CI lands | medium | P0-1 badge green on ≥2 real engines | portability evidence stays ref-executor-only |

## F. CURRENT VERSUS ROADMAP

Implemented or demonstrated today (at `ad511d3`):

- v3 format: six zones, profiles, B-N⇄eval traceability, validator-enforced both directions
- XS–L runnable leaves; XL/XXL composition nodes; node-refusal conformance-tested
- PRE-gate sign-off with HMAC v2 seal; POST-gate acceptance writing a separate `accepted: true` envelope
- `blocked` + `blocked_reason` + Open Questions as structural holes; A2A TaskState mapping
- TaskPlan/v1, credential-free TaskHandoff/v1, AuthoringEvidence schemas with checked-in examples
- L0–L2 conformance levels plus reference executor; release/evidence.json reports `make check` pass, experience suite 26/26
- Install destinations for Codex/Claude Code/Kimi/Grok; offline, credential-free core

Unproven, unfinished, or planned:

- Real multi-engine CI matrix (P0-1; current CI is credential-free `make check` on two OSes only)
- Sealed holdout evals, graded `check_type`, mutation matrix (P1-1–P1-3)
- Per-author identity and key rotation (P1-4); HMAC is shared-key, not identity
- MCP server, deeper A2A payload alignment, tracker adapters (P2-1–P2-3)
- Any production or deployment evidence — explicitly not claimed; `accepted: true` is a local gate result

## G. VERDICT

- strongest argument (Q3): It separates what agentic tooling usually fuses — authorization, execution, verification — into markdown+YAML+bash small enough to be genuinely vendor-neutral. Eval-decides-done plus sealed authority converts "trust the agent" into "rerun the gate," which unattended work requires.
- strongest counterargument (Q4): The moat is only as deep as the evals. Exit codes verify presence and behavior, not intent or quality; Goodhart gaming is acknowledged but only mitigated, and the strongest fixes (holdout evals, graded judges) are roadmap. The headline "any conformant executor" lacks its promised multi-engine CI proof, so portability today is a design property plus reference-executor evidence. The repo itself cites METR's Task Standard: good formats lose without ecosystem pull.
- missing evidence (Q8): Confirms the thesis — P0-1 matrix green on ≥2 real engines, third-party executors certifying L2, acceptance-rate metrics from real backlogs. Falsifies it — handoffs needing per-engine spec edits, agents passing evals while failing PR review, or the ecosystem standardizing on tracker-native or A2A-native task formats instead.
- final conclusion: An honest, well-bounded artifact that does what it claims at the pinned commit and names its own gaps. Atomic tasks as a fundamental unit are plausible precisely because the format refuses to be a scheduler, sandbox, or model. But the thesis is unproven beyond one author's ecosystem; treat it as a credible contract candidate, not a settled standard.

## H. AUDIENCE EXPLANATION

Task-Spec makes "a task for an AI agent" work like a shipping container. Today you hand an agent a prompt and trust its self-report. A Task-Spec packs one piece of work into a standard box: which files it may touch, which commands prove it done, a tamper-evident seal showing a human approved exactly this, and a separate inspector who re-runs the proof afterward. A standard box means the same task can go to OpenAI's, Anthropic's, or Moonshot's agent — and no agent marks its own homework. The caveat: the proof is only as good as the tests inside, and the cross-vendor promise is unproven at scale. Strong, self-aware design; the ecosystem evidence is still catching up.
