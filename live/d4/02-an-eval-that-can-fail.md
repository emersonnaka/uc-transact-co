# 02 — An eval that can fail

## Session

**NEW — Session B.** It carries the proof discipline through checkpoint 03. Session
A is already closed and discarded. Session B is an **architect** for Moves A–C
(judgment, no hands) and the human types the Exit Check rewrite in Move D. The
mutation itself is done by hand, in the terminal, so nobody can suspect the agent
of arranging its own grade.

## Why this step

Checkpoint 01 showed three greens that proved nothing and one red that proved
something. This checkpoint turns that observation into a repeatable procedure with a
name that predates agents by forty years.

Software testing calls the deliberate breaking of code to see whether the tests
notice **mutation testing**. Jia and Harman defined it in their 2011 survey as a
fault-based technique that yields a *mutation adequacy score*: you inject a small
change, and if at least one test fails, the mutant is **killed**; if every test still
passes, the mutant **survives**. A survivor is not a passing grade. A survivor is a
hole in the gate, in a place you can point at.

`taskspec eval-audit` applies exactly that idea to an agent's evals.

## Structure

```mermaid
flowchart LR
    A[Baseline: the work as built] --> B[Inject mutation 1]
    A --> C[Inject mutation 2]
    B --> D{Any eval fails?}
    C --> E{Any eval fails?}
    D -->|Yes| F[KILLED · the gate works here]
    E -->|No| G[SURVIVED · a hole in the gate]
    G --> H[Rewrite the eval, not the test data]
    H --> I[Re-audit until every mutation is killed]

    classDef base fill:#E5E7EB,stroke:#4B5563,color:#111827
    classDef mut fill:#DBEAFE,stroke:#2563EB,color:#172554
    classDef good fill:#DCFCE7,stroke:#16A34A,color:#14532D
    classDef bad fill:#FEE2E2,stroke:#DC2626,color:#7F1D1D
    class A base
    class B,C,D,E mut
    class F,I good
    class G,H bad
```

## Do live

### Move A — the five rules, one of which everyone skips

Put these on the deck, not the terminal. An eval worth trusting is:

1. **deterministic** — same input, same verdict
2. **idempotent** — running it twice changes nothing
3. **cheap before expensive** — the fast check gates the slow one
4. **explainable** — its failure message names what broke
5. **falsifiable** — *it fails when the thing it guards is broken*

Rules 1 to 4 get written. Rule 5 gets assumed. Say it plainly: **rule 5 is the only
one that makes the other four worth anything**, and it is the only one you cannot
verify by reading the eval. You have to run it against broken code.

### Move B — build the thing the eval will guard

We need real work before we can break it. Have the room watch you build the smallest
honest model for the hand-written spec:

```bash
cat > dbt/models/staging/stg_daily_gross_ordered.sql <<'SQL'
{{ config(materialized='view') }}

-- Daily gross ordered amount. NOT Revenue: Revenue is unresolved, owner Finance.
select
    cast(ordered_at as date)  as ordered_date,
    count(*)                  as order_count,
    sum(total_amount)         as gross_ordered_amount
from {{ ref('stg_orders') }}
where status != 'cancelled'
group by 1
SQL

make dbt-check
```

Name the label discipline once, then move on: the column is
`gross_ordered_amount`, not `revenue`. Tonight does not earn the right to rename it.

### Move C — write an Exit Check that is *almost* good

