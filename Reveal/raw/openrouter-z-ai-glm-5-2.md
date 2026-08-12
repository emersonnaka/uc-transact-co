# Task-Spec 3.6.0 — Independent Technical Evaluation

## A. METADATA

- **run ID:** unassigned
- **provider:** openrouter (as reported by harness workstation)
- **exact model:** z-ai/glm-5.2 (from workstation `Model` field; identity not independently verifiable from within the session)
- **date:** 2026-08-12
- **web research used:** yes (repository discovery only; all substantive evidence from pinned commit `ad511d3` primary sources)
- **sources accessed:** README.md, spec/task-spec-v3.md, docs/concepts/decomposition.md, docs/concepts/eval-driven-development.md, docs/concepts/conformance-levels.md, docs/concepts/effort-gate.md, docs/concepts/six-zones.md, docs/guides/multi-harness.md, docs/runbooks/dark-factory-as-task-spec.md, docs/examples/task-plan.yaml, docs/examples/task-handoff.json, release/evidence.json, TODO.md

---

## B. REVEAL CARD

- **Central thesis:** Task-Spec makes the unit of agentic work a self-verifying, tamper-evident, vendor-portable contract where executable evals — not agent self-report — decide done.
- **Killer insight:** The spec carries its own definition of done; the executor never grades itself.
- **Five breakthroughs:**
  1. Executable success criteria as the contract's moat — bash exit code IS done
  2. Bidirectional B-N ⇄ eval traceability enforced by the validator
  3. PRE-gate seal + POST-gate acceptance as architecturally separate moments
  4. Credential-free TaskHandoff/v1 decoupling executor choice from contract
  5. Conformance L0/L1/L2 making "any conformant executor" testable, not asserted
- **Ecosystem role:** The format and lifecycle layer — declares and verifies one atomic unit; scheduling, sandboxing, and model execution are explicitly external.
- **6–12 month bet:** If the real multi-engine CI matrix ships and sealed holdouts land, Task-Spec becomes the portable interchange format between heterogeneous agent runtimes.
- **Greatest limitation:** Structural validation proves format conformance and eval mechanics — it cannot prove semantic correctness, and the real multi-engine evidence matrix is still unfinished.
- **Confidence score:** 78

---

## C. ATOMICITY COMPARISON

| Dimension | TODO | Issue | Prompt | Workflow step | Task-Spec |
|---|---|---|---|---|---|
| Write surface bounded | No | No | No | Sometimes | Yes — `touches_paths` ∪ `creates_paths` |
| Done condition | Hope | Status field | Agent judgment | Next step reached | Executable bash Exit Check |
| Verification | None | Human review | Human review | Pipeline status | Runnable evals, POST-gate rerun |
| Dependency graph | No | Sometimes | No | DAG in engine | `depends_on` DAG, validated |
| Authority sealed | No | No | No | Engine auth | HMAC v2 envelope |
| Blocked as structural | No | Label | No | No | `status: blocked` + `blocked_reason` hole |
| Vendor portability | N/A | Tracker-bound | Model-bound | Engine-bound | Markdown + YAML + bash |
| Acceptance independent | No | Human close | No | Engine | Separate POST-gate, not executor-written |

---

## D. BACKEND ALIGNMENT

