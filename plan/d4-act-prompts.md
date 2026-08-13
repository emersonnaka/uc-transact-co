# Day 4 — The Loop · locked agenda and per-act dispatch prompts

Written 2026-08-13, after Day 3 executed. This file exists to be **split**: each
act below is a prompt you hand to a different engine, in parallel, with no shared
context. Each returns one `presentation/d4-act-<N>.html`, and they merge into
`presentation/d4.html`.

Two dispatch modes, and the difference matters:

- **Paste mode** — a chat window with no tools. Send §Shared contract +
  §Canonical facts + one act block. Everything the engine needs is inline.
- **Agent mode** — an engine with a terminal, file access and MCP research tools.
  Same three sections, plus the operating instruction in §Agent mode, which makes
  it read the repository, **verify state by running commands**, and ground its
  external claims. Use this when you have it; it is stronger.

## How to dispatch

1. Send **§Shared contract** + **§Canonical facts** + **one act prompt** to each
   engine. Send nothing else. No engine needs to read this repository.
2. Each returns one file: `presentation/d4-act-<N>.html`, self-contained and
   openable on its own.
3. Merge in act order, then measure. Merge is mechanical: lift each act's
   `<style data-act="N">` block and its `<section class="slide">` elements.

**The lesson from Day 3 that shapes this file:** ACT 4 came back built on the
wrong data model because its prompt said *"read `plan/d3-agenda.md`"* and that
file had drifted. Two acts came back with the wrong slide count. So every fact an
engine needs is written **inline below**, and every prompt states its exact slide
count. Nothing points at a file that can change.

---

## Agent mode — when the engine has repo access and research tools

The dispatch above assumes a chat window you paste into. If instead you are giving
each act to an **agent** with a terminal, file access and MCP research tools, use
this mode. It is stronger, because the agent can verify facts instead of trusting
prose — including trusting mine.

Paste **§Shared contract** + **§Canonical facts** + **one act block** (its brief
*and* its research brief), then prepend this operating instruction:

```text
You are building ONE act of a slide deck, working alone. Four phases, in order.
Do not skip phase 2.

PHASE 1 — READ. Read only these, and read them fully:
  plan/d4-act-prompts.md          your agenda and the act you own
  presentation/d3.html            LAST NIGHT'S DECK — your design reference.
                                  Match its grammar, density and tone exactly.
  live/d3/README.md               how a night is structured
  live/d3/0*.md                   the eight checkpoint runbooks, for voice
  skills/README.md                the three skills delivered so far
  AGENTS.md                       the agent roles and the ground rules

PHASE 2 — VERIFY BY RUNNING. Prose drifts; commands do not. Run these and treat
their output as the only authority on repository state. Where any prose in this
plan disagrees with them, the commands win and you say so in your reply:
  taskspec version
  taskspec ready
  taskspec ready --all
  taskspec lint
  taskspec metrics
  taskspec validate tasks/T-*.md
  taskspec dod tasks/T-*.md
  cat tasks/_state.yaml
  git log --oneline -12
  ls -la dbt/models/staging/
  make dbt-check
Record the exact output you will put on a slide. Never paraphrase a number.

PHASE 3 — GROUND. Use the research tools per your act's research brief. External
claims need a source and a date. See §Research grounding for the rules.

PHASE 4 — BUILD. Write exactly one file, presentation/d4-act-<N>.html, matching
the slide count in your act brief. Then self-check before replying:
  - slide count matches the brief exactly
  - every new CSS selector is .a<N>- prefixed, in one <style data-act="<N>"> block
  - every SVG id is a<N>-prefixed and appears in no reserved-id list
  - every slide has a .src line and a hidden speaker-notes aside
  - no number on any slide that you did not read from command output or cite
  - open the file and confirm nothing overflows at 1600x900

Reply with: the slide list, which slides are tightest on height, every command
output you used, every external source you cited, and anything in this plan you
found to be wrong.
```

### What to distrust

- **Any prose in this file that a command contradicts.** This plan was written
  2026-08-13; the repository moves. Phase 2 exists for exactly this.
- **`presentation/d3.html`'s content** — copy its *grammar*, never its claims. Its
  numbers belong to Day 3.
