# Day 3 — The Spec: The Unit of Work

Build document for night 3 of Semana Engenharia Agêntica. Written 2026-08-12,
after Day 2 executed end to end. The planning source is
[`semana.md`](semana.md) §14, module three: *specification and decomposition —
intent, acceptance evidence, atomic work → reviewable specification and task
graph.*

## The question carried through the night

> The plan says ten items. Which one can I hand to an agent tonight — and how
> will I know it is done without asking you?

Day 1 asked what is true. Day 2 asked what the agent may do. Tonight asks what
"done" means, in a form a machine can answer.

## Storytelling continuity

| Night | Villain | Hero | Durable result |
| --- | --- | --- | --- |
| Day 1 | the weak prompt | evidence and ontology | three specs |
| Day 2 | the unbounded agent | written authority | contract, roles, two plans |
| **Day 3** | **the plausible plan item** | **the atomic task spec** | **a task graph and one executed packet** |

The Day 3 villain is deliberately subtler than Day 2's. Nobody in the room will
call `4-plan-transform.md` item 7 a bad plan item — it names its evidence, it
cites a real number, it marks its blocked grain. It is still not work: three
engineers would build it three different ways and all three would claim done.
That gap is the night.

The invariant closes the night unchanged: the agent performs bounded work,
evidence supports claims, humans keep the decisions the system cannot
legitimately make.

## Inherited inventory — what Day 3 starts from

```text
storage/specs/1-context.md          Day 1 — read-only
storage/specs/2-ontology.md         Day 1 — read-only · Revenue unresolved, D1–D4
storage/specs/3-technical-brief.md  Day 1 — read-only
storage/specs/4-plan-transform.md   Day 2 — TONIGHT'S RAW MATERIAL, 10 items, 3 BLOCKED
storage/specs/5-plan-serve.md       Day 2 — read-only tonight
AGENTS.md                           Day 2 — architect + developer, committed 3858c8c
dbt/models/staging/                 Day 2 — stg_orders.sql + _raw_sources.yml, committed
```

New tonight: `storage/tasks/` (the task graph) and one more staging model built
from a packet rather than from a plan line.

## The programme — eight movements

Same rhythm as Days 1 and 2: deck explains, repository tests, evidence decides.
Break after movement 03, contract left on the projector.

| # | Time | Movement | Live | Deck cue |
| ---: | --- | --- | --- | --- |
| 00 | 20:00 | Turn three — the unit of work | deck only | plan → spec → executed packet |
| 01 | 20:12 | The plan is not the work | `00` · `01` | one item, three builds |
| 02 | 20:35 | Anatomy of a Tasks Pack | `02` | seven fields, one objective |
| 03 | 21:00 | Two halves of done — BDD and evals | `03` | humans read Gherkin, machines run bash |
| — | 21:20 | **Break** | — | the Tasks Pack stays on screen |
| 04 | 21:30 | Decomposition — item 7 becomes a graph | `04` | lookup table plus per-task specs |
| 05 | 21:55 | The ready set — dependencies and order | `05` | wide and shallow beats narrow and deep |
| 06 | 22:20 | One packet, one iteration, one commit | `06` | fresh context, exit check, stop |
| 07 | 22:50 | The boundary survives decomposition | `07` | Revenue cannot become a task |

## Deck acts — `presentation/d3.html`

The deck mirrors `d2.html`'s design system exactly — same CSS, same act rail,
same slide grammar. Day 3's signature accent is **purple** (Day 2 was gold).
OPENING and ACT 0 are **built and render-verified** at 1600×900; the remaining
acts are specified below so any engine can build them on top.

### Slide inventory — built (9 slides)

