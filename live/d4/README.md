# Day 4 — The Loop: Dispatch · Proof · Receipt · Measurement

> **Repository state:** Day 3 left a complete, validated, entirely unmoved graph.
> Six Task-Specs in `tasks/`, every one `DOD=COMPLETE`, `done: 0`, nothing signed,
> `tasks/_metrics.jsonl` absent, and **no repository signing key** — so a stamp
> today would be `TIER=2`, not `TIER=1`. Checkpoint `00` fixes that in front of
> the room. `dbt/models/staging/` still holds only `_raw_sources.yml` and
> `stg_orders.sql`.

The question carried through the session is:

> Six specs are ready and nobody has run one. What happens when no one is
> watching — and how do I know the green means anything?

The audience should leave understanding that **a loop is only as honest as its
oracle**; that a passing check is a claim until you have watched it fail for the
right reason; that the evaluator an executor can read is a weaker evaluator; and
that work you cannot measure after the fact was never delegated, only hoped.

## The one idea, stated once

The loop is not the new thing. A loop is a plan-act-measure-correct cycle with an
exit condition — James Watt shipped one in 1788, Norbert Wiener named the field
in 1948, Lisp had a REPL in the early 1960s, and continuous integration has been
one for thirty years. What changed in 2026 is that a language model can sit in
the **body** of the loop, doing the judgment a human used to do.

That moves the scarce part. The scarce part was never the `while`. It is the
signal from **outside** the loop that says the work is really done — software
testing calls it the **oracle**. Nobody fears their thermostat, because its
oracle is a thermometer: cheap, trustworthy, and external to the furnace.

Day 3 built the goal. Tonight builds the oracle.

## The complete story

```mermaid
flowchart LR
    S0[00 Preflight · the unmoved graph] --> S1[01 Green that proves nothing]
    S1 --> S2[02 An eval that can fail]
    S2 --> S3[03 The holdout]
    S3 --> S4[04 The authorization chain]
    S4 --> S5[05 Waves]
    S5 --> S6[06 The unit of measurement]
    S6 --> S7[07 Turn four closes]

    classDef setup fill:#E5E7EB,stroke:#4B5563,color:#111827
    classDef fail fill:#FEE2E2,stroke:#DC2626,color:#7F1D1D
    classDef proof fill:#DCFCE7,stroke:#16A34A,color:#14532D
    classDef seal fill:#CFFAFE,stroke:#0891B2,color:#164E63
    classDef human fill:#FEF3C7,stroke:#D97706,color:#78350F
    class S0 setup
    class S1 fail
    class S2,S3 proof
    class S4,S5 seal
    class S6,S7 human
```

## Sequence and deck switches

| Step | Session | Deck cue | Demo evidence | Durable result |
| ---: | --- | --- | --- | --- |
| [`00`](00-preflight.md) | No agent | The graph that has never moved | `done: 0`, no metrics file, `MISS signing` → key provisioned | `.taskspec/` signing key |
| [`01`](01-green-that-proves-nothing.md) | **NEW A** | Green that proves nothing | An eval returns 0 with nothing built; `gate` refuses to call it delegate-safe | None — session discarded |
| [`02`](02-an-eval-that-can-fail.md) | Continue A → then **NEW B** | An eval that can fail | `eval-audit`: a mutation killed, a mutation **survived** | A discriminating Exit Check |
| [`03`](03-the-holdout.md) | Continue B | An eval the agent cannot read | `HOLDOUT=SEALED` → `HOLDOUT=VERIFIED` → a run receipt the executor never read | A sealed bundle + receipt |
| ✦ | No agent | Break | Deck only — the sealed descriptor stays on screen | None |
| [`04`](04-the-authorization-chain.md) | **NEW C** — developer | The authorization chain | `TIER=1` → `HANDOFF` → exit 0 → `ACCEPTED=1`, plus one honest **REJECT** | A signed, accepted spec + a real staging model |
| [`05`](05-waves.md) | Continue C | Waves | `lint` names the partition; three specs run together; no write collision | Three more staging models |
| [`06`](06-the-unit-of-measurement.md) | No agent | The unit of measurement | `taskspec metrics` — the same command that found nothing at `00` | `tasks/_metrics.jsonl` |
| [`07`](07-reflection.md) | No agent | Turn four closes | Participant commitments | Team learning |

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
| 00 | None — terminal only | One signing key |
| 01 | One eval body, ≤6 lines | None — never kept |
| 02 | One audit table, ≤8 rows | One Exit Check, rewritten |
| 03 | One descriptor + one receipt | One sealed bundle |
| 04 | One sentence per chain step | One staging model + its stamps |
| 05 | One `lint` partition + one wave table | Three staging models |
| 06 | None — `jq` output only | None — read-only |
| 07 | None | Three commitment lines |

## Artifact workspace

```text
storage/specs/                  # Days 1–2 — read-only tonight, all five files
tasks/
├── T-20260812-*.md             # the six inherited specs — tonight they get stamped
├── _state.yaml                 # rebuilt as statuses transition
├── _metrics.jsonl              # DOES NOT EXIST at 00; written by 04 and 05; read at 06
└── .plans/transform.yaml       # Day 3's approved manifest, read-only

.taskspec/
├── config                      # exists (Day 3)
└── signing key                 # MISSING — checkpoint 00 provisions it

tmp/d4/
├── holdout/                    # the sealed bundle and its descriptor
├── audit/                      # eval-audit reports
└── receipts/                   # engine · environment · graded · human receipts

dbt/models/staging/             # holds stg_orders only; gains four models tonight
```

