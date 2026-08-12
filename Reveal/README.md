# Reveal — multi-LLM collection

`Reveal/raw/` is the immutable inbox for the Day 3 Task-Spec research. Each
model receives the same [`prompt.md`](prompt.md), unchanged.

## Collection rule

1. Paste [`prompt.md`](prompt.md) unchanged into a fresh model session with web
   or repository access enabled.
2. The model derives its output filename from its provider and model name.
3. If the model can write files, it writes exactly one file under `Reveal/raw/`.
4. If it cannot write files, save its complete labeled response at the path it
   returns, or paste it back into the orchestrator session for capture.
5. Record the exact model identifier and change the manifest status to
   `captured` only after the raw file exists.

Do not edit a captured raw response. Corrections and comparisons belong under
`normalized/`, `cards/`, or `synthesis/` after every model has responded.

## Current collection

The first collection is synthesized: nine submissions produced eight usable
analyses and one source-access failure. Start with
[`synthesis/consensus.md`](synthesis/consensus.md), then review the
[`cards/`](cards/) and [`synthesis/agenda.md`](synthesis/agenda.md). The raw
files remain unchanged and are sealed by [`raw.sha256`](raw.sha256).

## Layout

```text
Reveal/
├── prompt.md            # canonical prompt used by every model
├── manifest.yaml        # run slots, model identity, and capture state
├── raw/                 # untouched model responses
├── normalized/          # comparable structured extracts, created later
├── cards/               # presentation cards, created later
└── synthesis/           # consensus, disagreements, and agenda, created later
```

The models must not inspect other files in `raw/`. This prevents later runs
from copying or adapting earlier answers.
