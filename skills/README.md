# Skills

One skill per night of Semana Engenharia Agêntica. Each is the night's method,
packaged so it works from files in a fresh session — no chat memory, no
transcript, nothing carried in someone's head.

| Night | Skill | Turns this… | …into this | Gate |
| ---: | --- | --- | --- | --- |
| 1 | [`interview-the-system`](interview-the-system/SKILL.md) | a vague question about an unfamiliar system | evidence with provenance, an ontology, owned open questions | `CHECK_INVESTIGATION=PASS` |
| 2 | [`harness-scaffold`](harness-scaffold/SKILL.md) | an understood set of roles and a contract | the structure a harness lives in — every stub empty by design | `CHECK_SCAFFOLD=PASS` |
| 3 | [`spec-before-build`](spec-before-build/SKILL.md) | one ambiguous plan item | one atomic Task-Spec whose exit check answers for itself | `CHECK_TASK_SPEC=PASS` |

They compose in order. Night 1 produces the evidence and, crucially, the list of
things the evidence cannot decide. Night 2 gives that work written authority and a
place to live. Night 3 converts an item into a unit small enough to hand over and
prove finished.

## What every skill in this set holds to

- **A machine-checkable gate.** Each ships a script that exits non-zero and prints
  `CHECK_<NAME>=FAIL`. A skill whose output cannot fail a check is documentation.
- **Read-only by default.** None of them infer permission to mutate data,
  infrastructure, or source. Writing is a separate, granted act.
- **Facts looked up, decisions asked for.** Anything the environment can answer is
  discovered, not asked. Anything involving priority, ownership or business meaning
  is escalated to a named human.
- **Unresolved stays unresolved.** No skill here picks a definition for a term
  someone else owns. `Revenue` is the standing example in this repository: it is
  `unresolved`, owned by Finance, and every skill records the hole rather than
  closing it.
- **Structural validity is not approval.** Passing the gate means the artifact is
  well-formed. A named human still signs the meaning.

## Running the gates

```bash
# night 1 — validate an investigation package
uv run python skills/interview-the-system/scripts/validate_investigation.py \
  investigation.json technical-brief.md trace.jsonl

# night 2 — regenerate and verify harness structure
uv run python skills/harness-scaffold/scripts/scaffold_harness.py \
  --stack dbt,duckdb,fastapi,mcp --dest tmp/harness-scaffold --check

# night 3 — validate one or more Task-Specs
uv run python skills/spec-before-build/scripts/validate_task_spec.py tasks/T-*.md
```

Night 3's validator deliberately mirrors a subset of the `taskspec` CLI (v3.7.0,
MIT) so the skill stands alone on a machine without it. Where the CLI is present,
prefer `taskspec validate`, `taskspec dod` and `taskspec lint` — that is the
reference implementation.
