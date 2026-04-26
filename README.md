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
- **Data-collection paths**: BlueMuse (Muse 2) or OpenMuse (Athena) → LabRecorder (XDF), or Petal Metrics / Mind Monitor (CSV) — see [`data-collection/README.md`](data-collection/README.md) and [`docs/03-data-collection.md`](docs/03-data-collection.md).
- **XDF file guide**: how to open, inspect, and convert to CSV / pandas / MNE — see [`docs/xdf-format.md`](docs/xdf-format.md).
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
data-collection/  — per-device streaming guides + recorder + markers
code/             — your analysis code (stubs provided)
data/             — your recordings (gitignored)
reports/          — your written report
references/       — papers and reference implementations
```

## Site map (every doc, in reading order)

Every doc has a navigation block at the top with **Prereqs / Next / Related**
links. Use those to wander — this is the index.

### The curriculum (read these in order)
1. [`docs/eeg-primer.md`](docs/eeg-primer.md) — what EEG actually is, in 5 min
2. [`docs/01-the-case.md`](docs/01-the-case.md) — the five research questions, expanded
3. [`docs/02-hardware.md`](docs/02-hardware.md) — Muse 2 vs Athena, picking one
4. [`docs/03-data-collection.md`](docs/03-data-collection.md) — overview of recording paths
5. [`docs/04-experimental-design.md`](docs/04-experimental-design.md) — non-negotiables, baselines, markers
6. [`docs/05-analysis-pipeline.md`](docs/05-analysis-pipeline.md) — what a respectable pipeline contains
7. [`docs/06-deliverables.md`](docs/06-deliverables.md) — what you submit, how it's graded

### Reference docs (read when relevant)
- [`docs/xdf-format.md`](docs/xdf-format.md) — XDF files: structure, loading, conversion to CSV / pandas / MNE
- [`docs/00-original-brief.md`](docs/00-original-brief.md) — original Bulgarian brief (archived)
- [`references/papers.md`](references/papers.md) — papers, libraries, datasets

### Per-device recording walkthroughs
- [`data-collection/README.md`](data-collection/README.md) — pick the right path for your headset
- [`data-collection/muse2-bluemuse/README.md`](data-collection/muse2-bluemuse/README.md) — Muse 2 via BlueMuse (Windows)
- [`data-collection/athena-openmuse/README.md`](data-collection/athena-openmuse/README.md) — Muse Athena via OpenMuse (Python)
- [`data-collection/lab-recorder/README.md`](data-collection/lab-recorder/README.md) — recording streams to XDF
- [`data-collection/petal-metrics/README.md`](data-collection/petal-metrics/README.md) — fallback no-code CSV path
- [`data-collection/markers/send_markers.py`](data-collection/markers/send_markers.py) — LSL marker outlet

### Per-question experiment protocols
- [`protocols/01-ai-vs-human-coding.md`](protocols/01-ai-vs-human-coding.md)
- [`protocols/02-person-identification.md`](protocols/02-person-identification.md)
- [`protocols/03-activity-classification.md`](protocols/03-activity-classification.md)
- [`protocols/04-gender-differences.md`](protocols/04-gender-differences.md)
- [`protocols/05-attention-span.md`](protocols/05-attention-span.md)

### Code & data
- [`code/data_access/README.md`](code/data_access/README.md) — XDF / CSV loaders (stubs for you to fill)
- [`code/notebooks/00-quickstart.ipynb`](code/notebooks/00-quickstart.ipynb) — load + plot one recording
- [`code/notebooks/01-analysis-template.ipynb`](code/notebooks/01-analysis-template.ipynb) — end-to-end skeleton
- [`data/README.md`](data/README.md) — naming convention, privacy, large-file handling

### Reporting
- [`reports/README.md`](reports/README.md) — where your report goes
- [`reports/TEMPLATE.md`](reports/TEMPLATE.md) — report scaffold