Ask the architect session for an Exit Check for `B-1` ("the model produces one row
per ordered date, excluding cancelled orders"). Most sessions will propose something
like this, and it is worth keeping deliberately:

```bash
# B-1 — the model builds
cd dbt && dbt build --select stg_daily_gross_ordered >/dev/null 2>&1
```

It is deterministic, idempotent, cheap and explainable. It is also not falsifiable
against the behaviour it claims: it fails if the SQL is *invalid*, not if the SQL is
*wrong*. That distinction is what the audit is about to prove.

### Move D — the audit

```bash
taskspec eval-audit tasks/T-20260812-daily-gross-ordered.md \
  --baseline HEAD \
  --mutations 4 \
  --report tmp/d4/audit/gross-ordered.json
echo "exit=$?"
```

`eval-audit` reconstructs the baseline in temporary git worktrees, applies mutations,
and records which evals notice. Read the report as a table, at most eight rows:

```bash
jq -r '.mutations[] | [.id, .description, .verdict] | @tsv' \
  tmp/d4/audit/gross-ordered.json | column -t
```

The two rows to stop on:

- One mutation **KILLED** — e.g. breaking the `group by`, which makes the build fail.
  Point at it: here the gate works.
- One mutation **SURVIVED** — e.g. removing `where status != 'cancelled'`. The SQL is
  still valid, the build still succeeds, the eval still returns 0, and the numbers are
  now wrong. Say the sentence:

> This mutation is a real bug that ships. The eval was green for it. That is the
> hole, and it is not the model's fault — it is the check's.

Do the surviving mutation by hand too, so the room watches it rather than trusting
JSON:

```bash
cp dbt/models/staging/stg_daily_gross_ordered.sql tmp/d4/audit/original.sql
sed -i '' "/where status != 'cancelled'/d" dbt/models/staging/stg_daily_gross_ordered.sql
cd dbt && dbt build --select stg_daily_gross_ordered >/dev/null 2>&1; echo "eval exit=$?"; cd ..
```

`eval exit=0`. Green, with the filter deleted.

### Move E — close the hole by strengthening the eval

The only legitimate fix is to make the eval able to notice. Restore the model, then
rewrite the Exit Check so it asserts the *behaviour* rather than the *build*:

```bash
cp tmp/d4/audit/original.sql dbt/models/staging/stg_daily_gross_ordered.sql
```

New Exit Check for `B-1`:

```bash
# B-1 — cancelled orders are excluded: the model total must be strictly less
#        than the unfiltered total, and must match the filtered total exactly.
cd dbt
dbt build --select stg_daily_gross_ordered >/dev/null 2>&1 || exit 1
duckdb ../warehouse.duckdb -noheader -list -c "
  select case
    when (select round(sum(gross_ordered_amount),2) from main.stg_daily_gross_ordered)
       = (select round(sum(total_amount),2) from main.stg_orders where status != 'cancelled')
    then 'PASS' else 'FAIL' end
" | grep -qx PASS
```

Now repeat the mutation with the new check:

```bash
sed -i '' "/where status != 'cancelled'/d" dbt/models/staging/stg_daily_gross_ordered.sql
# …run the new Exit Check…            -> exit 1   RED. The mutation is now killed.
cp tmp/d4/audit/original.sql dbt/models/staging/stg_daily_gross_ordered.sql
# …run the new Exit Check…            -> exit 0   GREEN on correct work.
```

Two runs, two different colours, one command. **That pair is the deliverable of this
checkpoint** — not the green.

### Move F — re-audit

```bash
taskspec eval-audit tasks/T-20260812-daily-gross-ordered.md \
  --baseline HEAD --mutations 4 --report tmp/d4/audit/gross-ordered-v2.json
```

Every mutation killed. Say the honest caveat: mutation testing has known limits —
equivalent mutants that no test can distinguish, and real cost per mutation. Four
mutations is a discipline, not a certificate.

## Show the evidence

- The five rules, with rule 5 marked.
- The audit table: one `KILLED` row and one `SURVIVED` row.
- The same eval returning **1 on the mutated model** and **0 on the restored one**.
- `git diff` on the Exit Check — the eval got stronger; the model is byte-identical
  to what you built in Move B.

Never show the eval passing without also showing it failing. That pairing is the
entire lesson and the deck's `.src` line depends on it.

## Gate

- One mutation was killed and one survived, on screen, from a real `eval-audit` run.
- The survivor was closed by rewriting the **eval**, and `git diff` proves the model
  did not change to suit it.
- The rewritten eval was run twice: red on broken work, green on correct work.
- A re-audit kills every mutation.
- `make dbt-check` still passes and `stg_daily_gross_ordered.sql` matches Move B.
- The aggregate is still not called Revenue.

## Recovery

If `eval-audit` cannot create a worktree (dirty tree, detached HEAD), commit the
model first on a scratch branch and pass that ref as `--baseline`. If it still fails,
do the whole checkpoint by hand with Move D's `sed` and Move E's rewrite — the manual
version is *more* convincing, and the JSON was only ever a convenience. Label any
pre-generated report **prepared**.

## Sources

- Mutation testing as a fault-based technique with a mutation adequacy score, and
  the killed/survived vocabulary: Y. Jia and M. Harman, *"An Analysis and Survey of
  the Development of Mutation Testing"*, IEEE TSE, 2011.
- High mutation score as evidence of real fault-detection ability, and mutant
  reduction trade-offs: P. Zhang et al., *"Mutant Reduction Evaluation"*, ACM TOSEM,
  2022.
- "The only thing that turns green into a verdict is watching the test fail on the
  broken code": workman.tech, 2026-06-24.
- Deterministic graders for coding agents, and capability evals graduating into
  regression suites: Anthropic, *"Demystifying evals for AI agents"*, 2026.
- Verified usage: `taskspec eval-audit <spec> --baseline <ref> [--mutations N]
  [--report PATH]`, v3.7.0. Token on malformed input: `EVAL_AUDIT=INVALID`.

Next: [`03-the-holdout.md`](03-the-holdout.md).
