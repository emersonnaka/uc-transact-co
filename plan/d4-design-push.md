# Day 4 — design push · one prompt per act

`presentation/d4.html` is complete and correct. It is also **flat**: 4 of its 45
slides carry a figure and none carries a table. This file dispatches a redesign
pass, one act per engine, in parallel.

## The diagnosis that justifies the pass

| Act | Slides | Figures | Verdict |
| --- | --- | ---: | --- |
| OPENING | 1–3 | 0 | the programme is a list where it should be a timeline |
| ACT 0 | 4–10 | 2 | rings and wheel are good; 6, 8 and 10 are prose |
| ACT 1 | 11–15 | **0** | a whole villain act with nothing to look at |
| ACT 2 | 16–21 | 1 | the mutation figure exists but under-reaches |
| ACT 3 | 22–26 | **0** | a visibility argument with no visibility drawn |
| ACT 4 | 27–33 | **0** | **the night's peak, 7 slides, all text** |
| ACT 5 | 34–38 | **0** | slide 36 is *called* "Two waves, drawn" and draws nothing |
| ACT 6 | 39–42 | **0** | a measurement act that shows no measurements |
| CLOSE | 43–45 | 1 | six rings is right; the ledger is prose |

## The workflow — read this or you will destroy someone else's work

`d4.html` is **one file** and nine engines are working at once. Never edit it.

1. **Extract** your act's slides from `presentation/d4.html` into a new file
   `presentation/d4-act-<N>.html` — a complete, openable HTML document. Copy the
   `<head>`, the base `<style>`, and the deck script from `d4.html` so your file
   renders standalone. Copy your slides **byte-identical** to start.
2. **Redesign inside your file only.**
3. Return that file. The merge back into `d4.html` is done by one person, once.

**Never open `d4.html` for writing. Never touch another act's slides.**

## The bar

You are changing **how the information is seen**, not what it says.

- **Content is frozen.** Every claim, number, command, quotation, `.src` line and
  `speaker-notes` aside survives byte-identical unless you are moving it into a
  figure that says the same thing. If you think a fact is wrong, say so in your
  reply — do not silently fix it.
- **Every figure must carry information the prose cannot.** A diagram that
  restates a sentence is worse than the sentence: it costs space and adds nothing.
  If you cannot name what a figure reveals, cut it.
- **Prefer the honest shape.** Six specs in four states is a 6×4 grid. Two waves
  is a timeline. A before/after is two columns. Reach for the ordinary form that
  fits the data before you reach for something clever.
- **One idea per slide keeps its one figure.** Do not add a second chart to fill
  space. Whitespace is not a defect.
- **Density is not quality.** Days 1–3 read well because slides breathe. Match
  `presentation/d3.html` for density — study its ACT 2 and ACT 5, which are the
  strongest figure work in the series.

## Namespacing — how nine parallel redesigns merge

Taken in `d4.html` already: `.aop- .a0- .a1- .a1v- .d4-` plus all house classes.

Your act gets a fresh prefix. Use it for **every** new selector, in **one**
`<style data-act="<your-tag>">` block:

| Act | CSS prefix | style tag | SVG id prefix |
| --- | --- | --- | --- |
| OPENING | `.aopf-` | `data-act="opening-f"` | `aopf` |
| ACT 0 | `.a0f-` | `data-act="0f"` | `a0f` |
| ACT 1 | `.a1f-` | `data-act="1f"` | `a1f` |
| ACT 2 | `.a2f-` | `data-act="2f"` | `a2f` |
| ACT 3 | `.a3f-` | `data-act="3f"` | `a3f` |
| ACT 4 | `.a4f-` | `data-act="4f"` | `a4f` |
| ACT 5 | `.a5f-` | `data-act="5f"` | `a5f` |
| ACT 6 | `.a6f-` | `data-act="6f"` | `a6f` |
| CLOSE | `.aclf-` | `data-act="close-f"` | `aclf` |

**These 22 ids are taken — never reuse one:**
`a0coreG a0coreGlow a0flyCore a0flyGlow a0flyHot a0gContext a0gEval a0gGraph
a0gHarness a0gLoop a0gSpec a0hotGlow d4clCore d4clGlow d4mBad d4mGlow d4mGood
dcAct dcBar n total tracker`

Inline SVG only. No JavaScript, no external assets, no chart libraries, no
`<canvas>`. Charts are hand-built SVG with real coordinates.

## The measurement gate — non-negotiable