- **Anything about Day 4 you cannot run or cite.** If you want a figure that is
  neither in §Canonical facts nor in command output nor in a citation, draw the
  shape and label it `EXPECTED SHAPE — NOT LIVE OUTPUT`.

---

## Research grounding

Each tool has one job. Do not run all five on every act — that burns calls and
returns mush. Your act's research brief says which to use.

| Tool | Its one job |
| --- | --- |
| `mcp__tavily__tavily_search` | current state of practice; a fact with a date |
| `mcp__tavily__tavily_research` | one broad synthesis when an act needs a landscape, not a fact |
| `mcp__exa__web_search_exa` | describe the ideal page in a sentence; best for essays and primary write-ups |
| `mcp__exa__web_fetch_exa` | read the full page once a search gives you the URL |
| `mcp__firecrawl__firecrawl_search` with `categories:["research"]` | research-affiliated pages |
| `mcp__firecrawl__firecrawl_research_search_papers` | arXiv and scientific abstracts by topic |
| `mcp__firecrawl__firecrawl_research_read_paper` | pull the passage that actually supports your claim |
| `mcp__firecrawl__firecrawl_developer_search` | tool behaviour, CLI semantics, real issues and PRs |
| `mcp__context7__resolve-library-id` → `query-docs` | library documentation: dbt, DuckDB |
| `mcp__ref__ref_search_documentation` → `ref_read_url` | the same, when Context7 has no entry |

### The citation rule

Any claim that did not come from this repository is external, and external claims
carry their receipt **on the slide's `.src` line**: source, title, and date. Format:

```text
External: <source>, "<title>", <YYYY-MM> — <one-line what it supports>.
```

Three bans, and they matter more than coverage:

1. **No fabricated statistics.** If you cannot cite a number, do not put a number
   on the slide. A qualitative claim with a real source beats a precise-sounding
   invention.
2. **No single-source superlatives.** "The industry standard" needs more than one
   page. Prefer "reported by X in <month>" over "everyone now does".
3. **No stale framing as current.** Include the date. A 2023 claim presented as
   today's practice is the same failure this deck argues against.

If research returns nothing solid, say so in your reply and build the act on the
repository's own evidence. **An honest act with fewer external claims is better
than a padded one.** Days 1 to 3 carried very few external citations and were
stronger for it.

---

## The locked agenda

**Night name:** The Loop · **signature accent:** green · **43 slides**

Tonight lights the last two rings on the six-ring map — **Loop** and **Eval +
human gate**. Every previous night left them dim and said "waits for Day 4."
Completing the map is the spine.

**Carried question:** *Six specs are ready and nobody has run one. What happens
when no one is watching — and how do I know the green means anything?*

**Villain:** the eval that passes for the wrong reason. Day 1 was a weak prompt
(visible failure), Day 2 an unbounded agent (visible overreach), Day 3 a plausible
plan item (invisible ambiguity), Day 4 **invisible false confidence**.

| Act | Slides | Movement | Time | Subject |
| --- | ---: | ---: | --- | --- |
| OPENING | 3 | — | 20:00 | Title · what survived · the programme |
| ACT 0 | 6 | `00` | 20:00 | Turn four — the graph that has never moved |
| ACT 1 | 5 | `01` | 20:12 | Green that proves nothing (villain, discarded) |
| ACT 2 | 6 | `02` | 20:35 | An eval that can fail — mutation discrimination |
| ACT 3 | 5 | `03` | 21:00 | The holdout — the evaluator the executor cannot read |
| — | — | — | 21:20 | **Break** |
| ACT 4 | 7 | `04` + ✦ | 21:30 | The authorization chain, then giveaway → crank → Bootcamp handoff at 21:50 |
| ACT 5 | 4 | `05` | 22:00 | Waves — dispatching a write-disjoint frontier |
| ACT 6 | 4 | `06` | 22:20 | The unit of work becomes the unit of measurement |
| CLOSE | 3 | `07` | 22:50 | Turn four closes · six rings lit · the invariant |

---

## Shared contract

*Paste this section verbatim into every act prompt.*

You are building **one act** of a dark-themed, scroll-snap HTML slide deck for a
live 3-hour technical session. Return exactly one self-contained HTML file.

### Slide grammar

