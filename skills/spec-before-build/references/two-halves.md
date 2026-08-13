# Two halves of done

"Done" has two readers, and they cannot read each other's half.

A stakeholder cannot review `[[ $(dbt parse) ]]`. A shell cannot run "the numbers
should look right". So a spec carries both halves, and each is written for its
own reader.

| Half | Zone | Reader | Form |
| --- | --- | --- | --- |
| Behaviour | 2 | the human who owns the decision | `B-N` in GIVEN / WHEN / THEN, no shell |
| Proof | 3 | the machine | bash functions, one exit code |

## Write the behaviour first

The order is not stylistic. An eval written before its behaviour is an assertion
somebody invented; an eval derived from a signed behaviour inherits its meaning.

```markdown
## Behavior

- **B-1** — GIVEN raw orders carrying six distinct statuses
  WHEN the daily aggregate sums by the order timestamp
  THEN orders with status `cancelled` are excluded from the total.
- **B-2** — GIVEN the aggregate is published
  WHEN anyone reads its name or its labels
  THEN it is described by its physical basis and never by a contested business term.
```

Heading note: `taskspec batch` emits **`## Behavior`** (singular). Some written
material uses `## Behaviors`. Both validate; prefer the singular so a
hand-written spec and a generated one look identical side by side.

The test is social. Hand `B-1` to the person who owns the decision and ask if they
can approve it as written. If they need it explained, it is not yet a behaviour.

## Then derive the proof

Each eval names the behaviour it exists to prove:

```bash
# eval-1 (verifies B-1): the model exists and the project parses
eval_1() { make dbt-check >/dev/null 2>&1; }

# eval-2 (verifies B-1): the exclusion is expressed in the model
eval_2() { grep -q "cancelled" dbt/models/staging/stg_daily_gross_ordered.sql; }

# eval-3 (verifies B-2): the boundary holds — no output carries the contested name
eval_3() { ! grep -ril "revenue" dbt/models/ | grep -q . ; }
```

## The binding, written down

The comment above each eval is a convention. The Validation Card is the contract:

```yaml
success_criteria:
  - id: eval_1
    description: The model exists and the dbt project parses
    runnable: bash
    terminal: true
    expected_duration_sec: 20
    verifies: [B-1]
  - id: eval_2
    description: Cancelled orders are excluded in the model
    runnable: bash
    terminal: true
    expected_duration_sec: 1
    verifies: [B-1]
  - id: eval_3
    description: No output under the write surface carries the contested name
    runnable: bash
    terminal: true
    expected_duration_sec: 1
    verifies: [B-2]
```

**Neither side may dangle.** Every `B-N` is claimed by at least one eval — an
unverified behaviour is a hole. Every eval names at least one `B-N` — an eval with
no `verifies:` is testing something the spec never promised, which is scope creep
wearing a passing test.

Both directions are machine-checkable, which is the whole point:

```bash
uv run python skills/spec-before-build/scripts/validate_task_spec.py <spec>
taskspec dod <spec>     # where the CLI is installed
```

## What makes an eval terminal

1. **Deterministic** — the same input gives the same answer. No unretried network.
2. **Idempotent** — running it twice gives the same result and changes nothing.
3. **Cheap before expensive** — order them so the fast failure comes first.
4. **Explainable** — one line saying why it exists.
5. **Falsifiable** — break the thing on purpose and watch the eval fail. An eval
   that cannot fail proves nothing, and this is the check people skip.

## The exit check

One command. It returns 0 only when every eval passes:

```bash
eval_1 && eval_2 && eval_3
```

Run it **before** the build and confirm it fails. A gate whose failing state has
never been seen is a claim, not a gate — and this course's entire argument is that
evidence outranks claims.
