# 04 — The authorization chain

## Session

**NEW — Session C.** The developer. It receives **only** its Task-Spec and
`AGENTS.md` — no transcript, no summary of the last three checkpoints, no holdout.
That isolation is what makes the exit code mean anything.

The facilitator drives the chain from a second terminal. The agent never runs `gate`
or `accept` on itself; that is the entire idea of the checkpoint.

## Why this step

Day 3 ended with a graph and a lesson it never got to demonstrate: authority in files
rather than in memory. Tonight the seal actually gets stamped, and the room sees that
"done" is not one decision but **four, held by different parties**:

| Command | Question it answers | Who owns the answer |
| --- | --- | --- |
| `gate --stamp` | *May this be delegated at all?* | a human, before any work |
| `handoff --backend` | *What exactly does the executor receive?* | the format |
| `run --ci` | *Did the declared evals pass in the workspace?* | the machine |
| `accept --stamp` | *Is the work real, independent of the executor's claim?* | a human, after |

`accept` is the one people mis-describe. It does not re-run the tests. It runs **six
gates**, and only stamps `accepted` when they hold.

## Structure

```mermaid
flowchart LR
    A[gate --stamp] --> B[TIER=1 · signed_off written]
    B --> C[handoff --backend]
    C --> D[TaskHandoff v1 · read-only]
    D --> E[Session C executes]
    E --> F[run --ci]
    F --> G[exit 0]
    G --> H[accept --stamp]
    H --> I{Gates A-F}
    I -->|all hold| J[ACCEPTED=1]
    I -->|one fails| K[ACCEPTED=0 · exit 1]

    classDef human fill:#FEF3C7,stroke:#D97706,color:#78350F
    classDef fmt fill:#CFFAFE,stroke:#0891B2,color:#164E63
    classDef machine fill:#DBEAFE,stroke:#2563EB,color:#172554
    classDef good fill:#DCFCE7,stroke:#16A34A,color:#14532D
    classDef bad fill:#FEE2E2,stroke:#DC2626,color:#7F1D1D
    class A,B,H human
    class C,D fmt
    class E,F,G machine
    class I,J good
    class K bad
```

## Do live

### Move A — the pre-gate, and what a Tier means

Tonight's spec is `T-20260812-raw-payments-source`. Gate it **before** stamping, so
the room sees a verdict separately from a signature:

```bash
taskspec gate tasks/T-20260812-raw-payments-source.md; echo "exit=$?"
```

Read the verdict. Then explain the one line a dispatcher actually parses:

```text
TIER=1   HMAC verified            -> unsupervised dispatch is OK
TIER=2   structural only, no key  -> SUPERVISED dispatch ONLY
TIER=3   HMAC mismatch            -> never reached; a hard FAIL happens first
```

Name the thing checkpoint 00 bought: with no repository key this would read `TIER=2`,
and every diff tonight would need a human reader. Now stamp:

```bash
taskspec gate --stamp --require-tier1 tasks/T-20260812-raw-payments-source.md
echo "exit=$?"
git diff tasks/T-20260812-raw-payments-source.md
```

Show the frontmatter diff: `signed_off: false` → `signed_off: true`, plus
`signed_off_by` and `signed_off_at`. Then break it on purpose, once:

```bash
sed -i '' 's/^title: /title: x/' tasks/T-20260812-raw-payments-source.md
taskspec gate tasks/T-20260812-raw-payments-source.md; echo "exit=$?"   # seal breaks
sed -i '' 's/^title: x/title: /' tasks/T-20260812-raw-payments-source.md
taskspec gate tasks/T-20260812-raw-payments-source.md; echo "exit=$?"   # TIER=1 again
```

One character changed the body and the seal noticed. Day 3 promised that; this is the
first time the room has seen it.

### Move B — the handoff is what the executor gets, and nothing more

```bash
taskspec handoff tasks/T-20260812-raw-payments-source.md \
  --backend claude-code --json | tee tmp/d4/receipts/handoff-01.json | jq '.'
```

Read out what is **in** it — id, behaviours, evals, `touches_paths`,
`creates_paths`, the do-not-touch list, the authorization reference — and then what
is **not**: no repository history, no other spec, no holdout, no chat. Say it:

> This is a read-only packet. If the executor needs something that is not in here,
> the spec is wrong, and that is a bug in *our* authoring, not in the agent.

If a spec is unsigned or malformed the tokens are `HANDOFF=REFUSED` /
`HANDOFF=INVALID`; a refused handoff is a correct outcome, not an outage.

### Move C — the PT-BR prompt, and the isolated run

```text
Você é o developer. Sua única fonte é AGENTS.md e este Task-Spec:
tasks/T-20260812-raw-payments-source.md

Faça exatamente o que o spec autoriza — nada além de creates_paths.
Ao terminar, rode o Exit Check e me diga apenas o código de saída.
Não resuma o que você fez.
```

Let it work. One sentence per action on screen, per the output budget.

### Move D — the machine's half of "done"

```bash
taskspec run --ci tasks/T-20260812-raw-payments-source.md; echo "exit=$?"
```

Exit 0. Then say the sentence that keeps the night honest:

> That zero is the machine's half. It is not the answer. Checkpoint 01 produced a
> zero too.

### Move E — the post-gate, all six gates named

```bash
taskspec accept --stamp --gold-sanity tasks/T-20260812-raw-payments-source.md
echo "exit=$?"
```

Walk the gates as they print. Do not skip Gate E; it is the whole night compiled:

| Gate | What it checks | What it defends against |
| --- | --- | --- |
| **A** | evals pass, **re-run by us** | trusting the executor's claim |
| **B** | changed files ⊆ `touches_paths`/`creates_paths`, ∩ do-not-touch = ∅ | satisfying the eval by editing something else |
| **C** | the sign-off HMAC still verifies | making evals pass by weakening them |
| **D** | isolation report from `requires:` — **warns, never blocks** | undeclared network egress on an unattended task |
| **E** | **gold-sanity**: rebuild the baseline in an ephemeral worktree, hold the eval bodies constant, and require the evals to **FAIL** there | an eval that is green even on unbuilt work |
| **F** | format-v4 receipt policy | a claim with no receipt behind it |

Expect **`ACCEPTED=1`** and the frontmatter gaining `accepted: true`, `accepted_by`,
`accepted_at`. Show the diff.

Gate E deserves one sentence spoken slowly: *the tool reconstructs last week's code,
drops tonight's evals into it, and refuses to accept the work unless those evals go
red there.* That is checkpoint 02's discipline, enforced by a command instead of by a
facilitator with a `sed` one-liner.

### Move F — one honest rejection

A chain nobody has watched refuse is a decoration. Break blast radius, deliberately:

```bash
echo "-- touched by nobody's authority" >> dbt/models/staging/stg_orders.sql
taskspec accept --gold-sanity tasks/T-20260812-raw-payments-source.md; echo "exit=$?"
```

Expect **`ACCEPTED=0`**, exit 1, with **Gate B** naming `stg_orders.sql` as outside
the spec's write surface. Point at it: the evals still pass. The work is still real.
It is rejected anyway, because it touched something it was not authorized to touch.

```bash
git checkout dbt/models/staging/stg_orders.sql
taskspec accept --stamp --gold-sanity tasks/T-20260812-raw-payments-source.md
```

Back to `ACCEPTED=1`.

### Move G — the state moves for the first time all week

```bash
taskspec transition T-20260812-raw-payments-source done "accepted at checkpoint 04"
taskspec rebuild-state
grep -A7 '^stats:' tasks/_state.yaml
taskspec ready
```

`done: 1`. The frontier has changed shape without anyone editing an order. Hold one
beat here — this is the moment the graph moves for the first time since Day 3 created
it.

### Moves H, I, J — the three deck slides, 21:50, five minutes

Deck only, no terminal.

1. **Giveaway.** Tonight's skill, `skills/prove-the-oracle/`, free and MIT, with a
   real install line. Say plainly what it cannot do: it does not tell you *what* to
   mutate, and a four-mutation audit is a discipline, not a certificate.
2. **The crank.** The loop consuming the graph in waves. **Say the difference from
   Day 3 out loud: last night's crank clip was pre-recorded; this one ran twenty
   minutes ago, in this repository, in front of you.**
3. **The Bootcamp handoff.** Switch to `presentation/bootcamp.html`. A door, not a
   pitch — no price, no second CTA, five minutes, then straight back to the graph at
   Act 5.

## Show the evidence

- `TIER=1`, then the seal breaking on a one-character edit, then `TIER=1` again.
- The `TaskHandoff` JSON, with what is absent named out loud.
- `run --ci` → exit 0.
- `accept --stamp --gold-sanity` → gates A–F → `ACCEPTED=1` and the frontmatter diff.
- One `ACCEPTED=0` with Gate B naming the unauthorized file.
- `stats:` showing `done: 1` and a recomputed `ready`.

## Gate

- `signed_off: true` was written by `gate --stamp`, and the seal broke on an edit.
- The executor received a handoff packet and nothing else.
- `run --ci` returned 0 in an isolated session.
- `accept` returned `ACCEPTED=1` with gold-sanity on, and the room heard what Gate E
  does.
- One acceptance was **rejected** and the failing gate was named on screen.
- `tasks/_state.yaml` shows `done: 1`.
- `tasks/_metrics.jsonl` now **exists** — do not open it; checkpoint 06 does.
- No file outside `dbt/models/staging/` and `tasks/` changed.

## Recovery

If `--require-tier1` fails because checkpoint 00's key did not take, drop the flag,
show `TIER=2`, and say the supervised-dispatch sentence — do not fake a tier. If
`--gold-sanity` cannot build a worktree it degrades to a warning by design; announce
that Gate E is a warning tonight and that you are therefore keeping the manual
mutation from checkpoint 02 on screen as the substitute proof. If Session C stalls,
the facilitator finishes the file by hand and says so; the chain is the subject, not
the SQL.

## Sources

- The lifecycle and its precondition — *acceptance presupposes the gate; you cannot
  accept work that was never delegate-safe*: `taskspec accept --help`, v3.7.0.
- Gate B as the Goodhart guard, Gate C against post-gate eval weakening, Gate D as
  document-and-warn, Gate E's ephemeral-worktree baseline requirement:
  `taskspec accept --help`, v3.7.0.
- Tier semantics and the machine-readable `TIER=N` line: `taskspec gate --help`,
  v3.7.0.
- Tokens: `TIER=1|2`, `HANDOFF=INVALID|REFUSED`, `ACCEPTED=1|0` —
  `taskspec agent-context`, format version 4.
- Exit codes 0 success · 1 contract/gate/eval failure · 2 usage · 3 runtime floor —
  `taskspec --help`, v3.7.0.
- Why an unattended task with undeclared egress is the exposed surface: RHB reports
  RL post-training raising exploit rates from 0.6% to 13.9% (Thaman, 2026); quoted
  only if the room asks, and always with the date.

Next: [`05-waves.md`](05-waves.md).