```html
<section class="slide" data-act="ACT N" data-act-name="Short name" data-accent="green">
  <div class="aurora aurora--green" aria-hidden="true"><b></b></div>
  <div class="wrap reveal" style="max-width:1700px;">
    <!-- content -->
    <div class="src">Provenance: where every number and quote came from.</div>
    <aside class="speaker-notes" hidden>[Sources]
…one line per source…
[/Sources]
Talk track: what the presenter says, in order, including what NOT to say.</aside>
  </div>
</section>
```

`data-accent` must be one of `accent cyan purple gold green red`. Every slide
carries a `.src` provenance line and a hidden `speaker-notes` aside.

### Design tokens (already defined — use, do not redefine)

```css
--bg:#08080a  --surface:#111114  --surface2:#19191e
--border:rgba(120,160,220,0.08)  --border-bright:rgba(120,160,220,0.18)
--rule:rgba(160,190,230,0.13)
--text:#eaedf2  --text-dim:#6e7a8c  --text-mute:#4d5666
--accent:#4a9eff  --cyan:#22d3ee  --purple:#a78bfa
--gold:#d4af37  --green:#3fb950  --red:#f85149  --silver:#b0bec5
--font-display:'Instrument Serif'  --font-editorial:'Newsreader'
--font-body:'DM Sans'  --font-mono:'Fira Code'
```

### House classes you may reuse freely

`wrap reveal slide src speaker-notes tag eyebrow kick h2 display lede note
callout co-k co-b panel panel-k cols code grad grad-green grad-gold grad-cyan
grad-purple flow fl-node fl-k fl-name fl-note fl-arrow golive gl-grid gl-k gl-v
gl-top gl-title gl-file next-hook hook-n hook-copy proof-cell proof-num
proof-label proof-caveat rings-layout rings-copy rings-viz ring-decision
skillcard sk-top sk-id sk-title sk-sub sk-grid sk-cols pullquote pq-text pq-who
pq-attr prog-head programme prow prow-num prow-time prow-name prow-live rail
rail-seg rail-track title-grid title-rule title-sub fnd-label spine sp sp-dot
sp-head sp-n sp-name sp-job orbit orbit-ring orbit-core orbit-node node-shell
node-n node-name node-note ts-preview ts-ring ts-orbit ts-dot st st-evi st-inf
st-unr act-num turn-head turn-number vs vs-a vs-b vs-k vs-v io-block io-k io-v`

Syntax-highlight spans inside `.code`: `.c` comment, `.k` keyword, `.s` string,
`.n` name, `.g` green, `.r` red, `.w` white.

### Namespacing — non-negotiable, this is how parallel acts merge

- New CSS goes in **one** `<style data-act="N">` block, every selector prefixed
  `.aN-` (act 4 → `.a4-`). Never edit or restate house CSS.
- Every SVG `id` prefixed `aN` (e.g. `id="a4Glow"`). **These ids are already
  taken — do not reuse any of them:**
  `a1-fanA a1-fanB a1-fanC a1-glow a1-halo a1-qglow a2lA1 a2lA2 a2lA3 a2lA4 a2lA5
  a2lCore a2lGlow a2lGold a2lRet a2zBind a2zGlow a3-mCy a3-mGo a3-mRd a4-mCut
  a4-mDep a4-mPtr a4-mRef a4-pGlow a4-pGrad a4bGlow a4bWave a5ArrG a5ArrR
  a5DoneFill a5Glow a5ReadyFill a5RedFade a5RedGlow a5WaitFill a6-core
  a6-coreGlow a6-eg a6-eng a6-glow a6-ng a6-og a6-outR a6-pkt a6-r1 a6-r2 coreG
  coreGlow dcAct dcBar eqCore eqCoreGlow eqGlow g1 g2 g3 g4 g5 g6 hotGlow n total
  tracker`
- No JavaScript. No external assets. Inline SVG only.

### The measurement contract

Every slide's content must fit **1600×900** with no vertical overflow. Slide
padding defaults are generous; for a dense slide set
`style="padding-top:clamp(9px,1.5vh,20px);padding-bottom:clamp(9px,1.5vh,20px);"`
on the `<section>`. Prefer cutting words over shrinking type below the clamps
given. State in your reply which slides you consider tightest.

