---
name: spec-before-build
description: Turn one reasonable-looking plan item into a single atomic Task-Spec that states its goal, the behaviour a named human signs, and the machine-runnable proof that answers "am I done?" without asking. Use when a backlog item, plan row, or ticket permits more than one defensible implementation; before handing work to an agent; when "done" is still a matter of opinion; or when a graph of small units must be derived from a large plan. Refuses to invent a definition for any term whose meaning is owned by someone else.
---

# Spec Before Build

A plan enumerates work. It briefs no one. This skill converts one plan item into
the smallest unit an agent can finish and prove finished — and stops when the item
depends on a decision the agent is not entitled to make.

Day 3 of Semana Engenharia Agêntica delivers this skill. It consumes what
[`interview-the-system`](../interview-the-system/SKILL.md) produced (evidence,
ontology, owned open questions) and what the harness contract authorized. It
hands the next day a dependency graph whose units are individually provable.

## Non-negotiable boundaries

- One objective per spec. If the title needs the word "and" to be honest, it is
  two specs.
- Write only inside paths the confirmed contract authorizes. If the plan item
  names a layer the contract does not cover, scope the spec **down** rather than
  widening the contract, and record that reduction in the spec's context.
- Behaviour is signed by the human who owns the decision, not by the agent and
  not by whoever is typing.
- Every behaviour is verified by at least one eval; every eval names at least one
  behaviour. Neither side may dangle.
- An eval is a shell exit code, not a sentence. If a human must read prose to
  decide whether it passed, it is not an eval.
- Never choose a definition for an `unresolved` term. Record the hole, name the
  owner, and leave the unit unable to run.
- Producing a spec is not authorization to execute it. Those are separate gates.

## Workflow

### 1. Establish that the item is ambiguous

Before writing anything, prove the item needs a spec. Ask three fresh sessions to
plan the same item and compare the results, or read the item and name the axes on
which two competent engineers would diverge — which rows qualify, which upstream
source is read, where a label lives.

If nobody can diverge, the item does not need this skill. Say so and stop.

### 2. Size it, then split it

Read [references/sizing.md](references/sizing.md). Assign `effort` from
`XS`/`S`/`M`/`L` for a runnable leaf, or `XL`/`XXL` for a composition node that
declares `children` and owns no write surface.

Apply the sizing rule to the title before the body: split on "and". A plan item
that promises a join *and* a coverage rule is two units with an edge between them.

### 3. Write Intent

State the goal in one sentence and the context in the fewest lines that let a
fresh session act. Cite the evidence the goal rests on.

If Intent grows longer than Behaviour plus Contract combined, you have written a
PRD. Trim it.

### 4. Write Behaviour, and get it signed

Read [references/two-halves.md](references/two-halves.md). Write each behaviour as
`**B-N**` in GIVEN / WHEN / THEN, in the domain's language, with no shell in it.

The test of a behaviour is social, not technical: hand it to the person who owns
the decision and ask whether they can approve it as written. If they cannot read
it, rewrite it.

### 5. Derive the proof

Write one bash function per eval, each naming in a comment the `B-N` it proves.
Then write the Validation Card that makes the binding machine-checkable — every
eval carries `verifies: [B-N]` — plus the retry policy and the agent contract.

Close with an Exit Check: one command combining every eval, returning 0 only when
all of them pass.

**Run the Exit Check before anything is built.** It must fail. A gate that has
never returned non-zero has not been shown to be a gate.

### 6. Declare the boundary and the holes

Fill Guardrails (anti-patterns, do-not-touch) and Operations (open questions).
These are written by a human too — they are the blast radius and the honest
unknowns, not proofs.

Any unresolved decision goes in Open Questions with its owner named. If the
unresolved decision is load-bearing for the unit, the unit is `blocked`, not
`ready`, so no picker will hand it to an executor.

### 7. Validate, then stop

```bash
uv run python skills/spec-before-build/scripts/validate_task_spec.py tasks/T-*.md
```

The validator checks the id format, the sizing rule, the "and" rule, the presence
of both halves, the bidirectional `B-N ⇄ verifies:` binding, exit-check
completeness, and a forbidden-term boundary (`--forbid revenue` by default). It
must finish with `CHECK_TASK_SPEC=PASS`.

Where the `taskspec` CLI (v3.7.0+, MIT) is installed, prefer its own gates —
they are the reference implementation and this validator deliberately mirrors a
subset:

```bash
taskspec validate tasks/T-*.md      # structural and authorization lint
taskspec dod      tasks/T-*.md      # behaviour → eval → exit-check matrix
taskspec lint                       # DAG, collisions, concurrency partition
```

Structural validity is not approval. The spec stays unsigned until a named human
accepts the behaviour.

## Deriving a graph instead of one spec

For a whole plan section rather than a single item, propose a reviewable map
first and generate files only after a human approves it:

1. Write a `TaskPlan/v1` manifest declaring every unit, its `effort`, its write
   surface, its `depends_on`, and any hole it could not resolve.
2. Preview it — this must write nothing.
3. A human sets `approved: true`. Generation materializes exactly the manifest
   and never invents missing work.
4. Validate every generated unit, then read the frontier.

Keep two layers: a lean index for choosing and one full spec per unit for doing.
An agent scanning a hundred full specs to pick its next unit burns the context it
needs to do the work.

## Failure handling

- **Ambiguity survives the spec.** If two engineers still diverge after reading
  it, the behaviour is underspecified. Add a `B-N`, not a paragraph.
- **An eval passes for the wrong reason.** Mutate the model deliberately and
  confirm the eval fails. An eval that cannot fail proves nothing.
- **The contract forbids the write.** Scope down and record it. Do not widen the
  contract to fit the spec.
- **The owner is unavailable.** The spec ships `blocked` with the question and the
  owner. That is a complete, honest outcome — not a delay.
- **The unit will not fit.** Convert it to a composition node with children and
  move the write surface into the leaves.
