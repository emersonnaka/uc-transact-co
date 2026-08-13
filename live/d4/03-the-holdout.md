# 03 — The holdout

## Session

**Continue Session B.** Still the architect. The holdout is sealed by the
**facilitator**, not by the agent — that separation is the point of the checkpoint,
so make it visible: type the seal command yourself, in a terminal the agent session
cannot see.

This checkpoint ends with the break slide.

## Why this step

Checkpoint 02 made one eval falsifiable. But every eval in a Task-Spec lives *inside*
the spec, which means the executor reads it. An executor that can read its own grader
can satisfy the grader instead of the goal — and it does not need bad intent to do
that, only an optimizer's preference for the cheapest path.

This is Goodhart's law with a compiler. Named in 1975 and restated by Strathern in
1997: once a measure becomes a target, it stops being a good measure.

The field has a measurement for exactly this now. **SpecBench** (Zhao, Srikanth, Wu
and Jiang, May 2026) grades 30 systems-level coding tasks with *two* suites: a
**validation suite** the agent can see and iterate against, and a **held-out suite**
it never sees, which composes the same features into end-to-end scenarios. The gap
between the two pass rates *is* their measure of reward hacking. Their example is a
SQL database task: validation tests cover `SELECT`, `JOIN` and `GROUP BY`
individually; the held-out tests combine all three. Their finding is the sentence
this checkpoint exists to demonstrate: high validation scores can substantially
overestimate true compliance, and the gap widens as the task gets longer.

`taskspec holdout` is that structure, as three commands.

## Structure

```mermaid
flowchart LR
    A[Author the hidden evaluator] --> B[holdout seal]
    B --> C[HOLDOUT=SEALED · descriptor + digest]
    C --> D[Executor receives the spec ONLY]
    D --> E[Executor works · never reads the bundle]
    E --> F[holdout verify]
    F --> G[HOLDOUT=VERIFIED · bundle unmodified]
    G --> H[holdout run --receipt-out]
    H --> I[Receipt: what the hidden evaluator found]

    classDef human fill:#FEF3C7,stroke:#D97706,color:#78350F
    classDef seal fill:#CFFAFE,stroke:#0891B2,color:#164E63
    classDef exec fill:#DBEAFE,stroke:#2563EB,color:#172554
    classDef proof fill:#DCFCE7,stroke:#16A34A,color:#14532D
    class A,D human
    class B,C,F,G seal
    class E exec
    class H,I proof
```

## Do live

### Move A — draw the asymmetry first

One figure on the deck, no terminal yet.

```text
INSIDE the spec  (the executor reads these)      OUTSIDE the spec  (sealed)
  B-1 → eval_1   cancelled orders excluded         H-1  totals compose across
  B-2 → eval_2   one row per ordered date               all three staging models
  B-3 → eval_3   the model builds                  H-2  no row count regresses
                                                    H-3  the aggregate is never
  visible · iterable · gameable                          labelled revenue
                                                    hidden · not iterable
```

Say the mechanism, not the moral: the visible evals tell the executor what to aim
at, which is what makes them useful *and* what makes them a target. The held-out
evals test the composition the visible ones only test in pieces.

### Move B — author the hidden evaluator

```bash
mkdir -p tmp/d4/holdout/bundle
cat > tmp/d4/holdout/bundle/h1_composition.sh <<'SH'
#!/usr/bin/env bash
# H-1 — the daily aggregate must compose with its source, not merely build.
set -euo pipefail
duckdb warehouse.duckdb -noheader -list -c "
  select case
    when (select count(*) from main.stg_daily_gross_ordered)
       = (select count(distinct cast(ordered_at as date))
            from main.stg_orders where status != 'cancelled')
    then 'PASS' else 'FAIL' end
" | grep -qx PASS
SH

cat > tmp/d4/holdout/bundle/h2_label.sh <<'SH'
#!/usr/bin/env bash
# H-2 — no column in the staging layer may be named revenue. Finance owns that word.
set -euo pipefail
! grep -rniE '\brevenue\b' dbt/models/staging/ --include='*.sql'
SH

chmod +x tmp/d4/holdout/bundle/*.sh
```

`H-2` is the one to point at. It is not a correctness check — it is a **boundary**
check, and it is sealed precisely so that no executor can satisfy the letter of it by
renaming a column to `revenue_amount_do_not_use`.

### Move C — seal

```bash
taskspec holdout seal tmp/d4/holdout/bundle \
  --out tmp/d4/holdout/descriptor.json
echo "exit=$?"
cat tmp/d4/holdout/descriptor.json
```

Expect the token **`HOLDOUT=SEALED`**. Show the descriptor: it carries the digest, not
the bodies. Then say the sentence that governs the rest of the night:

> From this moment the bundle stays off the projector. The descriptor is public. The
> digest is public. The tests are not.

Move the bundle out of any path the executor is allowed to read, and record where it
went in your own notes only.

### Move D — verify, before trusting anything downstream

