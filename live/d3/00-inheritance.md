# 00 — Verify the Inheritance

## Session

**No agent.** Terminal only. The first agent session opens at checkpoint 01.

## Why this step

Two nights of evidence are on disk. Tonight consumes the newest of it — the
transform plan — as raw material. Before anything is decomposed, the room sees
that the plan is real, that the rails from Day 2 still stand, and that the
construction site is where Day 2 left it.

## Structure

```mermaid
flowchart LR
    A[Five specs] --> B[Rails standing]
    B --> C[dbt parses]
    C --> D{Inheritance intact?}
    D -->|Yes| E[Decomposition may begin]
    D -->|No| F[Recapture, never substitute]

    classDef evidence fill:#DCFCE7,stroke:#16A34A,color:#14532D
    classDef build fill:#DBEAFE,stroke:#2563EB,color:#172554
    classDef gate fill:#FEF3C7,stroke:#D97706,color:#78350F
    classDef stop fill:#FEE2E2,stroke:#DC2626,color:#7F1D1D
    class A,C evidence
    class B build
    class D gate
    class E evidence
    class F stop
```

Explain briefly:

- Five specs, two of them written by an agent last night under a contract.
- The rails did not evaporate: the agent pair and one passing model are committed.
- Nothing here says what "done" means — that is tonight's whole programme.

## Do live

```bash
git status --short
git rev-parse --short HEAD
make status
ls -la storage/specs/
make dbt-check
test ! -d tasks && echo "tasks absent — correct"
```

Then open the raw material and scroll to its blocked rows:

```bash
sed -n '10,22p' storage/specs/4-plan-transform.md
```

## Show the evidence

Four healthy entities from `make status`. Five specs with their timestamps. The
dbt project parsing with the Day 2 model in place. Then the plan's table, and
specifically rows 7, 9 and 10 — the ones marked BLOCKED with Finance named.

Say:

> Ten items. Every one names its evidence. Three of them are blocked where
> meaning is missing. This is a good plan — and not one line of it tells an
> agent when it is done.

## Gate

- Environment healthy; four entities visible.
- Five specs present and readable, including both Day 2 plans.
- `make dbt-check` passes with the Day 2 staging model.
- `tasks/` does not exist yet — if a rehearsal left one behind, remove it now.
- `taskspec version` prints **3.7.0**. Checkpoint 04 depends on it; a missing CLI
  must surface here at 20:00, not at 21:30 in front of the room.
- The plan's BLOCKED rows were read aloud.

## Recovery

```bash
make up
make land
```

If the two Day 2 plans are missing, stop and restore them before continuing —
they are the only input to tonight's decomposition. Do not substitute an
unlabeled copy; a prepared fallback must be announced as **prepared**.

Next: [`01-plausible-plan.md`](01-plausible-plan.md).
