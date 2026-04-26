# case-EEG-analysis

An open-ended EEG case study for graduate research. You are given two consumer EEG
headsets (Muse 2 and Muse Athena), a set of research questions, and the freedom to
design your own experiments, collect your own data, and build your own analysis
pipelines.

This repo is a **scaffold**, not a finished product. It tells you what to do, gives
you the protocols and data-collection tooling, and leaves the science to you.

---

## The case

Pick one (or more) of the following research questions and run a study end-to-end:

1. **Brain activity while using AI** — does coding with an AI assistant produce a
   different EEG signature than coding alone, or watching a sports broadcast?
2. **Person identification** — can the same activity, recorded across people, be
   used to identify the individual? Optionally cross-reference Myers–Briggs type.
3. **Activity classification** — distinguish video gaming, online shopping,
   financial-market analysis, and an intelligence test from EEG alone.
4. **Sex differences in resting-state EEG** — at rest or during low-activity
   tasks, are there reliable male/female differences?
5. **Attention span** — short vs. long videos, instructional vs. entertainment.

See [`docs/01-the-case.md`](docs/01-the-case.md) for expanded prompts.
The original project brief is archived at [`docs/00-original-brief.md`](docs/00-original-brief.md).

## What's provided

- **Hardware**: Muse 2 (4 EEG channels, 256 Hz) and Muse Athena (extended channels). See [`docs/02-hardware.md`](docs/02-hardware.md).
- **Data-collection paths**: LSL + LabRecorder (XDF) and Petal Metrics / Mind Monitor (CSV) — see [`docs/03-data-collection.md`](docs/03-data-collection.md).
- **Protocol templates**, one per research question, in [`protocols/`](protocols/).
- **Code stubs** in [`code/`](code/) — empty modules, you fill them in.
- **Report template** in [`reports/TEMPLATE.md`](reports/TEMPLATE.md).
- **References**, including a working Python EEG pipeline you may study for ideas: see [`references/papers.md`](references/papers.md).

## What we expect from you

A short research report (`reports/<your-name>.md`), reproducible code under
`code/`, and your raw recordings under `data/raw/` (or a link to them if too
large for git).

Grading rubric and deliverables: [`docs/06-deliverables.md`](docs/06-deliverables.md).

## Getting started

1. **New to EEG?** Read [`docs/eeg-primer.md`](docs/eeg-primer.md) first (5 min).
2. Then [`docs/01-the-case.md`](docs/01-the-case.md) → [`docs/02-hardware.md`](docs/02-hardware.md) → [`docs/03-data-collection.md`](docs/03-data-collection.md).
3. Pair your headset and record a 60-second baseline.
4. Open [`code/notebooks/00-quickstart.ipynb`](code/notebooks/00-quickstart.ipynb) and verify you can load and plot it.
5. Pick a research question, copy the matching `protocols/0X-*.md`, and adapt it.
6. Collect, analyse, write up.

## Repo layout

```
docs/             — case description, hardware, methods, deliverables
protocols/        — per-question experimental protocol templates
data-collection/  — LSL config, marker scripts, alt-app instructions
code/             — your analysis code (stubs provided)
data/             — your recordings (gitignored)
reports/          — your written report
references/       — papers and reference implementations
```