| # | Act | data-act-name | Accent | Content |
| ---: | --- | --- | --- | --- |
| 1 | OPENING | The Spec | purple | title, four rails (Intent · Behaviour · Evals · Graph), Engineering Lead pullquote, contract strip |
| 2 | OPENING | What survived the night | green | two-col: copy + tag chips + callout left; `flow` manifest right (D1 specs → D2 rails → D2 plan → tonight, `is-end` glow) |
| 3 | OPENING | The programme | purple | `prog-head` + `rail` weight bar + prow rows, Topic rows 02 · 03, `prog-foot` |
| 4 | ACT 0 | Turn three | purple | divider, d2-S04 grammar: act-num + two-tone h2 + tag chips left; `flow` of four claims right (reality → name → economics → tonight) |
| 5 | ACT 0 | The first ring, again | purple | `rings-layout` SVG progress map — six rings, Prompt/Spec hot, Harness earned solid, Loop/Eval dashed |
| 6 | ACT 0 | Spec = Behaviour + Proof | purple | `rings-layout` SVG equation — Tasks Pack enclosure, four quadrant gates (INTENT · BEHAVIOUR · PROOF · GRAPH), spinning packet loop, Packet core |
| 7 | ACT 0 | The spec, in code | purple | d2-S07 grammar: 1fr auto 1fr grid, red-bordered "mentioned" code vs green-bordered "specified" code, `kick` labels, centered callout |
| 8 | ACT 0 | Last night's proof, tonight's gap | gold | d2-S08 grammar: pullquote ("Is this what you wanted?") left; four `fl-node` stack + gold callout right |
| 9 | ACT 0 | The WHY, in numbers | purple | `proof-cell` ×3 with `--pc` borders + caveat lines (3:1 · 4 · 0), `market-meaning` closing line |

Note for engines: the "Three nights, three villains" rmgrid concept was replaced
by the `flow`-based divider (slide 4) during the look-and-feel alignment pass —
the villain escalation now lives in slide 4's left column and the divider flow.

### Acts to build (map to movements and checkpoints)

Follow d2.html's per-act shape: divider with `act-num` → concept slide(s) →
go-live slide naming its `live/d3/` file → act close. Every go-live slide
carries `[Sources]` + talk track in a hidden `speaker-notes` aside.

| Act | Accent | Movement | Checkpoints | Slides (suggested) |
| --- | --- | --- | --- | --- |
| ACT 1 | green | 01 · The plan is not the work | `00` · `01` | divider 01 → "GO LIVE · The inheritance" (five specs, dbt-check, staging present from D2) → "Go live · three builds" (item 7 ×3 fresh sessions, divergence circled, nothing executes) → act close: "mentioned, not specified" |
| ACT 2 | accent | 02 · Anatomy of a Tasks Pack | `02` | divider 02 → anatomy slide (the seven fields, one per row, reader column) → "Go live · write T-001 by hand" (the felt cost — 15–20 min, do not rush) → skill card S1 |
| ACT 3 | gold | 03 · Two halves of done | `03` | divider 03 → "humans read Gherkin, machines run bash" (scenario above, derived eval below, same behaviour) → "Go live · run the eval" (bash returns 0 on screen) → **BREAK slide** — the Tasks Pack stays on the projector |
| ACT 4 | purple | 04 · Item 7 becomes a graph | `04` | divider 04 → two-layer index concept (lean `tasks.md` + one spec per packet; wide and shallow beats narrow and deep) → "GO LIVE · Decompose" (architect cuts 4–6 packets, index shown) → **giveaway slide** — Tasks Pack template, MIT, same pattern as Day 2's BriefSpec slide |
| ACT 5 | cyan | 05 · The ready set | `05` | divider 05 → dependency/order concept (ready set = unblocked ∩ highest priority) → "Go live · name the ready set" (graph on screen, order justified from `depends_on` alone) |
| ACT 6 | green | 06 · One packet, one iteration | `06` | divider 06 → trajectory slide (fresh session, files only, exit check, stop) → "GO LIVE · Execute one packet" (exit check returns 0 + item-10 refusal still holds — both on one screen) → "same pack, any engine" |
| CLOSE | gold | 07 · Turn three closes | `07` | "Turn three" ledger (built / withheld / tomorrow: Day 4 measures) → **Bootcamp slide** (one slide, after the gift, priced against the felt cost) → "The invariant" |

### Rules for any engine building on top

- Use ONLY classes already defined in the deck's `<style>` block — no new CSS.
  Verify with: every `class="…"` token must appear as a `.selector` in the file.
- Known engine mistakes from the d2 build round: invented metrics, wrong CSS
  var (`--pc` vs `--pk` — panels use `--pk`, programme rows use `--pc`),
  long text inside nowrap `.seam-t`, deleted `-->` comment closers.
- Numbers must be real: item 7's text is quoted verbatim from
  `4-plan-transform.md`; R$ figures come from `storage/specs/`; never invent.
