# Sizing a unit

The unit shrank for a mechanical reason, not a stylistic one: an agent edits files
inside a finite context window. Hand it a whole plan and one of two failures
follows — a sprawling diff nobody can review, or a contradiction at hour two of a
decision made at hour one.

So the unit has to be small enough to close inside one window, and the sizing
field is where that judgment is recorded.

## effort is a decomposition rule, not a label

| effort | Runnable? | Owns a write surface? | Must declare `children`? |
| --- | --- | --- | --- |
| `XS` | yes | yes | no |
| `S` | yes | yes | no |
| `M` | yes | yes | no |
| `L` | yes | yes | no |
| `XL` | **no** | **no** | **yes** |
| `XXL` | **no** | **no** | **yes** |

`XL` and `XXL` are composition nodes. They cannot be executed at all: they exist to
group children and to carry the edges between them. If you find yourself giving an
`XL` a `creates_paths`, the decomposition is not finished.

## The "and" rule

Apply it to the **title**, before writing a single line of the body.

> If the title needs the word "and" to be honest, it is two specs.

A plan item reading *"left join order to payment **and** keep the unpaid orders as
explicit coverage"* makes two promises. Two promises means two units and one edge:
the coverage rule depends on the join existing.

This is the cheapest correction available. Catching it in the title costs a
sentence; catching it after the evals are written costs the whole spec.

## Wide and shallow beats narrow and deep

A shallow graph has more ready units at any moment, so the loop is never starved
waiting on a chain. A dependency chain three deep is a smell: either the split went
too far, or an intermediate unit does too little to deserve its own file.

Aim for a frontier several units wide. Check it rather than assume it:

```bash
taskspec ready      # the units whose depends_on is satisfied
taskspec lint       # the DAG plus write-disjoint groups safe to dispatch together
```

## Two layers, always

Keep a lean index for choosing and one full spec per unit for doing:

```text
tasks/
├── _state.yaml          # one line per unit: id, title, status, path, depends_on
└── T-YYYYMMDD-<slug>.md # the full spec, opened only once its unit is chosen
```

Cheap choosing, expensive doing, never both in the same file. Dependency edges live
in the frontmatter, which is why the index can be derived without opening a single
zone.

## status is not the frontier

These two disagree, and the disagreement is not a bug:

- `_state.yaml`'s `ready:` count is how many units carry `status: ready` — a label a
  human wrote.
- `taskspec ready` prints the units whose `depends_on` is actually satisfied — a
  fact the graph computed.

Six authored units with one blocked and four waiting on an unmet edge gives
`ready: 5` in the index and two rows in the frontier. Read the frontier when you
want to know what can run.

## A blocked unit is never ready

An unresolved decision is not a footnote. Encode it twice:

1. **For machines** — `status: blocked` plus a `blocked_reason`, so no picker offers
   it to an executor.
2. **For humans** — the question in `## Open Questions`, with the owner named.

Leaving a unit blocked is the correct, honest state. It is not a delay, and it is
not a failure to decompose — it is decomposition telling you the truth about where
the work actually stops.
