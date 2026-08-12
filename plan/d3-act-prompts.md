# Day 3 — Act build prompts (one per engine)

Six self-contained prompts. Each goes to a different LLM, in its own session,
with no shared context. Each produces one standalone file under
`presentation/`. Nothing is merged until every act renders on its own.

**Naming:** `presentation/d3-act1.html` … `d3-act6.html`.
**Merge:** I extract the `<section class="slide">` elements plus each act's
namespaced `<style>` block and splice them into `d3.html` in act order.

---

## The subject of the night: Task-Spec

**Task-Spec is a real, shipped product** — `~/GitHub/task-spec`,
`github.com/luanmorenommaciel/task-spec`, **v3.7.0**, MIT, works with Codex ·
Claude Code · Kimi · Grok Build · any conformant executor. It is the operator's
own project and it is tonight's giveaway.

Earlier drafts of this deck called it a "Tasks Pack" with "seven fields". That
was wrong on both counts. The canonical facts, from `spec/task-spec-v3.md`:

**Six zones**

| Zone | Contains |
| --- | --- |
| 1 · Intent | Goal, Context |
| 2 · Behavior | `B-N` statements in Given/When/Then |
| 3 · Contract (The Moat) | Success Criteria, Validation Card, Exit Check |
| 4 · Guardrails | Anti-Patterns, Do-Not-Touch |
| 5 · Operations | Open Questions |
| 6 · Reversal & Runtime | Rollback Plan, Observability Hooks (`full` profile only) |