- Every act's go-live slide names its `live/d3/` checkpoint file explicitly.
- Slides must fit 1600×900: content height ≤ ~850px inside the section padding.
- The act rail (`data-act` / `data-act-name`) drives the HUD — keep both on
  every section. Accents come from the ACCENT map: accent, cyan, purple, gold,
  green, red.
- Revenue stays unresolved. Item 10 is refused at ACT 6, never built. The
  refusal is a success state.
- Language: deck copy and this document are English; live prompts and any
  text quoted from `storage/specs/` or the session recordings stay in
  Portuguese, verbatim. Never translate a quoted prompt, plan item, or
  transcript line — the deck already follows this (e.g. the agent's refusal
  quote on slide 8).

## Checkpoint sequence — `live/d3/`

Build these eight files today, in the Day 1/Day 2 format: Session · Why this
step · Structure (mermaid) · Do live · Show the evidence · Gate · Recovery.

| Step | Session | Demo evidence | Durable result |
| ---: | --- | --- | --- |
| `00-inheritance.md` | no agent | five specs, rails intact, `dbt-check` PASS | baseline |
| `01-plausible-plan.md` | **NEW A**, disposable | three divergent builds of item 7 | none — discarded |
| `02-tasks-pack.md` | **NEW B** | one Tasks Pack, seven fields, human-edited | `storage/tasks/T-001.md` |
| `03-bdd-and-evals.md` | continue B | Gherkin scenario + runnable bash eval | evals inside `T-001` |
| `04-decompose.md` | continue B as architect | `tasks.md` index + 4–6 packets | `storage/tasks/` graph |
| `05-ready-set.md` | continue B | dependency graph, ready packets named | `tasks.md` ordering |
| `06-execute-one.md` | **NEW C**, developer | exit check green, one commit | second staging model |
| `07-reflection.md` | no agent | three commitment lines | team learning |

Session discipline is unchanged: A is the villain and is discarded, B carries
specification work, C is a fresh developer that receives only files.

### 01 — the villain, concretely

Paste item 7 verbatim as if it were a ticket, three times, into three fresh
contexts (or the same context reset). Say nothing else.

**The prompt below is in Portuguese by design — do not translate it.** Live
prompts across `live/d1/` and `live/d2/` are delivered in PT-BR (the room's
language), and the inner quote is item 7 verbatim from `4-plan-transform.md`
— translating it would break the premise that the agent receives exactly what
the plan says.

```text
Implemente o item 7 do plano de transformação:

"mart_daily_gross_ordered — soma por ordered_at, pedidos não cancelados;
grão = dia calendário UTC, rotulado como janela técnica"

Apresente apenas o seu plano em no máximo 6 linhas. Não execute.
```

English gloss, for reference only: *Implement item 7 of the transform plan:
"mart_daily_gross_ordered — sum by ordered_at, non-cancelled orders; grain =
UTC calendar day, labelled as a technical window". Present only your plan, 6
numbered lines maximum. Do not execute yet.*

Expect divergence on: which statuses count as "não cancelados" (non-cancelled), whether the
mart reads `stg_orders` or `int_orders_payments_reconciled`, whether the
technical-window label is a column, a model name, or a comment. Circle the
three. The line that lands:

> Every one of these is defensible. That is the problem. A plan item that
> permits three builds has not been specified — it has been mentioned.

### 06 — the payoff

Session C receives only `storage/tasks/T-00N.md` and `AGENTS.md`. No plan, no
transcript, no chat memory. It builds, runs the exit check, and stops. Then run
the exit check yourself in the terminal so the room sees the same `0` the agent
saw.

## The Tasks Pack — the seven fields

This is the night's teaching artifact and the thing to put on one slide.

| # | Field | What it holds | Who reads it |
| ---: | --- | --- | --- |
| 1 | **Intent** | one sentence, no "and" — the single objective | human |
| 2 | **PRD** | goal, lean context, the files to inspect and change | human + agent |
| 3 | **BDD** | Given / When / Then scenarios — behaviour in domain language | human first |
| 4 | **Evals** | 3+ runnable bash functions, terminal and idempotent | machine |
| 5 | **Exit criteria** | one command that returns 0 only when every eval passes | machine |
| 6 | **Cards** | the validation card — retry policy, iteration budget, agent contract | loop |
| 7 | **Related items** | `depends_on`, `touches_paths`, `do_not_touch`, soft links | graph |

