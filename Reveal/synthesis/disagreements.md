# Disagreements and overclaims

The disagreements are more useful than a winner ranking because they expose
where the Day 3 story can become dishonest.

| Question | Strong claim in the raw responses | Evidence-bounded conclusion |
| --- | --- | --- |
| Is Task-Spec already a standard? | “standard protocol” or future “lingua franca” | It is a working open format and reference implementation, not yet an adopted ecosystem standard. |
| Is the seal tamper-proof? | One audience explanation says “tamper-proof.” | HMAC v2 is tamper-evident for covered content with a shared key. It is not identity, non-repudiation, sandboxing, or compromise-proof security. |
| Is acceptance truly independent? | Several cards say the executor can never grade itself. | The lifecycle and acceptance envelope are separate, and the POST gate reruns evidence without trusting the report. The format does not cryptographically prove a different human or machine invoked it. |
| Can it run without humans? | One thesis says “without a human in the loop.” | Bounded Tier-1 execution may be unattended, but humans still own intent, semantic decisions, authorization, high-consequence review, and exceptions. Tier 2 is supervised-only. |
| Is one task always one PR? | Several models call it “one PR-sized change.” | That is a useful heuristic. The canonical rule is one coherent done-condition that fits one fresh executor context and bounded write surface. |
| Is portability proved? | Some answers imply any named model works interchangeably today. | Handoffs, adapters, schemas, and conformance mechanics exist. The real multi-engine CI matrix is still P0 work. |
| Do evals prove truth? | “Bash exit code IS done.” | A passing Exit Check establishes configured local acceptance. It does not prove semantic correctness, deployment, production health, or business truth. |
| Will A2A or MCP adopt it? | Several forecasts expect Task-Spec to become their payload. | Plausible but unproved. They may integrate Task-Spec, translate it, or standardize a competing contract. |

## Presentation rule

Never reveal only the enthusiastic sentence. Pair each model's strongest claim
with its strongest limitation. The credibility of Day 3 comes from showing that
Task-Spec knows its own boundary.
