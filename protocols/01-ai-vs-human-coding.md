# Protocol 01 — AI vs. Human Coding (vs. Neutral Baseline)

> **Prereqs:** [`../docs/01-the-case.md`](../docs/01-the-case.md), [`../docs/04-experimental-design.md`](../docs/04-experimental-design.md), [`../docs/03-data-collection.md`](../docs/03-data-collection.md)
> **Next:** [`../docs/05-analysis-pipeline.md`](../docs/05-analysis-pipeline.md), [`../reports/TEMPLATE.md`](../reports/TEMPLATE.md)
> **Related:** [`../data-collection/markers/send_markers.py`](../data-collection/markers/send_markers.py)

---

> Copy this file to `protocols/<your-name>_01.md` and fill in the TODOs.

## Hypothesis

> _Write a directional hypothesis. Example: "Frontal theta power will be higher
> during AI-assisted coding than during solo coding due to increased
> meta-cognitive load."_

## Design

| Block | Duration | Marker code | Description |
|-------|----------|-------------|-------------|
| BASELINE_EO | 60 s   | 1   | Eyes open, fixation cross |
| BASELINE_EC | 60 s   | 2   | Eyes closed |
| WATCH_NEUTRAL | 5 min | 10 | Sports broadcast, neutral teams |
| REST_1      | 60 s   | 99  | Rest |
| CODE_SOLO   | 8 min  | 20  | Solve programming task without AI |
| REST_2      | 60 s   | 99  | Rest |
| CODE_AI     | 8 min  | 30  | Same task class, with AI assistant |
| BASELINE_EO_END | 60 s | 1 | Eyes open closing baseline |

Counterbalance order of `WATCH_NEUTRAL`, `CODE_SOLO`, `CODE_AI` across subjects.

## Stimuli & task material

- Sports broadcast clip: _link / file_
- Solo coding prompt: _link / file_
- AI coding prompt: _link / file_ (must be a *different* problem of equivalent difficulty)
- AI tool used: _Copilot / Claude / Cursor / other_

## Subject instructions (verbatim)

> _Write what you will read out loud to the participant. Same for everyone._

## Inclusion / exclusion

- TODO

## Analysis plan (pre-registered)

- Pre-processing: _band-pass, notch, artifact handling_
- Features: _e.g., band power per condition, frontal theta, parietal alpha_
- Statistics: _within-subject paired comparison, multiple-comparison correction_
- ML (optional): _model, CV scheme, chance level_

## Notes

- TODO