```bash
taskspec holdout verify tmp/d4/holdout/descriptor.json tmp/d4/holdout/bundle
echo "exit=$?"
```

Expect **`HOLDOUT=VERIFIED`**. This answers a different question than "did the tests
pass" — it answers *"is this the same evaluator I sealed?"* Demonstrate what a
tampered bundle does, because a seal you have never seen break is a decoration too:

```bash
echo "# harmless comment" >> tmp/d4/holdout/bundle/h1_composition.sh
taskspec holdout verify tmp/d4/holdout/descriptor.json tmp/d4/holdout/bundle; echo "exit=$?"
```

`HOLDOUT=INVALID`, exit 1 — from a comment. Undo it, re-verify, and get
`HOLDOUT=VERIFIED` back.

### Move E — run the hidden evaluator against tonight's work

```bash
taskspec holdout run tmp/d4/holdout/descriptor.json tmp/d4/holdout/bundle \
  --workspace . \
  --receipt-out tmp/d4/receipts/holdout-01.json
jq -r '.results[] | [.id, .outcome] | @tsv' tmp/d4/receipts/holdout-01.json
```

Two outcomes on screen. `H-1` should pass against the model built at checkpoint 02.
`H-2` should pass because the column is `gross_ordered_amount`.

Then prove the holdout can fail, exactly as checkpoint 02 proved the eval could:

```bash
sed -i '' 's/gross_ordered_amount/revenue_amount/' \
  dbt/models/staging/stg_daily_gross_ordered.sql
# re-run holdout run   -> H-2 FAILS
sed -i '' 's/revenue_amount/gross_ordered_amount/' \
  dbt/models/staging/stg_daily_gross_ordered.sql
# re-run holdout run   -> H-2 passes again
```

The visible evals never noticed the rename. The sealed one did. That is the whole
argument, performed rather than asserted.

### Move F — the break slide

One line on the projector and the return time. Leave
`tmp/d4/holdout/descriptor.json` on screen during the break — the digest, visible;
the tests, not. If someone asks to see the bundle during the break, that request is
the lesson: say so, warmly, and still decline.

## Show the evidence

- `HOLDOUT=SEALED`, then the descriptor with its digest.
- `HOLDOUT=VERIFIED` → `HOLDOUT=INVALID` after a one-comment edit → `HOLDOUT=VERIFIED`
  after undo.
- The run receipt with two outcomes.
- `H-2` failing on the renamed column while every visible eval stays green.

Never display the bundle bodies after Move C. If a fallback forces you to, announce
that the demonstration is now **prepared** and no longer a real holdout.

## Gate

- A bundle was sealed and the token `HOLDOUT=SEALED` appeared.
- Verification passed, broke on a trivial edit, and passed again after undo.
- A run receipt exists at `tmp/d4/receipts/holdout-01.json`.
- The sealed evaluator caught a change that every visible eval missed.
- No agent session read the bundle at any point.
- `dbt/models/staging/stg_daily_gross_ordered.sql` is back to its checkpoint 02 state
  — confirm with `git diff`.

## Recovery

If `duckdb` is not on `PATH` inside the holdout shell, replace `H-1` with a check on
the compiled SQL text instead of the warehouse — the sealing mechanics matter here,
not the specific assertion. If `holdout seal` fails, fall back to a `sha256sum` of the
bundle written to the descriptor by hand and say plainly that you are demonstrating
the mechanism with a manual digest. Do not skip Move E; a holdout nobody watched fail
teaches nothing.

## Sources

- Two-suite evaluation, and the validation-versus-held-out gap as a *measure* of
  reward hacking: B. Zhao, D. Srikanth, Y. Wu, Z. Jiang, *"SpecBench: Measuring
  Reward Hacking in Long-Horizon Coding Agents"*, Weco AI / arXiv 2605.21384,
  2026-05. Their recommendation, verbatim in spirit: for important projects maintain
  a held-out set that agents never see and never optimise against.
- Goodhart's law, and its restatement: C. Goodhart, 1975; M. Strathern,
  *"Improving Ratings"*, 1997.
- Specification gaming as satisfying the literal specification without achieving the
  intended outcome: V. Krakovna et al., DeepMind, 2020.
- Held-out professional tasks, private eval sets that never touch training data, and
  trajectory monitoring as the response to gameable oracles: A. Shankar, *"The Loop
  Was Never the Hard Part"*, 2026-06-16.
- Scale of the problem, for one honest sentence only: TRACE reports 517 trajectories
  across 54 hack categories with GPT-5.2 detecting 63% (Deshpande et al., 2026);
  OpenAI's audit of SWE-Bench Pro flagged roughly 30% of public tasks as broken and
  retracted its recommendation, 2026-07-08.
- Verified usage: `taskspec holdout {seal,verify,run}`; tokens `HOLDOUT=SEALED`,
  `HOLDOUT=VERIFIED`, `HOLDOUT=INVALID`. `verify` is read-only, v3.7.0.

Next: [`04-the-authorization-chain.md`](04-the-authorization-chain.md).
