# Protocol 03 — Activity Classification

> **Prereqs:** [`../docs/01-the-case.md`](../docs/01-the-case.md), [`../docs/04-experimental-design.md`](../docs/04-experimental-design.md), [`../docs/03-data-collection.md`](../docs/03-data-collection.md)
> **Next:** [`../docs/05-analysis-pipeline.md`](../docs/05-analysis-pipeline.md), [`../reports/TEMPLATE.md`](../reports/TEMPLATE.md)
> **Related:** [`../data-collection/markers/send_markers.py`](../data-collection/markers/send_markers.py)

---

> Copy this file to `protocols/<your-name>_03.md` and fill in the TODOs.

## Hypothesis

> _Example: "EEG features can distinguish four cognitively distinct
> activities (gaming, shopping, market analysis, IQ test) above chance
> within-subject."_

## Design

| Block | Duration | Marker | Activity |
|-------|----------|--------|----------|
| BASELINE_EO | 60 s | 1 | |
| BASELINE_EC | 60 s | 2 | |
| GAME       | 5 min | 10 | _specify game_ |
| REST       | 60 s | 99 | |
| SHOP       | 5 min | 20 | Online shopping task |
| REST       | 60 s | 99 | |
| MARKET     | 5 min | 30 | Financial-market analysis |
| REST       | 60 s | 99 | |
| IQ_TEST    | 5 min | 40 | Reasoning test (Raven, etc.) |
| BASELINE_EO_END | 60 s | 1 | |

Counterbalance the four activity orders (Latin square if N permits).

## Stimuli

- Game: _link / version_
- Shopping site: _link_
- Market data tool: _link_
- IQ test: _link_

## Subject instructions

> _verbatim_

## Analysis plan

- 4-class within-subject classifier
- LOSO across subjects
- Chance = 25 %
- Report per-class precision/recall, confusion matrix
- Sub-epoch length: _e.g., 5 s windows, 2.5 s overlap_
