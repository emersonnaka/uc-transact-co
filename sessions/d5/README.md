# Day 5 — live runbook

One checkpoint. The TransactCo use case is closed here and nowhere else in the
night; everything after it on the deck is the method lifted off TransactCo and
put under other work.

| # | Checkpoint | Budget | Deck slide before it |
| --- | --- | --- | --- |
| `01` | [Close the CFO question](01-close-the-cfo-question.md) | 8 min | **The CFO question** |

## What is already true before the night starts

Nothing in checkpoint `01` builds anything. All of it was finished and committed
in advance, on purpose, so the segment cannot run long:

- five specs authored, gated at Tier 1, executed and accepted through
  `taskspec accept` with gates A–E — one commit each
- `tasks/_state.yaml` reports `done: 5`
- the sealed holdout is green and bound by attempt id to the accepted run
- `make dbt-check` and `make test` return 0, working tree clean
- `scripts/cfo_mcp.py` is registered as `transactco-cfo` in `.mcp.json`

The only thing that happens live is the question.

## The boundary that has to survive

`T-20260812-daily-grain-decision` stays open. It declares no write surface, so
the crank cannot execute it — a decision is not a file. If someone asks whether
the loop could just finish it, the answer is no, and that is the point of the
whole week rather than an unfinished task.

## Preflight

```bash
grep -A7 '^stats:' tasks/_state.yaml      # done: 5
git status --short dbt tasks scripts      # empty
make dbt-check                            # exit 0
```

Scope the status check to `dbt tasks scripts`. That is the accepted work, and it
is what has to be clean. The deck and these runbooks live outside it and are
routinely uncommitted on the night.

If the MCP server does not attach in the session, checkpoint `01` carries a
stdio fallback that runs the identical code path. Label it as a fallback out
loud if you use it.