Fields 1, 2, 3 are written by a human or reviewed by one. Fields 4, 5, 6 are
what let the agent answer "am I done?" without asking. Field 7 is what lets a
hundred packets be ordered without a project manager.

### The rule that makes a packet atomic

One objective with no "and". One area of the codebase. Verifiable by the steps
it already contains. Ends in a single clean commit. If the title needs "and" to
be honest, it is two packets.

## Assessment — does the Tasks Pack match where atomic tasks are going?

Researched 2026-08-12 with Tavily, Exa, and Firecrawl. Verdict: **six of the
seven fields are industry-convergent, one is a genuine gap, and one needs an
upgrade.** Evidence per field:

| Field | Status | External backing |
| --- | --- | --- |
| Intent | aligned | Spec Kit's *specify* phase; Ralph Loop's "one objective, split on the *and*" |
| PRD | aligned | Ralph Loop: "the PRD is the contract for the whole project, a task packet is the contract for one iteration" |
| BDD | **gap in v1** | arXiv 2602.00180: a feature was "done" only when all Gherkin scenarios passed; Intent Integrity Kit generates `.feature` files from a spec's Given/When/Then; Safeword routes any 3+ file change to a BDD track with `test-definitions.md` |
| Evals | aligned | Eval-driven development; Ralph Loop's test — "can a machine return yes or no without your opinion?" |
| Exit criteria | aligned | Spec Kit checkpoints; Ralph's `passes` flag flipping only after verification |
| Cards | aligned, ahead | Closest external analogue is Ralph's `passes` + iteration cap and TrueFoundry's `agent.eval_gate` / `agent.eval_result` telemetry fields. The validation card generalises both |
| Related items | **upgrade needed** | Ralph splits a lean `tasks.json` lookup table from per-task specs, and advises "wide and shallow beats narrow and deep". Task-Spec v1 has `depends_on` but no index layer |

### The one real gap: BDD

`~/.claude/skills/task-spec.v1.bak.*/templates/task-spec.md.tpl` has Why, Goal,
Context, Success Criteria, Validation Card, Exit Check, Anti-Patterns,
Do-Not-Touch, Open Questions. There is no Given/When/Then anywhere. Every eval
is bash, which is correct for the machine and wrong for the room: a stakeholder
cannot review `[[ $(dbt parse) ]]`, and Finance cannot confirm a behaviour they
cannot read.

Adding BDD is not ceremony. It is the field that lets the human who owns the
decision approve the behaviour before an agent encodes it. In TransactCo terms:

```gherkin
Scenario: gross ordered excludes cancelled orders
  Given the raw orders table with six distinct statuses
  When mart_daily_gross_ordered aggregates by ordered_at
  Then orders with status 'cancelled' are excluded
  And the result is labelled a technical window, never "Revenue"
```

That scenario is readable by Finance and mechanically translatable into the
bash eval underneath it. Write the BDD first, derive the eval, and the eval
stops being an assertion someone invented.

### The upgrade: a two-layer index

Add `storage/tasks/tasks.md` as a lean index — id, title, status, spec path,
`depends_on` — with the detail in one file per packet. Reason: an agent scanning
a hundred full specs to choose its next unit burns the context it needs to do
the work. The index is what makes the graph scale, and it is what movement 05
demonstrates.

## Why atomic tasks, for frontier-agent teams

Read literally, the argument is not a process preference — it is a context
argument, which is why it holds for the teams building the agents as much as for
teams using them.

An agent edits files inside a finite context window. Hand it a whole plan and
one of two failures follows: a sprawling diff nobody can review, or context rot
— it contradicts at hour two a decision it made at hour one. The fix is
structural, not motivational: never ask the agent to hold the project in its
head. One packet per iteration, fresh context each time, and the filesystem
carrying memory between passes instead of a chat history.

That is why the frontier labs' own tooling converged on the same four phases —
specify, plan, tasks, implement — across GitHub Spec Kit, AWS Kiro, and Tessl,
and why Thoughtworks' ladder (spec-first → spec-anchored → spec-as-source)
describes ambition rather than disagreement. The unit of work shrank because
the context window is finite. Everything else follows.