Every slide must fit **1600×900** with no vertical overflow. Figures make this
easy to break. Check every slide you touch, and in your reply list each slide's
content height against its available height. If something does not fit, cut words
or simplify the figure — never shrink type below the deck's clamps.

## Colour discipline

Use the tokens, never raw hex outside an SVG: `--accent #4a9eff` · `--cyan
#22d3ee` · `--purple #a78bfa` · `--gold #d4af37` · `--green #3fb950` · `--red
#f85149` · `--silver #b0bec5`.

Meaning is fixed across the whole week and figures must obey it:
**green = passed / proved**, **red = refused / failed / blocked**,
**gold = human authority, a seal, a decision**, **silver = inert, absent, not run**,
**cyan = data or dependency**, **purple = the graph or the plan**.

A green cell must never mean "in progress". A red cell must never mean "warning".

## Your reply

The slide list with what figure each one gained · every slide's measured height vs
available at 1600×900 · anything you believe is factually wrong · anything you
chose **not** to draw and why.

---

# The nine prompts

Each block below is complete. Prepend §The workflow, §The bar, §Namespacing,
§The measurement gate and §Colour discipline, then send one block.

---

## OPENING · slides 1–3 · prefix `.aopf-`

Currently: a title slide, a `flow` manifest, and a programme rendered as rows.

- **Slide 3 "The programme" is the opportunity.** Eight movements with real
  times and real durations is a **timeline**, not a list. Build a horizontal
  band where each movement's width is proportional to its minutes, coloured by
  its act accent, with the break as a gap and the ✦ 21:50 beat marked distinctly.
  The room should see at a glance that movements 02–04 own the middle of the night.
- **Slide 2 "What survived the night"** carries four state facts (6 specs,
  `DOD=COMPLETE`, `done: 0`, `signed_off: false`). Render them as a **counter row
  with provenance** — the number large, the command that produced it beneath in
  mono, so every figure on screen is visibly sourced.
- **Slide 1** is the title. Leave its type alone. If you add anything, make it a
  quiet closed-circuit motif behind the text, dim — the loop not yet running.

---

## ACT 0 · slides 4–10 · prefix `.a0f-`

Has the two strongest figures in the deck already (5 rings, 9 wheel). Do not
touch those two beyond colour-token compliance. Three slides need work.

- **Slide 6 "Complete, valid, never run" is the act's best unbuilt figure.**
  Six specs × four states — validated · `DOD=COMPLETE` · executed · signed — as a
  **6×4 status matrix**. The first two columns fill green, the last two sit empty
  in silver. One glance and the room sees a graph that is finished and has never
  moved. Use the real spec ids from the slide.
- **Slide 8 "No metrics file found"** should feel like an absence, not a
  sentence. A terminal card holding that one line, with an empty-set treatment
  where a populated log would be. This slide is the setup for ACT 6's payoff, so
  build it to be recalled.
- **Slide 10 "The villain, with a face"** — the eval that cannot fail. Render the
  vacuous eval and its green verdict as a **specimen card**: the code, the exit
  code, and a red annotation pointing at what it never touched.

---

## ACT 1 · slides 11–15 · prefix `.a1f-`

Five slides, zero figures, and it is the villain act — the room must *see* the
lie, not read about it.

- **Slide 12 "Three ways an eval lies" is the centrepiece.** Build a
  **three-column diagnostic**: each column gets the eval's code, its green verdict,
  and — revealed beneath — what it actually proves, in red. Same green on top,
  three different emptinesses underneath. The parallel structure is the argument.
- **Slide 13 GO LIVE** keeps `golive` grammar. Add only an evidence strip showing
  `exit 0` beside "nothing built" — the contradiction, side by side.
- **Slide 14 "The verdict"** is a pullquote and should stay one. Do not decorate a
  quote.
- **Slide 15** closes the act. A single hairline figure at most.

---

## ACT 2 · slides 16–21 · prefix `.a2f-`

- **Slide 18 already has an SVG — push it much further.** Mutation discrimination
  is a **matrix**: mutations down, evals across, each cell caught or survived.
  Add a discrimination score as a bar beneath. Show at least one **survivor** and
  mark it as a hole in the gate, not a passing grade. This is the act's argument
  in one figure.
- **Slide 17 "The rule everyone skips"** — five eval-quality rules where the fifth
  is the point. A **numbered scorecard** with four in normal weight and
  falsifiability pulled out in gold.
- **Slide 19 `eval-audit`, in code** — keep the code block, add a small
  **flag anatomy**: each flag labelled with what it does, drawn against the
  command.