| layer | responsibility | examples | owned by Task-Spec | NOT owned by Task-Spec |
|---|---|---|---|---|
| Format | Declare one atomic unit | Six zones, frontmatter, B-N | Yes — normative spec + validator | — |
| Verification | Prove done mechanically | Eval functions, Exit Check | Yes — evals + POST-gate | Semantic correctness beyond eval |
| Authorization | Seal authority before delegation | HMAC v2, sign-off tiers | Yes — PRE-gate stamps envelope | Per-author identity, key rotation |
| Transfer | Hand off to any executor | TaskHandoff/v1 | Yes — credential-free contract | Model invocation, worker scheduling |
| Decomposition | Turn intent into gateable atoms | TaskPlan/v1, depends_on | Yes — DAG + blocked holes | Priority ordering, parallel dispatch |
| Conformance | Certify executors | L0/L1/L2, ref-executor | Yes — suite + reference | Fleet reliability evidence |
| Execution | Run the model | Codex, Claude, Kimi, Grok | No | Model selection, cost metering |
| Scheduling | Fleet across DAG | anthive, taskship | No | Worker pools, priority queues |
| Sandbox | Isolate execution | E2B, Daytona, worktrees | Declares `sandbox_type` only | Network/process isolation enforcement |
| Tracking | Issue/PR lifecycle | GitHub, Linear | Backlink via `tracker_ref` only | Issue workflow, PR creation |

---

## E. FORECAST

| prediction | confidence | confirmation signal | failure condition |
|---|---|---|---|
| Model routing converges on a Task-Spec-agnostic dispatch layer where the handoff backend is an open string, not a vendor lock | 65% | ≥3 engines pass L2 conformance on the same fixture set in CI | Vendors resist the open interface; conformance suite stays single-engine |
| Persistent agents adopt Task-Spec as the task-pickup boundary, with blocked→ready transitions driving human-in-the-loop | 55% | A2A alignment (TODO P2-2) ships and ≥1 A2A dispatcher consumes Task-Spec natively | A2A Tasks and MCP Tasks subsume the format without adopting its eval-gate discipline |
| Sandboxed execution becomes spec-declared (environment contract, TODO P2-4) rather than executor-implicit | 60% | `setup`/`teardown` hooks guaranteed by dispatcher before evals run | Sandboxing vendors (E2B, Daytona) optimize for their own task format instead |
| Independent verification via sealed holdout evals (TODO P1-1) becomes the differentiator for unattended dispatch | 50% | Format v4 ships with HMAC-sealed second eval block; ≥1 fleet uses it in production | Sealed holdouts prove impractical or gameable in practice; Goodhart guard insufficient |

---

## F. CURRENT VERSUS ROADMAP

**Implemented or demonstrated today (evidence at `ad511d3`):**

- TaskPlan/v1 with explicit `depends_on` dependency graph and `parent:` edges (docs/examples/task-plan.yaml, decomposition.md)
- XS/S/M/L executable leaves + XL/XXL composition nodes (effort-gate.md, spec)
- One coherent done-condition per leaf, enforced by Exit Check (spec)
- Bounded write surfaces via `touches_paths` + `creates_paths` + Do-Not-Touch (spec, six-zones.md)
- B-N Given/When/Then behaviors with bidirectional traceability validated by `validate-task-spec.sh` (spec Zone 2)
- `status: blocked` + `blocked_reason` as structural elements, withheld from gate (decomposition.md)
- Effort sizing, `budget_iterations`, token/wall-clock budgets, authority tiers (effort-gate.md, README)
- PRE-gate: `safe-to-delegate.sh` / `gate --stamp` HMAC v2 seal (README, conformance-levels.md)
- Credential-free TaskHandoff/v1 (docs/examples/task-handoff.json, multi-harness.md)
- POST-gate: `accept-task.sh` → `accepted: true`, separate from executor (README, spec)
- Portability across Codex / Claude / Kimi / Grok adapters (adapters/engines/)
- Conformance L0/L1/L2 with reference executor `ref-executor.sh` (conformance-levels.md)
- A2A TaskState mapping (conformance-levels.md)
- Release evidence: `make check` pass, experience suite 26/26, npm pack dry-run pass (release/evidence.json)
- Honest boundaries: not a hosted service, not a fleet scheduler, not production evidence (release/evidence.json, README trust table)
- HMAC does not prove identity; `accepted: true` does not prove deployment (README trust boundaries)

**Unproven, unfinished, or planned (TODO.md + release/evidence.json):**

