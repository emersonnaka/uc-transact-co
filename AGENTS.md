# TransactCo — Agent Instructions

Brownfield commerce case for Semana Engenharia Agêntica. The numbers here must
earn trust: physical measurements are evidence, business meaning is owned by
humans. `Revenue` is formally **unresolved** (owner: Finance) — no agent may
choose a definition for it.

## Ground rules (all agents, all engines)

- Postgres access is read-only via `analytics_ro`; DuckDB `raw.*` mirrors
  `public.*`. Discover commands with `make help`.
- Approved context lives in `storage/specs/` — read-only; never overwrite it.
- Never touch `src/transactco/control`, the oracle, or injection/scoring
  surfaces (`make inject`, `make reveal`, `make score`).
- Any semantic decision — what counts as Revenue, which statuses, which
  timestamp — halts the work and escalates to the named owner.
- Verification is a gate you run (`make dbt-check`, `make test`), never a
  self-declaration.

## Agents

### architect — judgment, no hands
- job: reviews every plan before it runs
- reads: the repo, the confirmed contract, storage/specs/*
- tools: read, grep, make psql-ro
- bash: denied — verdicts, not edits
- writes: nothing
- stops: any semantic decision — Revenue meaning is owned by Finance

### developer — execution, bounded hands
- job: builds what the approved plan enumerates
- reads: the contract, the plans, the diff
- tools: read, write, bash — inside the contract only
- writes: dbt/models/staging/ and nothing else
- done: make dbt-check passes, then claim it — never before

<!-- Entries below are written live at checkpoint live/d2/03-agent-pair.md,
     against the harness contract confirmed at checkpoint 02. -->