Say it once, in the room, as the reason the night exists:

> A plan is how humans agree. A packet is how an agent finishes. The window is
> finite, so the unit has to be small enough to close inside it.

## Bootcamp — designed as generosity, then judgment

Same discipline that worked on Day 2: make the room feel a cost, then price it
in one line, never a pitch.

**The felt cost (movement 02–03).** Write `T-001` by hand, on screen. All seven
fields, including a Gherkin scenario and three bash evals that actually run.
This takes fifteen to twenty minutes and it should feel long. Do not rush it.
The room must experience that the hard part is not typing — it is deciding what
"done" means precisely enough that a machine can check it.

**The giveaway (movement 04).** Give the Tasks Pack template away, free and
MIT, exactly as BriefSpec was given on Day 2. It generates the seven-field
skeleton and the index. Say plainly what it does not do: it cannot size a
packet, cannot tell you whether an eval is genuinely terminal, and cannot write
a scenario Finance would sign.

**The offer (after movement 07, three minutes).** One slide. The structure is
free; the judgment is the Bootcamp — a library of evals that hold under real
data, decomposition review, and the loop that runs a hundred packets without a
human in each one. Price it against the twenty minutes they just watched,
multiplied by a real backlog. Then stop talking and take questions.

Sequence matters: give before you ask. Day 2 proved the room accepts the hook
when it arrives after a gift and lasts one sentence.

## Today's build order

1. `live/d3/README.md` — sequence table, output budgets, completion gate.
2. `live/d3/00-inheritance.md` … `07-reflection.md` — eight checkpoints.
3. `plan/` decision: add BDD to the Tasks Pack template and ship the index layer.
4. `presentation/d3.html` — **OPENING + ACT 0 built and render-verified**
   (9 slides, 1600×900, no invented classes). Remaining: ACT 1 → CLOSE per the
   act map above — buildable act by act, by any engine, on top of the existing
   file.
5. Rehearse `06-execute-one.md` end to end, then reset the artifacts it creates.
6. Commit `storage/specs/4-plan-transform.md` and `5-plan-serve.md` — see the
   blocker below.

## Blocker to clear before building

`.gitignore:17` ignores `storage/specs/*.md`. Day 2's two plans exist on disk
and are **not in git**. They are the only input to tonight's decomposition, and
they are one `make bootstrap` away from being gone. Decide today:

- carve an exception for `4-plan-transform.md` and `5-plan-serve.md`, or
- copy them under a tracked path that Day 3 reads from.

Either is fine. Doing neither means Day 3 has no raw material if the working
copy is lost.

## Completion gate for the night

- [ ] The inherited plan was shown intact, including its BLOCKED rows.
- [ ] One plan item produced three divergent builds, and nothing executed.
- [ ] A Tasks Pack was written by hand with all seven fields present.
- [ ] A Gherkin scenario and its derived bash eval were both shown running.
- [ ] Item 7 decomposed into packets with an index and a dependency graph.
- [ ] The ready set was named before any packet was worked.
- [ ] A fresh developer session executed one packet from files alone and its
      exit check returned 0.
- [ ] Item 10 was requested and refused — Revenue still cannot become a task.
- [ ] The room wrote three commitment lines.

## Sources

- Ralph Loop, *Breaking a PRD Into Atomic Agent Tasks* (2026-04-17) —
  https://ralphloop.sh/blog/break-prd-into-agent-tasks/
- Böckeler, *Understanding Spec-Driven Development: Kiro, spec-kit, Tessl* —
  https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- *Spec-Driven Development: From Code to Contract in the Age of AI Coding
  Assistants*, arXiv 2602.00180 — https://arxiv.org/html/2602.00180v1
- GitHub, *Spec-driven development with AI* —
  https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit
- Intent Integrity Kit — https://github.com/intent-integrity-chain/kit
- Safeword, BDD routing by change size — https://github.com/ArcadeAI/safeword
- TrueFoundry, *Spec-Driven Development for AI Agents: Governing Specs* —
  https://www.truefoundry.com/blog/spec-driven-development-ai-agents
- Osmani, *How to write a good spec for AI agents* —
  https://addyosmani.com/blog/good-spec/