- Real multi-engine CI matrix (≥2 real engines in GitHub Actions) — P0-1, foundation landed but real-engine layer unfinished
- Sealed holdout evals (format v4) — P1-1, roadmap
- Graded `check_type` (model-judged rubric) — P1-2, roadmap
- Mutation matrix for eval red-forcing — P1-3, roadmap
- Key management: rotation, per-author identity, remote verification — P1-4, roadmap
- Security pass for untrusted text sanitization + sandbox doctrine — P1-5, roadmap
- MCP server exposing engine as tools — P2-1, roadmap
- A2A alignment as verifiable payload — P2-2, roadmap
- Tracker adapters via MCP — P2-3, roadmap
- Environment contract (setup/teardown hooks) — P2-4, roadmap
- npm/curl installs pending `v3.6.0` tag publication (release/evidence.json: `pending_release_tag`)
- Live research provider support — fake adapters only; live providers not advertised (release/evidence.json)

---

## G. VERDICT

**Strongest argument:** Task-Spec makes the eval — not the agent — the arbiter of done, and separates the three moments (authorize, execute, accept) with distinct responsibilities and tamper-evident seals. This is a real structural innovation: every other task format is readable; this one is executable and self-verifying. Combined with vendor-neutral portability (markdown + YAML + bash) and testable conformance levels, it addresses the core trust problem of autonomous agents: how do you know the work is actually done?

**Strongest counterargument:** Structural validation proves format conformance and eval mechanics, not semantic correctness. The format itself acknowledges this (Goodhart's Law guard, "cannot make a weak oracle wise"). The real multi-engine CI matrix — the evidence that would turn "vendor-neutral" from design property to proven fact — is unfinished (TODO P0-1). Without it, portability is an architectural claim validated only by the reference executor and fake adapters. Sealed holdouts, graded evals, and mutation testing — the protections that would harden the eval oracle against gaming — are all roadmap items (P1-1 through P1-3). The format's honesty about its limitations is admirable, but honesty does not close the gap.

**Missing evidence:**
- No published results from ≥2 real engines (Claude, Codex) executing the same fixture set in CI
- No sealed holdout evals in production use
- No graded check_type implementation
- No fleet-scale acceptance rate or cost-per-green data (P3-3)
- No evidence that conformance L2 holds under adversarial or production-scale conditions

**Final conclusion:** Task-Spec 3.6.0 is a well-designed, honestly-bounded format that introduces a genuinely novel primitive: the self-verifying atomic task with separated authorization, execution, and acceptance. Its architecture is sound and its self-awareness about limitations is exceptional. However, its thesis — that atomic tasks become a fundamental unit of work in the agentic ecosystem — rests on evidence that is still structural and single-engine. The breakthrough is real; the proof is incomplete. If the P0-1 multi-engine matrix and P1-1 sealed holdouts ship with positive results within 6–12 months, the thesis gains strong support. Until then, it is a promising, well-reasoned bet, not a proven one.

---

## H. AUDIENCE EXPLANATION (~45 seconds spoken)

Task-Spec is a file format for giving AI coding agents work to do — but with a twist. Instead of just describing what you want, each task carries its own test. When the agent says "I'm done," the task runs its own checks to prove it. And the person who checks the result isn't the agent — it's a separate gate that re-runs the tests and verifies nothing went out of bounds.

Think of it like a contract: it says what files you can touch, how many tries you get, what "done" looks like as a runnable script, and who authorized it. The same contract works whether you hand it to Claude, Codex, Kimi, or any other tool. The agent doesn't grade itself.

It's not a scheduler, it's not a sandbox, and it doesn't run models. It's the contract layer — one atomic unit of work that any engine can pick up, execute, and prove. The honest limitation: the tests can be gamed, the seal proves the contract wasn't tampered with but not who you are, and the real proof that this works across different AI engines is still being built. It's a strong idea with an honest gap between design and evidence.
