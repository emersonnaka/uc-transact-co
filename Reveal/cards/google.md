# Google Gemini — the eval decides done

**Model:** `gemini-pro-latest` · **Confidence:** 85/100

> The eval decides “done,” not the agent's prose report.

**What it saw.** Task-Spec separates the definition of work from the engine
that performs it, using executable checks and a sealed authorization envelope.

**Best contribution.** This is the simplest audience-facing explanation of the
transition from narrative completion to observable completion.

**Important restraint.** Its raw explanation calls the contract
“tamper-proof” and a “standard protocol.” The repository supports
tamper-evidence, not tamper-proof security, and Task-Spec is not yet an adopted
ecosystem standard.

**Use in the room.** Reveal this first: it gives the audience the most digestible
mental model, followed immediately by the correction above.