`tasks/_metrics.jsonl` **must not exist** when checkpoint 00 runs — the whole of
Act 6 is the before/after on one command. If a rehearsal created it, checkpoint 00
archives it into `tmp/prepared/` rather than deleting it.

## Shared boundaries

- Postgres access stays read-only (`analytics_ro`); DuckDB `raw.*` is the mirror.
- All five files under `storage/specs/` are inherited evidence and read-only.
- Agent writes remain governed by `AGENTS.md`: the architect writes nothing; the
  developer writes only in `dbt/models/staging/`. Facilitator-controlled paths
  tonight are `tasks/`, `.taskspec/` and `tmp/d4/`.
- Every command is real `taskspec` v3.8.0. Checkpoint 00 gates on
  `taskspec version` and `taskspec setup`.
- **The holdout bundle is never displayed while Session C is alive.** Seal it at
  `03`, show the descriptor and the receipt, never the bundle body. If the room
  asks to see it, that request is the lesson.
- `Revenue` stays unresolved, owner Finance. `T-20260812-daily-grain-decision`
  must still refuse to become ready. Measuring work never earns the right to
  define it.
- Session A is the villain and is **discarded**. Session B carries the proof
  discipline. Session C is the developer and receives only its spec and
  `AGENTS.md`.
- Instructor `_control`, injection, scoring and reveal surfaces stay closed.
- Label any fallback artifact **prepared**.
- **There is no commercial beat between `04` and `05`.** The giveaway, crank and
  Bootcamp handoff slides were removed from the deck; the skill card now sits
  inside Act 2, next to the audit that earns it. The five minutes are slack.
- A guest segment runs at ~20:12: **Rafael Rodrigues on evals**, ten minutes,
  taken out of movement `01` so no later checkpoint moves.

## What is new tonight, and what is only now honest

Two things in this runbook exist because a command contradicted the plan:

1. **`taskspec setup` reports `MISS signing — no repository key`.** Day 3 taught
   `hmac-sha256-v2` and never stamped one, so the repository never needed a key.
   Without it `gate --stamp` degrades to **`TIER=2` — supervised dispatch only**.
   Checkpoint 00 provisions the key so checkpoint 04 can honestly show `TIER=1`.
   If you skip it, do not claim Tier 1 on screen; show `TIER=2` and say why.
2. **`taskspec accept` runs five gates, not one.** A–E under 3.8: evals re-run by
   us; handoff, dependency closure, base commit and blast radius; authorization
   integrity; opt-in gold-sanity; and sealed receipt policy. Gate D is tonight's
   thesis compiled into the tool: it reconstructs the baseline in an ephemeral
   worktree, holds the eval bodies constant, and **requires the evals to fail
   there**. Do not describe `accept` as "re-runs the tests", and do not use the
   3.7 A–F table — 3.8 removed the warn-only isolation gate and renumbered the
   two after it.
3. **`accept` needs the handoff file.** Write it with `handoff --out` and pass it
   back with `accept --handoff`. Without it the acceptance drops to Tier 2 and
   refuses to stamp unless a human adds
   `--allow-tier2 --supervised-by <id> --reason <text>`.

## The skill this night delivers

`skills/prove-the-oracle/` — the packaged method: before you trust a green check,
make it red on purpose; before you delegate, seal the evaluator; after it runs,
keep the receipt. It ships the mutation-discrimination drill, the holdout
lifecycle, and a standalone validator:

```bash
uv run python skills/prove-the-oracle/scripts/validate_oracle.py tasks/T-*.md
```

It must finish `CHECK_ORACLE=PASS`. See
[`../../skills/README.md`](../../skills/README.md) for how the four nights' skills
compose: Night 1 finds what is true, Night 2 grants authority, Night 3 defines the
unit of work, Night 4 proves the signal that closes it.

## Language

Deck copy and these runbooks are English. Prompts pasted on screen are PT-BR —
the room's language, same as Days 1 to 3. Spec content quoted inside a prompt is
quoted verbatim from the repository, which is English; never translate a spec line
into the prompt or back.

## Completion gate

- [ ] The inheritance was verified live: six specs, `done: 0`, no metrics file.
- [ ] The signing key was provisioned, or `TIER=2` was shown and explained.
- [ ] An eval returned 0 while nothing was built, and that session was discarded.
- [ ] A mutation was **killed** and a different mutation **survived**, on screen.
- [ ] The survivor was closed by rewriting the eval, not by weakening the test.
- [ ] A holdout was sealed, verified, and run without the executor reading it.
- [ ] One spec went `TIER=1` → handoff → exit 0 → `ACCEPTED=1`.
- [ ] One acceptance was **rejected** on purpose, and the room saw which gate.
- [ ] A write-disjoint wave ran three specs with no collision.
- [ ] `taskspec metrics` was read at `06` after finding nothing at `00`.
- [ ] `Revenue` is still unresolved and `daily-grain-decision` still refuses.
- [ ] The room filled the three commitment lines.

The planning source is [`../../plan/semana.md`](../../plan/semana.md);
the deck is [`../../presentation/d4.html`](../../presentation/d4.html). Day 3's
runbook ([`../d3/`](../d3/)) remains the format precedent.
