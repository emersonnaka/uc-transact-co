# Day 3 — The Spec: The Unit of Work

> **Repository state:** Day 3 is built and execution has started locally. Its
> first Task-Spec exists as untracked session evidence; the task graph and second
> staging model are not complete. The five inherited specs and Day 2 staging
> model remain committed inputs.

The question carried through the session is:

> The plan says ten items. Which one can I hand to an agent tonight — and how
> will I know it is done without asking you?

The audience should leave understanding that a plan enumerates work but briefs
no one; that "done" is two halves — behaviour a human signs and proof a machine
runs; and that a packet small enough to close inside one context window is the
unit that makes autonomous work reviewable.

## The complete story

```mermaid
flowchart LR
    S0[00 Inheritance] --> S1[01 Plausible plan]
    S1 --> S2[02 Task-Spec]
    S2 --> S3[03 BDD and evals]
    S3 --> S4[04 Decompose]
    S4 --> S5[05 Ready set]
    S5 --> S6[06 Execute one]
    S6 --> S7[07 Reflection]

    classDef setup fill:#E5E7EB,stroke:#4B5563,color:#111827
    classDef fail fill:#FEE2E2,stroke:#DC2626,color:#7F1D1D
    classDef spec fill:#EDE9FE,stroke:#7C3AED,color:#3B0764
    classDef build fill:#DCFCE7,stroke:#16A34A,color:#14532D
    classDef human fill:#FEF3C7,stroke:#D97706,color:#78350F
    class S0 setup
    class S1 fail
    class S2,S3,S4,S5 spec
    class S6 build
    class S7 human
```

## Sequence and deck switches

| Step | Session | Deck cue | Demo evidence | Durable result |
| ---: | --- | --- | --- | --- |
| [`00`](00-inheritance.md) | No agent | What survived the night | Five specs, rails intact, parse with the Day 2 model | Baseline only |
| [`01`](01-plausible-plan.md) | **NEW A** | The plan is not the work | Three divergent plans for item 7 | None — session discarded |
| [`02`](02-task-spec.md) | **NEW B** | Anatomy of a Task-Spec | `T-20260812-daily-gross-ordered.md`, six zones, human-edited | `tasks/T-20260812-daily-gross-ordered.md` |
| [`03`](03-bdd-and-evals.md) | Continue B | Two halves of done | Scenario + pre-build exit check returning non-zero | Evals inside `T-20260812-daily-gross-ordered` |
| [`04`](04-decompose.md) | Continue B as architect | Item 7 becomes a graph | TaskPlan preview → approval → `batch`, then `dod` + `lint` | `tasks/` graph |
| ✦ | No agent | Giveaway → crank | Deck only — 2 slides, ~21:50, 3 min | None — the crank clip is **pre-recorded** |
| [`05`](05-ready-set.md) | Continue B | The ready set | Agent predicts, `taskspec ready` adjudicates | `_state.yaml` ordering |
| [`06`](06-execute-one.md) | **NEW C** — developer | One packet, one iteration | Exit check returns 0 + refusal holds | Second staging model |
| [`07`](07-reflection.md) | No agent | Turn three closes | Participant commitments | Team learning |

Switch in the same rhythm every time:

```text
DECK: explain why
  -> DEMO: perform one bounded action
  -> EVIDENCE: show only the named proof
  -> DECK: state what changed
  -> GATE: continue or keep the failure visible
```

## Output budgets

| Checkpoint | Visible agent response | Artifact budget |
| ---: | --- | --- |
| 00 | None — terminal only | None — read-only |
| 01 | Three plans, 6 lines each | None — never executed |
| 02 | None — the human types | One spec, six zones |
| 03 | One scenario + one eval | Two sections inside `T-20260812-daily-gross-ordered` |
| 04 | 120-word summary | Index + 4–6 packets, ≤200 words each |
| 05 | One table, ≤8 rows | Ordering inside `tasks/_state.yaml` |
| 06 | One sentence per action | One staging model + its test |

## Artifact workspace

```text
storage/specs/
├── 1-context.md            # Day 1 — read-only tonight
├── 2-ontology.md           # Day 1 — read-only tonight · Revenue unresolved
├── 3-technical-brief.md    # Day 1 — read-only tonight
├── 4-plan-transform.md     # Day 2 — TONIGHT'S RAW MATERIAL, read-only
└── 5-plan-serve.md         # Day 2 — read-only tonight

.taskspec/config             # created by taskspec init at checkpoint 04

tasks/
├── .plans/
│   └── transform-5-8.yaml   # the TaskPlan/v1 manifest — reviewed, then approved
├── _state.yaml              # derived index, rebuilt by taskspec rebuild-state
├── _metrics.jsonl           # append-only status log — carries the item-10 refusal
└── T-20260812-*.md          # one Task-Spec per atomic change

dbt/models/staging/          # already holds stg_orders from Day 2
```

`tasks/` intentionally does not exist before the session; the architect
creates it live inside the contract's writable path.

## Shared boundaries

- Postgres access stays read-only (`analytics_ro`); DuckDB `raw.*` is the mirror.
- All five inherited specs are read-only tonight; no checkpoint may overwrite them.
- Writable paths tonight: `tasks/` (including `tasks/.plans/`), `.taskspec/`, and
  `dbt/models/staging/` only.
- Checkpoints 04 and 05 use the real `taskspec` CLI (v3.7.0, MIT) — the same tool
  given away at 21:50. Checkpoint 00 gates on `taskspec version`.
- Item 10 of the transform plan cannot become a task while `Revenue` is
  `unresolved` — the refusal at checkpoint 06 is the success state.
- Session A demonstrates the divergence and is discarded.
- Session B carries spec → BDD → decomposition → ready set, then stops.
- Session C is the developer: receives only its Task-Spec and `AGENTS.md`.
- Instructor `_control`, injection, scoring, and reveal surfaces remain closed.
- Label any fallback artifact **prepared**.
- The giveaway and crank are two deck slides between checkpoints 04 and 05.
  The crank clip is pre-recorded and must be announced as such; there is no
  pricing or offer slide in the current deck.

## Language

Deck copy and these runbooks are English. Prompts pasted on screen are PT-BR —
the room's language, same as Days 1 and 2. Spec content quoted inside a prompt
is quoted verbatim from `storage/specs/`, which is English; do not translate a
spec line into the prompt or back.

## Completion gate

- [ ] The inheritance was verified live (five specs, rails, parse).
- [ ] One plan item produced three divergent plans, and nothing executed.
- [ ] A Task-Spec was written by hand with all six zones present.
- [ ] A scenario and its derived eval were both shown running.
- [ ] Item 7 decomposed into packets with an index and a dependency graph.
- [ ] The ready set was named before any packet was worked.
- [ ] A fresh developer session executed one packet from files alone and its
      exit check returned 0.
- [ ] Item 10 was requested and refused — Revenue still cannot become a task.
- [ ] The room filled the three commitment lines.

The planning source is [`../../plan/semana.md`](../../plan/semana.md); the
deck is [`../../presentation/d3.html`](../../presentation/d3.html). Day 2's
runbook ([`../d2/`](../d2/)) remains the format precedent.