### Hard rules

1. **Build only your act.** Do not add a title slide, a programme slide, a close,
   or another act's content. Wrong slide counts cost a merge pass.
2. **Exact slide count.** Your prompt states it. Deliver that number.
3. Every number, command and quotation must be **traceable** and appear in `.src`.
   Invent no metrics. If you need a figure that is not in §Canonical facts, show
   the shape and label it `EXPECTED SHAPE — NOT LIVE OUTPUT`.
4. **`Revenue` is unresolved and owned by Finance.** No slide may define it,
   compute it, or imply an agent may choose its meaning.
5. Prompts shown on screen are **PT-BR** (the room's language). All other deck
   copy is **English**.
6. Plain language. Short sentences. No invented vocabulary, no metaphor standing
   in for a mechanism. The operator reads English as a second language.

---

## Canonical facts

*Paste this section verbatim into every act prompt. Everything an engine needs is
here; no engine should read a file in the repository.*

### The case

**TransactCo** — a brownfield commerce system whose numbers must earn trust. The
week's question: *how much Revenue did TransactCo make yesterday, and why should
the CFO trust that number?* The arithmetic is easy; the trust problem is not.
`Revenue` is formally **unresolved**, owner **Finance**.

### The six-ring map (recurring figure, one ring lights per night)

Outermost to innermost: **Graph** (earned Day 1) · **Eval + human gate** (lights
tonight) · **Loop** (lights tonight) · **Harness** (earned Day 2) · **Context**
(earned Day 1) · **Prompt/Spec** (earned Day 3) · **Model** at the core.
Tonight is the first night **two** rings light, and it completes the map.

### What the four nights are called

Day 1 **The Foundations** · Day 2 **The Harness** · Day 3 **The Task** ·
Day 4 **The Loop**.

### What Day 3 left on disk (verified 2026-08-13)

- **Six Task-Specs** in `tasks/`, all passing `taskspec validate`, all reporting
  `DOD=COMPLETE`. Ids: `T-20260812-daily-gross-ordered` (hand-written),
  `T-20260812-raw-payments-source`, `T-20260812-stg-orders-payments-join`,
  `T-20260812-stg-returns-refunds-mirror`,
  `T-20260812-stg-daily-captured-payments`, `T-20260812-daily-grain-decision`.
- `tasks/_state.yaml`: `total: 6 · ready: 6 · in_progress: 0 · blocked: 0 ·
  done: 0 · parked: 0`.
- `taskspec ready` prints a **2-wide frontier** (`daily-gross-ordered`,
  `raw-payments-source`) and reports `(4 ready spec(s) hidden — blocked by an
  unmet depends_on)`.
- `taskspec lint` → `LINT=OK`, one write-disjoint group under `dbt/models`.
- **`signed_off: false` on every spec. Nothing was ever gated or accepted.**
- **`done: 0`. Not one spec has been executed.** No second staging model exists;
  `dbt/models/staging/` holds only `_raw_sources.yml` and `stg_orders.sql`.
- **`taskspec metrics` prints `No metrics file found at tasks/_metrics.jsonl`.**
- `make dbt-check` passes. `Revenue` remains unresolved.

### The tool

**Task-Spec v3.7.0**, MIT, `github.com/luanmorenommaciel/task-spec`. Given away
free on Day 3. Six zones: 1 Intent · 2 Behavior · 3 Contract (The Moat) ·
4 Guardrails · 5 Operations · 6 Reversal & Runtime. Zones 1–2 are authored and
signed by a human; zone 3 is the only executable zone.

**The traceability rule:** every `B-N` is verified by ≥1 eval carrying
`verifies: [B-N]`; every eval names ≥1 behaviour. Neither may dangle.

**The seal:** `signed_off*` is bound by `hmac-sha256-v2`. Only `gate --stamp`
writes it; only `accept --stamp` writes `accepted*`. Change one character of the
body after sign-off and the seal breaks.

**Commands verified present in v3.7.0** (do not invent others):
`version init new plan batch migrate validate dod gate handoff run accept
author-doctor holdout receipt eval-audit identity evidence bridge mcp ready lint
transition rebuild-state archive backup metrics agent-context conformance
executor doctor`

Exact usage strings, verified:

```text
taskspec gate [--stamp] [--require-tier1] <spec>
taskspec handoff <spec> --backend <token>
taskspec run [--ci] <spec>
taskspec accept [--stamp] [--no-blast-radius] [--accepted-by NAME] <spec>
taskspec eval-audit <spec> --baseline <ref> [--mutations N] [--report PATH]
taskspec holdout {seal,verify,run} …
taskspec transition <id> <status> [reason]
taskspec metrics
```

Gate tokens: `DOD=COMPLETE`, `TIER=1`, `ACCEPTED=1`.

### The multi-engine boundary (state it honestly if an act touches it)

`taskspec evidence` supports nine families (OpenAI, Anthropic, Google, xAI,
DeepSeek, Kimi, MiniMax, Qwen, GLM). The checked-in release matrix
`evidence/3.7/engine-matrix.json` has **every family disabled with
`model_id: TO_RECORD`** — no real multi-engine result exists upstream. Compare
terminal outcome, never writing style. An engine that could not run is
`unavailable`, **never** a pass.

### Numbers that are real (use these, invent nothing)

- Candidate 1 — gross ordered: **R$ 1,403,044.31** across **868** orders.
- Candidate 2 — captured payments: **R$ 980,870.44** across **632** payments.
- Candidate 3 — delivered: **R$ 0.00** (the schema carries no delivery clock).
- The spread between candidates 1 and 2: **R$ 422,173.87**.
- Day 2's plan has **10 items**; items 9 and 10 are BLOCKED on Finance.
- Day 3 hand-wrote **one** spec in **15–20 minutes**; the tool then generated
  five in seconds.

---

## OPENING — 3 slides

Accent `green`, slide 2 `gold`. `data-act="OPENING"`. Deliver
`presentation/d4-act-opening.html`.

The room arrives. Three slides, no teaching yet.

1. **Title.** `title-grid` grammar. Eyebrow reads
   `Semana Engenharia Agêntica · Day 4 of 5 · 20:00–23:00 BRT`. A gold-green
   `title-rule`, then `<h1 class="display">The Loop</h1>`, then a `title-sub`
   paragraph: last night produced a graph of six provable units and ran none of
   them; tonight it runs, and every run leaves a receipt. On the right, a `spine`
   of the night's four rails — **Dispatch · Proof · Receipt · Measurement** — each
   with a one-line job. Close with a presenter strip and three chips: what the
   agent may access, what counts as evidence, what tonight outputs.
2. **What survived the night.** Accent `gold`. Two columns: copy plus tag chips on
   the left, a `flow` manifest on the right showing D1 specs → D2 rails → D3 task
   graph → tonight, with the last node marked `is-end`. Name the inheritance
   exactly: six specs all `DOD=COMPLETE`, `done: 0`, `signed_off: false`,
   `taskspec metrics` finding no file. Land the line: *the graph is complete and
   has never moved.*
3. **The programme.** `prog-head` + a `rail` weight bar + `prow` rows for eight
   movements. Use these rows verbatim:
   `00 · 20:00 · Turn four — the graph that has never moved · deck only`;
   `01 · 20:12 · Green that proves nothing · ▶ 01`;
   `02 · 20:35 · An eval that can fail · Topic · ▶ 02`;
   `03 · 21:00 · The holdout · Topic · ▶ 03`;
   `— · 21:20 · Break`;
   `04 · 21:30 · The authorization chain · ▶ 04`;
   `✦ · 21:50 · Giveaway → crank → Bootcamp · 5 min`;
   `05 · 22:00 · Waves · ▶ 05`;
   `06 · 22:20 · The unit of measurement · ▶ 06`;
   `07 · 22:50 · Turn four closes · ▶ 07`.
   Foot line: every ▶ is a numbered file in `live/d4/`.

### Research brief — OPENING

**None.** Repository state and the programme only.

---

## ACT 0 — Turn four · the graph that has never moved · 6 slides

Accent `green`, one slide `gold`. `data-act="ACT 0"`. Deliver
`presentation/d4-act-0.html`.

Open the night. The room inherits a complete, validated, entirely unmoved graph.

1. **Divider — "Turn four."** Act-num treatment, two-tone headline, three or four
   tag chips, and a `flow` of claims on the right: *the graph exists · nothing has
   run · nothing is signed · green is not yet evidence*.
2. **The last two rings.** The six-ring `rings-layout` figure. This is the first
   night **two** rings light — Loop and Eval + human gate — and the map completes.
   Earned rings solid; tonight's two hot.
3. **The inheritance, in numbers.** `proof-cell` ×3 with caveat lines:
   **6** specs all `DOD=COMPLETE` · **0** executed · **0** signed.
4. **`taskspec metrics` → "No metrics file found."** A terminal-shaped slide whose
   whole payload is that one line of output. The unit of work exists; the unit of
   measurement does not yet.
5. **The night's equation.** `Loop = dispatch + proof + receipt`. Name what each
   term means and who owns it. Accent `gold` on this one.
6. **The villain, named but not yet shown.** *An eval that cannot fail is not a
   gate — it is a decoration.* Hand off to Act 1 with a `next-hook`.

### Research brief — ACT 0

**None.** This act is entirely repository state. Do phase 2 thoroughly and skip
phase 3. Every number on these six slides comes from command output.

---

## ACT 1 — Green that proves nothing · 5 slides

Accent `red` for the villain slides, `green` for the divider. `data-act="ACT 1"`.
Deliver `presentation/d4-act-1.html`.

The villain, performed live and then discarded. This is the honest failure the
whole night is built on.

1. **Divider — "Green that proves nothing."**
2. **Three ways an eval lies.** A three-column comparison: an eval that tests
   nothing (`true`), an eval that tests the wrong artifact, an eval that passes
   because the file merely exists. Each looks green.
3. **GO LIVE — run a spec whose eval cannot fail.** `golive` grammar: Session,
   Action, Evidence, Gate, "come back when". The PT-BR prompt goes on screen.
   Evidence: exit 0, and nothing built. Cite `live/d4/01-*.md`.
4. **The verdict.** `pullquote` treatment: the loop did exactly what it was told,
   and what it was told proved nothing. Name that the session is **discarded**.
5. **Act close.** *A passing test is a claim. Tonight we make it evidence.*
   `next-hook` to Act 2.

### Research brief — ACT 1

The claim to ground: **tests and evals routinely pass while proving nothing**, and
this is a documented failure mode rather than a rhetorical device.

- `firecrawl_research_search_papers` — "tests that pass without detecting faults",
  "assertion-free test smells", "LLM benchmark contamination false confidence".
- `tavily_search` — recent write-ups on agent evals that pass vacuously; get a
  date on anything you use.
- `exa` — "essay on why green test suites fail to catch regressions".

Two or three real citations is plenty. If the literature gives you a named smell
(assertion-free tests, tautological assertions), use the real name on the slide.

---

## ACT 2 — An eval that can fail · 6 slides

Accent `green`. `data-act="ACT 2"`. Deliver `presentation/d4-act-2.html`.

The night's first topic: mutation discrimination. An eval earns trust by failing
when the thing it guards is broken.

1. **Divider — "An eval that can fail."**
2. **The falsifiability rule.** The five eval-quality rules — deterministic,
   idempotent, cheap-before-expensive, explainable, **falsifiable** — with the
   fifth marked as the one everyone skips.
3. **Mutation discrimination, drawn.** An inline SVG: baseline → N deliberate
   mutations → each eval's verdict → a discrimination score. Show a caught
   mutation and a **survived** mutation, and say plainly that a survivor is a hole
   in the gate, not a passing grade.
4. **`taskspec eval-audit`, in code.** A `.code` block with the verified usage
   `taskspec eval-audit <spec> --baseline <ref> --mutations N --report PATH` and
   what each flag does.
5. **GO LIVE — audit one of Day 3's evals.** `golive` grammar. Break the model on
   purpose, watch the eval catch it, then restore. Cite `live/d4/02-*.md`.
6. **Skill card S1.** `skillcard` grammar: *Prove the eval before you trust it.*
   Skill · when to use · inputs · method · output · two gates.

### Research brief — ACT 2

The claim to ground: **mutation testing is the established way to prove a test can
fail**, and `taskspec eval-audit` applies that idea to agent evals.

- `firecrawl_research_search_papers` — "mutation testing effectiveness",
  "mutation score as test adequacy", then `research_read_paper` for the passage
  that supports your specific sentence.
- `firecrawl_developer_search` — how mutation testing is used in practice, and any
  known limits worth naming honestly (cost, equivalent mutants).
- `context7` or `ref` — dbt behaviour only if a slide shows real dbt output.

This is the act where a citation earns its place: the room is being asked to trust
a discipline, so name where the discipline comes from. Do **not** claim a mutation
score for this repository unless you ran `eval-audit` and read the number.

---

## ACT 3 — The holdout · 5 slides

Accent `cyan`. `data-act="ACT 3"`. Deliver `presentation/d4-act-3.html`.
End with the break slide.

The second topic: an evaluator the executor is not allowed to read.

1. **Divider — "The holdout."**
2. **Why a visible eval is a target.** An agent that can read its own grader can
   satisfy the grader instead of the goal. Draw the asymmetry: visible evals in
   the spec, sealed evals outside it.
3. **`seal → verify → run`.** The three-step lifecycle as a flow, with what each
   step emits (a sealed bundle, a verification receipt, a result). Verified usage:
   `taskspec holdout {seal,verify,run}`.
4. **GO LIVE — seal a holdout, then run it.** `golive` grammar. Evidence: the
   receipt, and that the executor never saw the bundle. Cite `live/d4/03-*.md`.
5. **BREAK slide.** Large, calm, one line on screen and the time the room returns.
   Say what stays on the projector during the break.

### Research brief — ACT 3

The claim to ground: **an evaluator the subject can read is a weaker evaluator** —
held-out sets, contamination, and Goodhart's law.

- `firecrawl_research_search_papers` — "benchmark contamination", "held-out
  evaluation leakage", "reward hacking specification gaming".
- `exa` — "essay on Goodhart's law in machine learning evaluation".
- `tavily_search` — a recent, dated example of a model or agent optimising the
  metric instead of the goal.

One well-chosen citation for Goodhart and one for contamination is enough. Keep
the slide about the mechanism; the citations belong in `.src`.

---

## ACT 4 — The chain, then the offer · 7 slides

Accent `green`, with the last three `gold`. `data-act="ACT 4"` for slides 1–4 and
`data-act="✦ BOOTCAMP"` for slide 7. Deliver `presentation/d4-act-4.html`.

**The night's peak, and the commercial beat sits inside it at 21:50 — never at the
close.** Slides 5–7 are the three-beat that worked on Day 3: giveaway, crank,
handoff. Do not add pricing to any slide; terms live in a separate deck.

1. **Divider — "The chain."**
2. **Four commands, four different authorities.** The authorization chain as a
   figure: `gate --stamp` (writes `signed_off`) → `handoff --backend` (emits a
   portable TaskHandoff) → `run --ci` (executes evals) → `accept --stamp` (writes
   `accepted`). Mark which step a human owns and which the machine owns.
3. **The seal, finally stamped.** Day 3 taught `hmac-sha256-v2` and never stamped
   one. Show a spec's frontmatter before and after `gate --stamp`, and the tokens
   `DOD=COMPLETE` / `TIER=1` / `ACCEPTED=1`.
4. **GO LIVE — one spec, end to end.** `golive` grammar, the full chain on
   `T-20260812-raw-payments-source`. Evidence: `signed_off: true`, exit 0, then
   the frontier recomputing. Cite `live/d4/04-*.md`.
5. **Beat 1 — the giveaway.** Tonight's skill, free and MIT, with a real install
   line. Say plainly what it cannot do.
6. **Beat 2 — the crank.** The loop consuming the graph in waves. **Unlike Day 3
   this is no longer pre-recorded** — the loop genuinely ran twenty minutes
   earlier. Say that difference out loud.
7. **Beat 3 — the Bootcamp handoff.** `data-act="✦ BOOTCAMP"`, accent `gold`,
   centred, sparse, `ts-preview` orbit behind it. A door, not a pitch: no price,
   no second CTA. It names the deck switch and says *five minutes, then straight
   back to the graph*.

### Research brief — ACT 4

**Minimal, and be careful.** The chain is verified repository mechanics — take it
from `taskspec gate/handoff/run/accept` output. Do **no** market research for the
commercial beat: no competitor claims, no ROI statistics, no urgency framing. The
only external fact permitted is the Bootcamp's own published dates and terms.

---

## ACT 5 — Waves · 4 slides

Accent `cyan`. `data-act="ACT 5"`. Deliver `presentation/d4-act-5.html`.

Concurrency that comes from the graph, not from a scheduler.

1. **Divider — "Waves."**
2. **Write-disjoint means safe together.** `taskspec lint` reports a concurrency
   partition: groups whose write surfaces do not overlap. Draw two waves — a
   2-wide frontier, a gate returning 0, then 3 in parallel. **This is the real
   shape of Day 3's graph, verified.**
3. **GO LIVE — dispatch the frontier.** `golive` grammar. Evidence: two specs
   accepted concurrently, no write collision, the frontier recomputed. Cite
   `live/d4/05-*.md`.
4. **Act close.** *Nobody scheduled that. The graph did.* `next-hook` to Act 6.

### Research brief — ACT 5

**Minimal.** The wave shape is measured, not researched — take it from
`taskspec ready` and `taskspec lint`. At most one citation on why write-disjoint
concurrency is the safe partition; skip it if nothing solid appears.

---

## ACT 6 — The unit of measurement · 4 slides

Accent `green`. `data-act="ACT 6"`. Deliver `presentation/d4-act-6.html`.

The sentence Day 3 promised, delivered as output.

1. **Divider — "The unit of work becomes the unit of measurement."**
2. **What a receipt carries.** `taskspec metrics` now has data where Act 0 found
   none: attempts, retries, durations, acceptance verdicts, per-spec. Draw the
   record, and mark which fields are measured versus declared.
3. **GO LIVE — read the metrics.** `golive` grammar. Put Act 0's *"No metrics file
   found"* beside tonight's populated log. That before/after is the act.
   Cite `live/d4/06-*.md`.
4. **What measurement does not buy.** It does not resolve `Revenue`. The
   `daily-grain-decision` hole is still blocked, still Finance's. Measuring work
   never earns the right to define it.

### Research brief — ACT 6

The claim to ground: **measuring agent work needs receipts, not vibes** — what the
field currently measures and what it admits it cannot.

- `tavily_research` — one synthesis on how teams currently measure agent-assisted
  engineering work in 2026, and what the reported limits are.
- `firecrawl_research_search_papers` — "measuring LLM agent task completion",
  "agent evaluation metrics reliability".
- `firecrawl_developer_search` — real telemetry fields other agent frameworks emit,
  to show `taskspec metrics` is not eccentric.

Careful here: this act is the one most likely to attract a fabricated productivity
statistic. If you cannot cite it with a date, do not state it. The strongest
version of this act uses **only** the metrics you actually read from
`taskspec metrics` plus one or two dated external claims.

---

## CLOSE — 3 slides

Accent `gold`. `data-act="CLOSE"`. Deliver `presentation/d4-act-close.html`.

1. **Turn four closes.** The flywheel `orbit` figure with four stations lit and
   Day 5 ahead. A `built / withheld / tomorrow` ledger, plus the three commitment
   lines the room writes rather than hears.
2. **Six rings, lit.** The recurring figure, complete for the first time all week.
   Every ring solid, the Model at the core, nothing dashed. Let it sit.
3. **The invariant.** Unchanged from Days 1–3, word for word: *the agent performs
   bounded work; evidence supports claims; humans keep the decisions the system
   cannot legitimately make.* One neutral Bootcamp line, and the Day 5 time.

### Research brief — CLOSE

**None.** The invariant is quoted verbatim from Days 1 to 3; do not rewrite it.

---

## Open decisions — settle these before dispatching

1. **Tonight's giveaway** (Act 4 beat 1). Day 3 gave Task-Spec. The natural
   candidate is the eval-audit and holdout discipline packaged as skill #4, but it
   needs a name and a real install line before Act 4 can be built honestly.
2. **Whether Day 3's specs get stamped tonight or beforehand.** If you stamp them
   before the session, Act 4 slide 3 loses its live moment and must be rewritten
   as a walkthrough.
3. **Day 5's name.** CLOSE slide 1 points at it. `The Factory` is the shape the
   week has been building toward.
