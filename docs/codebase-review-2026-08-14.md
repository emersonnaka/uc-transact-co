# Codebase review and sign-off — 2026-08-14

Full-repository review after the Day 4 execution and the Day 5 build. Scope:
every top-level folder, the root docs, and the verification gates. Gates run
at review time: `make dbt-check` — all checks passed (one expected warning:
unused `intermediate`/`marts` config paths, those layers are participant
work); `make test` — 18 tests, OK.

## Per-folder sign-off

| Folder | State | Verdict |
| --- | --- | --- |
| `infra/postgres/` | `01_schema.sql`, `02_control.sql`, `03_roles.sql` — matches the README description | Signed off |
| `src/transactco/` | `domain/`, `operational/`, `analytical/`, `control/` plus `cli.py`, `config.py` — matches the README documentation table | Signed off |
| `dbt/` | Five staging models (`stg_orders`, `stg_daily_gross_ordered`, `stg_daily_captured_payments`, `stg_orders_payments_reconciled`, `stg_returns_refunds`), `_raw_sources.yml`, `_stg_reconciled.yml`; no intermediate or marts, by design | Signed off |
| `tasks/` | Six specs: five accepted at Tier 1 in `tasks/done/` with signatures and acceptance digests, `T-20260812-daily-grain-decision` open (Finance-owned, no write surface); `_state.yaml` reports `done: 5, ready: 1` | Signed off |
| `storage/specs/` | Five frozen artifacts present (`1-context` … `5-plan-serve`); read-only, untouched by this review | Signed off |
| `skills/` | Three skills with validators; `skills/README.md` accurate | Signed off |
| `scripts/` | `cfo_mcp.py` (read-only CFO MCP server, registered in `.mcp.json`) and `crank.sh` (Day 4 loop driver) — both now named in the root README | Signed off |
| `tests/` | `test_ontology`, `test_contracts`, `test_interview_skill` — all green | Signed off |
| `sessions/` | Runbooks d1–d5; `sessions/README.md` updated in this review to reflect d3/d4 executed and add d5 | Signed off |
| `presentation/` | Decks d1–d5, `about-me`, `bootcamp`, `evals-deep-dive` (untracked); deck images live under `assets/` (untracked) | Signed off |
| `plan/` | `semana.md` header updated in this review; the Day 5 minute-by-minute detail lives in `sessions/d5/` | Signed off |
| `docs/` | Historical PDF brief plus this review | Signed off |
| `tmp/`, `dist/`, `transcripts/`, `.playwright-mcp/` | Session traces and build output; `dist/` and `.playwright-mcp/` added to `.gitignore` in this review | Signed off with notes below |

## Changes made by this review

- `live/` renamed to `sessions/` (`git mv`, history preserved). All path
  references updated: `README.md`, `AGENTS.md`, `plan/semana.md`,
  `skills/harness-scaffold/SKILL.md`, the five decks (`presentation/d1–d5.html`),
  two checkpoint files, and this document. The Makefile's `SCENARIO ?= live`
  is a defect-scenario name, not a path, and was deliberately left alone.
  Frozen surfaces (`storage/specs/`, signed specs in `tasks/done/`) contained
  no `live/` paths, so nothing sealed was touched.
- `README.md` — module table extended to Days 4 and 5; task-graph and staging
  claims brought current; command table gains `up`/`down`/`psql`/`query`/`clean`;
  documentation table gains `d5.html`, `cfo_mcp.py`, `crank.sh`, and this
  review; truth boundaries updated.
- `sessions/README.md` — d3/d4 marked executed, d5 row added, "current module" now
  Day 5.
- `plan/semana.md` — status header brought current; Nights 4–5 pointed at
  their runbooks.
- `.gitignore` — added `dist/` and `.playwright-mcp/`.
- `Makefile` — `defects` added to `.PHONY`.

## Open notes (not fixed here — owner decisions)

- `probe.txt` — a 1-byte tracked file at the repo root, apparently a Day 2
  probe leftover. Candidate for deletion; left in place pending owner
  confirmation.
- `transcripts/` is tracked. If that is intentional session evidence, no
  action; if not, it needs an owner decision before removal.
- Untracked but referenced by docs: `sessions/d5/`, `assets/`,
  `presentation/evals-deep-dive.html`, and the modified `presentation/d5.html`
  are not yet committed. The d5 deck resolves `assets/` through the
  `presentation/assets` symlink.
- `plan/semana.md` body still designs Nights 1–3 only; the header now says so
  explicitly and points to the d4/d5 runbooks rather than pretending coverage.
- `Revenue` remains `unresolved`, owned by Finance. Nothing in this review
  touched that boundary, `src/transactco/control`, the oracle, or the
  injection/scoring surfaces.