- **Slide 21 skill card** keeps `skillcard` grammar. It carries a facilitator
  warning about `skills/prove-the-oracle/` not being built — that warning must
  survive verbatim.

---

## ACT 3 · slides 22–26 · prefix `.a3f-`

The whole act argues about **what the executor can and cannot see**, and nothing
on screen shows a boundary.

- **Slide 23 "Visible is a target" is the figure to build.** Draw the **visibility
  boundary**: inside the executor's context, the spec and its visible evals;
  outside, the sealed holdout. Show the arrow that cannot cross. Goodhart in one
  picture — when the grader is readable, the subject optimises the grader.
- **Slide 24 "seal → verify → run"** is a three-stage pipeline and should look
  like one: each stage with its input, its emitted artifact (sealed bundle,
  verification receipt, result), and who may read what at each step.
- **Slide 26 "Break"** stays large, calm and nearly empty. Do not add a figure.

---

## ACT 4 · slides 27–33 · prefix `.a4f-`

**Seven slides, zero figures, and this is the night's peak.** The biggest single
gain available in the deck is here.

- **Slide 27 "The chain" — build the swimlane.** Two lanes, human and machine.
  Four commands crossing between them: `gate --stamp` → `handoff --backend` →
  `run --ci` → `accept --stamp`. Each emits something — mark `signed_off`,
  the portable handoff, the exit code, `accepted`. The room should see at a glance
  which two steps a human owns and which two the machine owns. This figure is the
  act.
- **Slide 28 "The seal, finally stamped"** — a **before/after** of the spec's
  frontmatter, `signed_off: false` beside `signed_off: true` with the hmac line
  appearing, and the changed lines marked. Day 3 taught the seal and never stamped
  one; this is the payoff, so make the change visible rather than described.
- **Slide 29 "Six gates, not one"** — six gates is a **ladder**: each rung named,
  what it checks, what token it emits (`DOD=COMPLETE`, `TIER=1`, `ACCEPTED=1`),
  and whether it can be skipped.
- **Slides 31–33** are the commercial beat. **Design restraint is the instruction
  here.** Keep them sparse. Slide 33 is a door, not a dashboard — no figure, no
  pricing, no second call to action. Slide 31 carries a facilitator warning about
  the unbuilt giveaway; it must survive verbatim.

---

## ACT 5 · slides 34–38 · prefix `.a5f-`

**Slide 36 is titled "Two waves, drawn" and draws nothing.** Fix that first.

- **Slide 36 — draw the waves.** A timeline: wave 1 with its parallel units, an
  eval gate returning 0, wave 2 opening because of it, and the blocked unit sitting
  outside every wave, greyed, never dispatched. Take the actual widths from the
  slide's own numbers; do not invent a shape.
- **Slide 35 "Write-disjoint means safe"** — this is a **matrix**: units down,
  write paths across, cells marking who touches what. Disjointness becomes visible
  as an absence of collisions in a column, which is far stronger than the sentence.
- **Slide 37 GO LIVE** keeps `golive` grammar; add a compact concurrency strip
  showing the two units dispatched together.
- **Slide 38 "Nobody scheduled that"** is a pullquote. Leave it.

---

## ACT 6 · slides 39–42 · prefix `.a6f-`

A measurement act with no measurements visible.

- **Slide 41 "Measured or declared" wants a real table** — the one genuine table
  in the deck. Every receipt field down the left, and a column marking whether it
  is **measured** (the system observed it) or **declared** (a human asserted it).
  That distinction is the act's honesty and a table states it better than prose.
- **Slide 40 GO LIVE "read the metrics"** — a **before/after**: ACT 0's
  "No metrics file found" on the left, tonight's populated log on the right. This
  is the night's arc in one slide; build it as the payoff it is.
- **Slide 42 "What measurement does not buy"** — the blocked hole is still
  blocked. A small figure showing the graph with every unit measured and one unit
  still grey, still owned by Finance. Do not let the figure imply Revenue moved.

---

## CLOSE · slides 43–45 · prefix `.aclf-`

- **Slide 43 "Turn four closes"** — a **built / withheld / tomorrow** ledger, plus
  the flywheel with four stations lit and the fifth ahead. House `orbit` classes
  exist; use them rather than inventing a new wheel.
- **Slide 44 "Six rings, lit"** is already an SVG and is the week's payoff — every
  ring solid for the first time. Push only its finish: even ring spacing, clean
  labels, nothing dashed. Do not restructure it.
- **Slide 45 "The invariant"** quotes Days 1–3 verbatim. **Do not touch the type
  and do not add a figure.** The deck should end quiet.