**Four layers** (the README's framing — good for a slide)

| Layer | Fields | Controls |
| --- | --- | --- |
| Bounded workspace | `touches_paths`, `creates_paths`, Do-Not-Touch | where the executor may write |
| Execution contract | goal, context, `depends_on`, `effort`, agent contract, budgets | what the unit means, how much autonomy |
| Executable proof | success criteria, evals, Exit Check, DoD traceability | what observable behavior counts as success |
| Authorization envelope | `signed_off*`, `hmac-sha256-v2` | whether body and authority still match human sign-off |

**The bidirectional traceability rule** — the strongest idea in the product:
every `B-N` is verified by ≥1 eval carrying `verifies: [B-N]`, and every eval
maps to ≥1 behavior. An unverified behavior is a hole; an eval with no
`verifies:` is scope creep. `validate-task-spec.sh` walks the graph both ways
and hard-fails on any unmatched node. **Neither may dangle.**

**Effort sizing is the decomposition rule:** `XS`/`S`/`M`/`L` are runnable
leaves; `XL`/`XXL` are non-runnable composition nodes requiring `children`
(≥2 for XL, ≥3 for XXL). Nodes are composed, never delegated.

**Other real facts:** `id` format `T-YYYYMMDD-<kebab-slug>` ·
`budget_iterations` default 15, hard cap 30 · `status` ∈ ready, in-progress,
blocked, done, parked · profiles `lite`/`standard`/`full` · CLI verbs
`validate`, `dod`, `gate --stamp`, `run`, `accept --stamp`, `transition`,
`ready`, `lint` · `gate --stamp` prints `VERDICT: DELEGATE` and `TIER=1` ·
only the gate writes `signed_off*`, only acceptance writes `accepted*`.

**Why the seal matters tonight:** Day 2 ended with a human confirming a
contract out loud. Task-Spec makes that confirmation tamper-evident — the
sign-off is bound by HMAC to the exact body, so changing one character of the
task after approval breaks the seal. That is the true Day 2 → Day 3 bridge, and
it should surface in ACT 2 and pay off in ACT 6.

---

## Shared contract (already inside every prompt — do not re-send)

| Rule | Reason |
| --- | --- |
| New CSS in one `<style data-act="N">` block, every selector prefixed `.a<N>-` | Six engines inventing `.card` would collide on merge |
| New SVG/filter/gradient `id`s prefixed `a<N>-` | Duplicate ids silently break — the browser binds the first match |
| Reserved ids, never reuse: `coreG coreGlow eqCore eqCoreGlow eqGlow g1–g6 hotGlow dcAct dcBar n total tracker` | Already used by OPENING + ACT 0 |
| Images: inline SVG, or the four existing files in `../assets/` | The deck must run offline on a projector |
| Every slide fits 1600×900 — content ≤ 850px inside section padding | Anything taller is clipped live |
| Every `<section>` carries `data-act` and `data-act-name` | They drive the HUD act chip and progress rail |
| All visible copy English; PT originals only in hidden `speaker-notes` | d2 convention |
| Numbers only from `storage/specs/`, `~/GitHub/task-spec`, or the cited recording | Never invent a metric |

---

## PROMPT — ACT 1

```text
You are building one act of a conference slide deck. Work only in this repository.

READ FIRST, in this order:
1. presentation/d3.html — the master deck. OPENING + ACT 0 are built (9 slides).
   Study its CSS block, slide grammar, and how ACT 0's slides are composed.
   This is your design system. Match it exactly.
2. presentation/d2.html — the previous night's deck, 40 slides. Its ACT 1
   (data-act="ACT 1") is your structural reference for pacing.
3. plan/d3-agenda.md — the night's narrative.
4. live/d3/00-inheritance.md and live/d3/01-plausible-plan.md — the two live
   checkpoints this act introduces. Your go-live slides must describe exactly
   what these files do.
5. storage/specs/4-plan-transform.md — tonight's raw material.

BUILD: presentation/d3-act1.html — a standalone, self-contained HTML file.
Copy d3.html's entire <head>, <style>, deck chrome and <script> so the file
opens and navigates on its own. Replace the slides with YOUR ACT 1 SLIDES ONLY.

ACT 1 — "The plan is not the work" · accent green · 6 slides
Narrative: the night's villain is revealed. Day 2's villain was loud (an agent
claiming authority nobody gave it). Tonight's is quiet: a plan item that would
pass any code review and still permits three different builds.

Slides:
1. Act divider. Use d2's divider grammar: act-num "01", two-tone headline, tag
   chips, and a `flow` of claims on the right.
2. "The inheritance, verified" — GO LIVE slide for live/d3/00-inheritance.md.
   Name the file. Show what runs (make status, ls storage/specs/, make dbt-check)
   and what each command can and cannot prove. The unprovable one: what "done"
   means.
3. "Ten items, three blocked" — the transform plan as an artifact. Item 7 is the
   one we attack. Quote it VERBATIM from storage/specs/4-plan-transform.md:
   "mart_daily_gross_ordered — sum by ordered_at, non-cancelled orders;
    grain = UTC calendar day, labeled as a technical window"
4. "GO LIVE · One item, three builds" — for live/d3/01-plausible-plan.md. The
   same text goes to three fresh sessions. Nothing executes.
5. "Three defensible answers" — the divergence made concrete. The three axes:
   which statuses count as non-cancelled; which upstream model it reads
   (stg_orders vs int_orders_payments_reconciled); where the technical-window
   label lives (column, model name, schema description, or an unread comment).
6. Act close: "Mentioned, not specified." The line to land: a plan item that
   permits three builds has not been specified — it has been mentioned.

Push the visual craft. ACT 0 uses two large hand-built SVG figures; ACT 1 should
earn at least one strong original visual — a divergence diagram (one input,
three outputs, one question mark) is the obvious candidate. Inline SVG only.

HARD RULES — a violation breaks the merge:
- New CSS in ONE block: <style data-act="1"> ... </style>, EVERY selector
  prefixed .a1- (e.g. .a1-diverge). Reuse d3.html's existing classes wherever
  they fit — prefer them over new ones.
- New svg/gradient/filter ids prefixed a1-. NEVER reuse: coreG coreGlow eqCore
  eqCoreGlow eqGlow g1 g2 g3 g4 g5 g6 hotGlow dcAct dcBar n total tracker.
- Every <section class="slide"> needs data-act="ACT 1" and a unique
  data-act-name. data-accent="green" (one slide may differ for contrast).
- Images: inline SVG only, or the existing ../assets/*.png|jpg. No external URLs.
- All visible text in English.
- Every slide ends with <div class="src"> and a hidden
  <aside class="speaker-notes" hidden>[Sources] ... [/Sources] Talk track: ...
  </aside>. Copy that pattern from d3.html exactly.
- Numbers only from storage/specs/. Do not invent metrics.
- Revenue stays unresolved and owned by Finance.

VERIFY BEFORE YOU FINISH — actually run these:
1. Open at 1600x900. Every slide fits, no clipping, no inner scrollbar.
2. Every class token you introduced exists in your .a1- block or in d3.html.
3. No id collides with the reserved list.
4. <section> open/close counts match; HTML comments balanced.

Report: slide count, classes added, ids added, deliberate departures and why.
```

---

## PROMPT — ACT 2

```text
You are building one act of a conference slide deck. Work only in this repository.

THE SUBJECT OF THIS ACT IS A REAL PRODUCT. Read its source of truth first:
  ~/GitHub/task-spec — Task-Spec v3.7.0, MIT, github.com/luanmorenommaciel/task-spec
  Read: README.md (the "Inside one atomic task" section) and
        spec/task-spec-v3.md (File anatomy, Zones 1-6, Field reference).
Do NOT invent fields. Every field name on your slides must exist in that spec.

THEN READ:
1. presentation/d3.html — the master deck. OPENING + ACT 0 are built. Its CSS
   and slide grammar are your design system; match exactly. Slide 7 ("The spec,
   in code") introduces the structure YOUR ACT teaches in full.
2. presentation/d2.html — its ACT 3 (harness anatomy, "Eight layers") is your
   structural reference: a concept act that teaches a structure, then writes it
   by hand live.
3. live/d3/02-tasks-pack.md — the live checkpoint your go-live slide describes.
4. storage/specs/4-plan-transform.md — item 7, the work being specified.

BUILD: presentation/d3-act2.html — standalone, self-contained. Copy d3.html's
<head>, <style>, deck chrome and <script>; replace the slides with ACT 2 only.

ACT 2 — "Anatomy of a Task-Spec" · accent accent(blue) · 5 slides
Narrative: this is the teaching core of the night. One plan item permits three
builds; a Task-Spec closes that gap by binding, for exactly one atomic change,
what may be touched, what behavior counts as success, what proves it, and who
authorized it.

THE SIX ZONES (canonical — from spec/task-spec-v3.md):
  Zone 1 · Intent      — Goal, Context
  Zone 2 · Behavior    — B-N statements in Given/When/Then
  Zone 3 · Contract    — Success Criteria, Validation Card, Exit Check ("The Moat")
  Zone 4 · Guardrails  — Anti-Patterns, Do-Not-Touch
  Zone 5 · Operations  — Open Questions
  Zone 6 · Reversal    — Rollback Plan, Observability Hooks (full profile only)

THE FOUR LAYERS (the README's framing — excellent for the anatomy slide):
  Bounded workspace     touches_paths, creates_paths, Do-Not-Touch
  Execution contract    goal, context, depends_on, effort, agent contract, budgets
  Executable proof      success criteria, evals, Exit Check, DoD traceability
  Authorization envelope signed_off*, hmac-sha256-v2

Real frontmatter fields: id (format T-YYYYMMDD-<kebab-slug>), title, status
(ready|in-progress|blocked|done|parked), effort (XS|S|M|L runnable leaves;
XL|XXL composition nodes), budget_iterations (default 15, cap 30), agent,
depends_on, touches_paths, creates_paths, source_note, created, tags.

Slides:
1. Act divider, "02", d2 divider grammar.
2. "Six zones, one contract" — THE anatomy slide of the night. This will be
   photographed; make it the best thing in the deck. Consider composing it as
   the four layers with the six zones mapped into them.
3. "The seal" — the idea that makes this the true sequel to Day 2. Last night a
   human confirmed a contract out loud. Task-Spec binds that sign-off to the
   exact body with hmac-sha256-v2: change one character after approval and the
   seal breaks. Only `taskspec gate --stamp` writes signed_off*; only acceptance
   writes accepted*. Authority stops being a memory and becomes tamper-evident.
4. "GO LIVE · Write the Task-Spec by hand" — for live/d3/02-tasks-pack.md. The
   human types the zones, 15-20 minutes, unhurried. The point: the hard part is
   not typing, it is deciding what done means precisely enough to be checked.
   Note the task targets dbt/models/staging/stg_daily_gross_ordered.sql — item 7
   names a *mart*, but the Day 2 contract authorizes staging/ only and
   4-plan-transform.md says the marts layer needs its own scope extension, so
   touches_paths scopes down instead of widening the contract. Name that
   restraint on the slide; it is a teaching beat.
5. Skill card S1 — condense the method: Intent -> Behavior -> Proof -> Seal,
   with a gate under each. Copy the skill-card pattern from d2.html (search
   "Skill card").

Push the visual craft. The anatomy slide should be an original composition, not
a plain table. Inline SVG welcome.

HARD RULES — a violation breaks the merge:
- New CSS in ONE block: <style data-act="2">, every selector prefixed .a2-.
- New svg/gradient/filter ids prefixed a2-. NEVER reuse: coreG coreGlow eqCore
  eqCoreGlow eqGlow g1 g2 g3 g4 g5 g6 hotGlow dcAct dcBar n total tracker.
- Every <section class="slide"> needs data-act="ACT 2", unique data-act-name,
  data-accent="accent".
- Images: inline SVG only, or existing ../assets/*. No external URLs.
- All visible text English.
- Every slide ends with <div class="src"> and hidden speaker-notes with
  [Sources] and a Talk track. Cite spec/task-spec-v3.md for field claims.
- Never invent a Task-Spec field. If it is not in the spec, it does not go on a
  slide.
- Revenue stays unresolved, owned by Finance.

VERIFY BEFORE YOU FINISH:
1. Open at 1600x900. Every slide fits.
2. Every introduced class exists in your .a2- block or in d3.html.
3. No reserved-id collision.
4. <section> counts match; comments balanced.
5. Grep spec/task-spec-v3.md for every field name you put on a slide. Any miss
   is a bug — fix it and say so.

Report: slide count, classes added, ids added, departures and why.
```

---

## PROMPT — ACT 3

```text
You are building one act of a conference slide deck. Work only in this repository.

THE SUBJECT OF THIS ACT IS A REAL PRODUCT. Read its source of truth first:
  ~/GitHub/task-spec — Task-Spec v3.7.0, MIT.
  Read spec/task-spec-v3.md, specifically "Zone 2 — Behavior", "The
  traceability rule (bidirectional)", and "Zone 3 — Contract (The Moat)".
Do NOT invent fields or rules.

THEN READ:
1. presentation/d3.html — master deck, OPENING + ACT 0 built. CSS and slide
   grammar are your design system.
2. presentation/d2.html — note how it renders code (class="code" with data-lang
   and .c/.k/.s/.n/.g/.r/.w syntax spans). Your act is code-heavy; use that
   exact treatment.
3. live/d3/03-bdd-and-evals.md — the live checkpoint your go-live slide describes.

BUILD: presentation/d3-act3.html — standalone, self-contained.

ACT 3 — "Neither may dangle" · accent gold · 5 slides
Narrative: "Done" has two readers. A stakeholder cannot review a bash assertion;
a machine cannot run a sentence. Task-Spec's answer is Zone 2 + Zone 3 bound by
a rule that runs in CI.

THE BIDIRECTIONAL TRACEABILITY RULE — the heart of this act, quote it exactly:
  1. Every B-N is verified by >=1 eval whose validation-card entry carries
     verifies: [B-N]. An unverified behavior is a hole.
  2. Every eval maps to >=1 behavior — an eval with no verifies: is testing
     something the spec never promised (scope creep) and is rejected.
  validate-task-spec.sh walks the B-N <-> verifies: graph in BOTH directions and
  hard-fails on any unmatched node.

Behavior format, from the spec:
  ## Behaviors
  - **B-1** — GIVEN the raw orders table carries six distinct statuses
    WHEN stg_daily_gross_ordered aggregates total_amount by ordered_at
    THEN orders with status 'cancelled' are excluded.
  - **B-2** — GIVEN the aggregate exists
    WHEN it is named and described
    THEN it is labeled a technical window and never "Revenue".

Contract side (Zone 3), with the traceability link:
  eval_1() { make dbt-check >/dev/null 2>&1; }              # verifies: [B-1]
  eval_2() { grep -q "cancelled" dbt/models/staging/stg_daily_gross_ordered.sql; }  # verifies: [B-1]
  eval_3() { ! grep -ril "revenue" dbt/models/ | grep -q . ; }  # verifies: [B-2]
  exit_check: eval_1 && eval_2 && eval_3

Slides:
1. Act divider, "03", d2 divider grammar.
2. "Behavior and proof, bound both ways" — THE slide of this act. B-N statements
   on top, evals below, with visual connectors showing verifies: in one
   direction and coverage in the other. Show what a DANGLING node looks like on
   each side: a behavior with no eval (a hole) and an eval with no behavior
   (scope creep). Both are rejected by the validator. This mutual obligation is
   the whole idea.
3. "What makes an eval terminal" — deterministic, idempotent, non-flaky, and
   answerable by a machine without a human judging. The test: can a machine
   return yes or no without your opinion? If not, rewrite it.
4. "GO LIVE · Run the exit check before the build" — for
   live/d3/03-bdd-and-evals.md. The exit check runs BEFORE anything is built and
   returns non-zero. That failing number is the proof the gate is real. Make the
   non-zero exit the hero of the slide.
5. BREAK slide. Movement 03 ends ~21:20; the Task-Spec stays on the projector
   through the break. Calm and nearly empty — d2 has no dedicated break slide,
   so this is yours to invent. Time, one line, nothing else.

Push the visual craft. Slide 2's bidirectional binding deserves real design:
connectors, colour-matched clauses, and a visible broken link on each side.

HARD RULES — a violation breaks the merge:
- New CSS in ONE block: <style data-act="3">, every selector prefixed .a3-.
- New svg/gradient/filter ids prefixed a3-. NEVER reuse: coreG coreGlow eqCore
  eqCoreGlow eqGlow g1 g2 g3 g4 g5 g6 hotGlow dcAct dcBar n total tracker.
- Every <section class="slide"> needs data-act="ACT 3", unique data-act-name,
  data-accent="gold".
- Images: inline SVG only, or existing ../assets/*. No external URLs.
- All visible text English. Code samples exactly as written above.
- Every slide ends with <div class="src"> and hidden speaker-notes with
  [Sources] and a Talk track. Cite spec/task-spec-v3.md for the rule.
- Never invent a field or a rule. Grep the spec if unsure.
- Revenue stays unresolved. eval_3 exists precisely to forbid it.

VERIFY BEFORE YOU FINISH:
1. Open at 1600x900. Every slide fits.
2. Every introduced class exists in your .a3- block or in d3.html.
3. No reserved-id collision.
4. <section> counts match; comments balanced.

Report: slide count, classes added, ids added, departures and why.
```

---

## PROMPT — ACT 4

```text
You are building one act of a conference slide deck. Work only in this repository.

THE SUBJECT OF THIS ACT IS A REAL PRODUCT — and it is tonight's giveaway:
  ~/GitHub/task-spec — Task-Spec v3.7.0, MIT,
  github.com/luanmorenommaciel/task-spec
  Read README.md (Install, Quickstart, the CLI table) and spec/task-spec-v3.md
  (Field reference — especially effort, children, depends_on).
Do NOT invent fields, commands, or version numbers.

THEN READ:
1. presentation/d3.html — master deck, OPENING + ACT 0 built. CSS and slide
   grammar are your design system.
2. presentation/d2.html — study its BriefSpec giveaway slide (search "yours
   tonight" / "take it home"). Your act ends with the same kind of giveaway and
   must feel like a sibling of it, not a copy.
3. live/d3/04-decompose.md — the live checkpoint.
4. storage/specs/4-plan-transform.md — items 5-8 are what gets decomposed.

BUILD: presentation/d3-act4.html — standalone, self-contained.

ACT 4 — "One item becomes a graph" · accent purple · 7 slides
(This act carries the night's commercial peak. Slides 4-6 are a giveaway →
crank → offer sequence placed deliberately in the MIDDLE of the evening, not at
the close, because the room is post-break and the hand-vs-machine contrast from
movements 02-04 is at its most vivid. Read the "Bootcamp" section of
plan/d3-agenda.md before building those three.)
Narrative: one Task-Spec took fifteen minutes by hand. A plan has ten items; a
real backlog has hundreds. Decomposition turns the spec from a craft object into
a system.

DECOMPOSITION IS A TYPED RULE IN THE PRODUCT — use it, do not invent one:
  effort XS | S | M | L  = runnable leaves — an executor may take these
  effort XL | XXL        = non-runnable composition nodes; they REQUIRE children
                           (>=2 ids for XL, >=3 for XXL) and have touches_paths: []
  "Nodes are composed, never delegated."
So decomposition is not a style preference: an XL cannot be executed at all. The
graph is enforced by the format.

Ordering fields: depends_on (list of Task-Spec ids that must complete first),
blocks (the inverse), precondition (an external event that is not a task).

Slides:
1. Act divider, "04", d2 divider grammar.
2. "Leaves and nodes" — the effort ladder as the decomposition rule. XS/S/M/L
   can be handed to an executor; XL/XXL cannot be executed at all and must carry
   children. Show a node expanding into leaves. This is the slide that makes
   "split it smaller" a mechanical rule instead of advice.
3. "GO LIVE · Decompose" — for live/d3/04-decompose.md. The architect cuts items
   5-8 into 4-6 leaf specs under one node. Then, deliberately, item 10 (the
   revenue model) is requested — and cannot become a Task-Spec at all, because
   its Behavior zone cannot be written while the concept is unresolved. It stays
   BLOCKED, owner Finance. The refusal survived becoming a graph: that is the
   punch line.
4. THE GIVEAWAY (beat 1 of 3). Task-Spec itself — v3.7.0, MIT,
   github.com/luanmorenommaciel/task-spec, works with Codex, Claude Code, Kimi,
   Grok Build, or any conformant executor. Show the real install line from the
   README. Say plainly what it does NOT do: it cannot size the task for you, it
   cannot tell you whether an eval is genuinely terminal, and it cannot write a
   behavior your stakeholder would sign. Structure is free; judgment is not.
   ONE sentence on what is free, ONE on what is not. Do not stack benefits.
5. THE CRANK (beat 2 of 3). The desire beat. The room has watched ONE spec
   written by hand over 15-20 slow minutes, then 4-6 generated in seconds. Now
   show the loop CONSUMING the graph: specs dispatched in dependency-respecting
   waves, evals deciding done, no human in the middle. The line: one human wrote
   one spec in twenty minutes; the loop runs six without being asked.
   This is Day 4's subject arriving early — say so on the slide, it is a preview
   and not a detour. The footage is PRE-RECORDED: label it "recorded — not live
   output", exactly the way d2.html labels illustrative output. Never imply it
   ran live.
6. THE LADDER + THE OFFER (beat 3 of 3). This is the night's commercial peak and
   it sits HERE, in the middle, not at the close — the room is twenty minutes
   past the break and the hand-vs-machine contrast is still vivid.
   First the mirror — Dan Shapiro's five levels of code automation, mapped to the
   NHTSA autonomous-driving levels:
     0 Manual · 1 Delegated tasks · 2 Pairing in flow ·
     3 You became a manager  <- THE ROOM IS HERE, life becomes reviewing diffs ·
     4 You became a PM · 5 The autonomous factory
   Say the true and uncomfortable thing: almost everyone parks at level 3 and it
   feels like a downgrade. Then place tonight: writing a Task-Spec whose exit
   check answers for itself is the first move from 3 to 4.
   Then the offer, plainly and ONCE:
     Bootcamp Engenharia Agêntica na Prática · 24-28/08, seg a sex
     19h30-23h30 · cinco noites ao vivo
     de R$1.997 por R$1.297 com o cupom DESLIVE
     garantia de 7 dias incondicional
     caso: NorthWind Pay — migração de plataforma financeira legada,
     validada centavo por centavo contra o próprio legado como oráculo
   The honest framing that makes this not-a-pitch: Task-Spec is item 04 of the
   Bootcamp's own six-item arsenal (Second Brain, OntoLayer, AgentSpec,
   Task-Spec, Multi-Model Harness, Converge). The room has been using one sixth
   of it all night and keeps it. The Bootcamp is the other five plus the case.
   State that once. Do NOT list all six with benefits — that turns a disclosure
   into a sales page. No urgency language, no second CTA, no benefit stacking.
7. Act close — enumeration ends here; the next act orders it. Deliberately quiet
   after the offer, so the night resumes as teaching rather than selling.

ACT 4 IS THEREFORE 7 SLIDES, NOT 5. Slides 4-6 are the giveaway → crank → offer
sequence and they run about five minutes total on the night.

Push the visual craft. Slide 2's node-to-leaves expansion and slide 3's
dependency graph are both strong original-visual opportunities. Inline SVG.

HARD RULES — a violation breaks the merge:
- New CSS in ONE block: <style data-act="4">, every selector prefixed .a4-.
- New svg/gradient/filter ids prefixed a4-. NEVER reuse: coreG coreGlow eqCore
  eqCoreGlow eqGlow g1 g2 g3 g4 g5 g6 hotGlow dcAct dcBar n total tracker.
- Every <section class="slide"> needs data-act="ACT 4", unique data-act-name,
  data-accent="purple".
- Images: inline SVG only, or existing ../assets/*. No external URLs.
- All visible text English.
- Every slide ends with <div class="src"> and hidden speaker-notes with
  [Sources] and a Talk track.
- Version numbers, install commands and CLI verbs must be copied from the repo,
  not remembered. Grep before you write.
- The giveaway must not oversell. Day 2 proved the room accepts the hook when it
  lasts one line.
- Revenue stays unresolved. Item 10 is refused, never built.

VERIFY BEFORE YOU FINISH:
1. Open at 1600x900. Every slide fits.
2. Every introduced class exists in your .a4- block or in d3.html.
3. No reserved-id collision.
4. <section> counts match; comments balanced.
5. Every command and version on a slide appears verbatim somewhere in
   ~/GitHub/task-spec. Check it.

Report: slide count, classes added, ids added, departures and why.
```

---

## PROMPT — ACT 5

```text
You are building one act of a conference slide deck. Work only in this repository.

THE SUBJECT IS A REAL PRODUCT: ~/GitHub/task-spec — Task-Spec v3.7.0, MIT.
Read README.md's CLI table and spec/task-spec-v3.md's "Status Lifecycle" and
depends_on / blocks / precondition field definitions. `taskspec ready` is a REAL
command — this act is about what it computes. Do not invent behavior.

THEN READ:
1. presentation/d3.html — master deck, OPENING + ACT 0 built. CSS and slide
   grammar are your design system.
2. presentation/d2.html — for pacing of a short concept act.
3. live/d3/05-ready-set.md — the live checkpoint.

BUILD: presentation/d3-act5.html — standalone, self-contained.

ACT 5 — "The ready set" · accent cyan · 4 slides
(Shorter on purpose. Day 2's ACT 6 ran three slides and landed fine — do not pad.)

Narrative: a graph without an order is still not work. The ready set is the
small idea that replaces a project manager: the specs whose depends_on have all
reached done. The executor picks from that set; nobody decides what is next.

Core content:
- Ready is computed, not chosen. Not list order, not business priority, not
  alphabetical.
- status lifecycle: ready | in-progress | blocked | done | parked. done requires
  acceptance — `accepted*` is written by acceptance, never by the executor. So
  "ready" downstream means a real gate passed upstream, not that someone ticked
  a box.
- precondition is deliberately NOT a task: an external event (a spec being
  checked in, an access grant) blocks work without pretending to be work.
- Shallow graphs keep the ready set large. A deep chain is a smell: either the
  split went too far or an intermediate spec does too little.

Slides:
1. Act divider, "05", d2 divider grammar.
2. "Ready is computed, not chosen" — the definition, the three wrong orderings
   it replaces, and the status lifecycle. A dependency graph with the ready set
   highlighted is the natural visual.
3. "GO LIVE · Name the ready set" — for live/d3/05-ready-set.md. A table of at
   most 8 rows: spec, depends_on, ready now, one-line justification. Every
   verdict traces to depends_on alone. Show one spec that is NOT ready and what
   it waits on — and one blocked by a precondition rather than by a task.
4. Act close: "Nobody in this room decided that order. The graph did — and it
   will still be right tomorrow, when none of us remember writing it."

Push the visual craft: the dependency graph with the ready set highlighted is
the one figure this act needs, and it should be excellent. Inline SVG.

HARD RULES — a violation breaks the merge:
- New CSS in ONE block: <style data-act="5">, every selector prefixed .a5-.
- New svg/gradient/filter ids prefixed a5-. NEVER reuse: coreG coreGlow eqCore
  eqCoreGlow eqGlow g1 g2 g3 g4 g5 g6 hotGlow dcAct dcBar n total tracker.
- Every <section class="slide"> needs data-act="ACT 5", unique data-act-name,
  data-accent="cyan".
- Images: inline SVG only, or existing ../assets/*. No external URLs.
- All visible text English.
- Every slide ends with <div class="src"> and hidden speaker-notes with
  [Sources] and a Talk track.
- Status values and CLI verbs copied from the repo, not remembered.
- Revenue stays unresolved.

VERIFY BEFORE YOU FINISH:
1. Open at 1600x900. Every slide fits.
2. Every introduced class exists in your .a5- block or in d3.html.
3. No reserved-id collision.
4. <section> counts match; comments balanced.

Report: slide count, classes added, ids added, departures and why.
```

---

## PROMPT — ACT 6 + CLOSE

```text
You are building the final act and the close of a conference slide deck. Work
only in this repository.

THE SUBJECT IS A REAL PRODUCT: ~/GitHub/task-spec — Task-Spec v3.7.0, MIT.
Read README.md's "How it works" and the CLI table, plus spec/task-spec-v3.md's
"Status Lifecycle" and "Agent Contract (cross-vendor portability)".
The real execution chain is: validate -> dod -> gate --stamp (writes signed_off*,
prints VERDICT: DELEGATE and TIER) -> run (any conformant harness) ->
accept --stamp (writes accepted*) -> transition ... done.
Only the gate writes signed_off*. Only acceptance writes accepted*. Do not
invent commands or reorder that chain.

THEN READ:
1. presentation/d3.html — master deck, OPENING + ACT 0 built. Design system.
2. presentation/d2.html — study its CLOSE slides ("Turn two", "The invariant").
   Yours are the direct sequel and must rhyme with them. Also study its ACT 5
   "GO LIVE · Bounded build", which pairs a pass with a refusal on one screen.
3. plan/d3-agenda.md — the Bootcamp section and the completion gate.
4. live/d3/06-execute-one.md and live/d3/07-reflection.md.

BUILD: presentation/d3-act6.html — standalone, self-contained. Contains BOTH
ACT 6 and CLOSE.

ACT 6 — "One spec, one iteration" · accent green · 4 slides
Narrative: everything so far was specification. This is the test. One Task-Spec,
one fresh context, one commit — and the agent decides it is finished by running
the spec's own Exit Check, not by asking.

Slides:
1. Act divider, "06", d2 divider grammar.
2. "Fresh context, files as memory" — the trajectory. Session C receives ONLY
   the Task-Spec and AGENTS.md. No plan, no transcript, no chat memory. That
   isolation is the proof: if the spec works, it works from files. Show the real
   chain: gate --stamp -> VERDICT: DELEGATE -> run -> Exit Check -> accept.
3. "GO LIVE · Execute one spec" — for live/d3/06-execute-one.md. TWO outcomes on
   one screen: the Exit Check returning 0 (the pass), and item 10 refused with
   Finance named and no file written (the refusal). Both are the system working.
   Mark any illustrative output as "expected shape — not live output", the way
   d2 does.
4. "Same spec, any engine" — Task-Spec is vendor-neutral by design: agent: any,
   and the README lists Codex, Claude Code, Kimi, Grok Build, any conformant
   executor. The spec is files, so it survives the engine swap exactly as
   AGENTS.md did on Day 2. Reuse ../assets/claude-code-icon.png,
   ../assets/codex.png, ../assets/kimi.png.

CLOSE · accent gold · 2 slides
IMPORTANT — there is NO Bootcamp slide in the close. The offer was made once, in
ACT 4, in the middle of the night, at the room's energy peak. Repeating it here
would turn the evening into a funnel. The close may carry at most ONE neutral
line pointing back to it (e.g. a single muted footer line with the dates), and
nothing more. Do not add a CTA, a price, or a second ask.
5. "Turn three" — the night's ledger, mirroring d2's "Turn two":
   BUILT (4): one Task-Spec written by hand; behaviors bound to evals both ways;
   the task graph with its ready set; one spec executed from files alone.
   WITHHELD (1): Revenue — still unresolved, still owned by Finance. Item 10
   could not become a Task-Spec, because its Behavior zone cannot be written
   while the concept is undecided. That refusal was a success.
   TOMORROW: Day 4 — specs get run in a loop and measured; the unit of work
   becomes the unit of measurement.
   Include the three reflection lines from live/d3/07-reflection.md.
6. "The invariant" — the week's closing line, unchanged from Days 1 and 2:
   "The agent performs bounded work. Evidence supports claims. Humans keep the
   decisions the system cannot legitimately make."
   Then: "Day 4 · the unit of work becomes the unit of measurement — 20:00 BRT".
   Match d2's final slide: large, quiet, almost empty.

HARD RULES — a violation breaks the merge:
- New CSS in ONE block: <style data-act="6">, every selector prefixed .a6-.
- New svg/gradient/filter ids prefixed a6-. NEVER reuse: coreG coreGlow eqCore
  eqCoreGlow eqGlow g1 g2 g3 g4 g5 g6 hotGlow dcAct dcBar n total tracker.
- ACT 6 sections: data-act="ACT 6", data-accent="green". CLOSE sections:
  data-act="CLOSE", data-accent="gold". Unique data-act-name on each.
- Images: inline SVG, or existing ../assets/* (three engine icons and
  luan-moreno-web.jpg). No external URLs.
- All visible text English.
- Every slide ends with <div class="src"> and hidden speaker-notes with
  [Sources] and a Talk track.
- CLI verbs and their order copied from the repo, not remembered.
- Revenue stays unresolved and owned by Finance through the last slide.
- The Bootcamp slide must not oversell.

VERIFY BEFORE YOU FINISH:
1. Open at 1600x900. Every slide fits.
2. Every introduced class exists in your .a6- block or in d3.html.
3. No reserved-id collision.
4. <section> counts match; comments balanced.
5. The act chip flips from "ACT 6" to "CLOSE" at the right slide.
6. Every CLI verb on a slide exists in ~/GitHub/task-spec. Check it.

Report: slide count, classes added, ids added, departures and why.
```

---

## After the engines return

Merge order: ACT 1 → 2 → 3 → 4 → 5 → 6 → CLOSE, spliced into `d3.html` between
ACT 0's last slide and the closing `</div>`.

Merge checklist per act:
1. Extract `<section class="slide">` blocks and the `<style data-act="N">` block.
2. Assert every `.aN-` selector used is defined; no unprefixed new class leaked.
3. Assert no id collision across all acts and the master.
4. Re-render the full deck at 1600×900 and re-measure every slide.
5. Re-check the act rail: 9 groups, correct order and counts.
6. Grep every Task-Spec field name and CLI verb against `~/GitHub/task-spec`.

Expected final size: ~40 slides, matching d2.
