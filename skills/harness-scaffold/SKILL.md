---
name: harness-scaffold
description: Regenerate the structural skeleton of a harness — agent role stubs, KB layout, and per-stack rule files — for a repository's stack, in seconds. Use when a harness structure must be (re)created from artifacts on disk, after the roles and contract are already understood and never before. Produces structure only: every stub is intentionally empty, and the scaffold grants no authority.
---

# Harness Scaffold

One run regenerates the harness structure the team already understands:
`agents/` role stubs, `kb/<stack>/` knowledge-base placeholders, and
`rules/<stack>.md` rule stubs, plus a manifest. It is the automation of the
hand-written work from `live/d2/03-agent-pair.md` — faster, never smarter.

Day 2 of Semana Engenharia Agêntica delivers this skill. It follows Day 1's
[`interview-the-system`](../interview-the-system/SKILL.md), which supplies the
evidence and the owned questions the harness is built around, and it precedes
Day 3's [`spec-before-build`](../spec-before-build/SKILL.md), which writes the
units that execute inside the authority this structure holds.

## Boundaries

- Writes ONLY under `tmp/harness-scaffold/`. Never touches `AGENTS.md`,
  `CLAUDE.md`, `dbt/`, `src/`, or `storage/`.
- Grants no authority. The harness contract does that; this skill only lays
  out where the pieces of a harness live.
- Every generated file is a stub, empty by design. What fills a stub —
  grounded KB content, tuned doctrine — is human work measured in hours, not
  a generator's output.
- Requires no chat memory: everything it needs is on disk.

## Method

1. Read the stack from the request (default for this repo:
   `dbt,duckdb,fastapi,mcp`).
2. Run the generator:

   ```bash
   uv run python skills/harness-scaffold/scripts/scaffold_harness.py \
     --stack dbt,duckdb,fastapi,mcp --dest tmp/harness-scaffold
   ```

3. Validate the structure:

   ```bash
   uv run python skills/harness-scaffold/scripts/scaffold_harness.py \
     --stack dbt,duckdb,fastapi,mcp --dest tmp/harness-scaffold --check
   ```

4. Report: the generated tree, the manifest summary, and the reminder that
   every stub is empty. Open one stub if asked — show, do not narrate.

## Human stop

The scaffold is structure, not content, and it is not authorization. Building
anything inside it still requires the confirmed harness contract, and every
semantic decision (Revenue included) stays with its named owner.
