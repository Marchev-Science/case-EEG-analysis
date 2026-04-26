# Protocol 02 — Person Identification (EEG Biometrics)

> **Prereqs:** [`../docs/01-the-case.md`](../docs/01-the-case.md), [`../docs/04-experimental-design.md`](../docs/04-experimental-design.md), [`../docs/03-data-collection.md`](../docs/03-data-collection.md)
> **Next:** [`../docs/05-analysis-pipeline.md`](../docs/05-analysis-pipeline.md), [`../reports/TEMPLATE.md`](../reports/TEMPLATE.md)
> **Related:** [`../data-collection/markers/send_markers.py`](../data-collection/markers/send_markers.py)

---

> Copy this file to `protocols/<your-name>_02.md` and fill in the TODOs.

## Hypothesis

> _Example: "A classifier trained on resting-state EEG will identify subjects
> with above-chance accuracy across recording sessions."_

## Design

Same activity recorded across **N ≥ 5** subjects, ideally **two sessions per
subject** at least 24 h apart so train/test sessions are independent.

| Block | Duration | Marker | Description |
|-------|----------|--------|-------------|
| BASELINE_EO | 60 s | 1 | Eyes open |
| BASELINE_EC | 60 s | 2 | Eyes closed |
| TASK        | 5 min | 10 | _your chosen common task_ |
| BASELINE_EO_END | 60 s | 1 | |

## Optional Myers–Briggs / Big Five extension

Collect questionnaire scores (link a validated short form). Analyze whether
within-type subjects cluster in feature space.

## Subject instructions

> _verbatim_

## Analysis plan

- Within-subject vs. between-subject: classifier should generalise across
  *sessions* but identify the *subject*
- Cross-validation: leave-one-session-out, then leave-one-subject-out
  (the latter should drop to chance — that's a sanity check)
- Chance level: 1 / N_subjects
- Report: top-1 and top-3 accuracy, confusion matrix

## Privacy

EEG biometrics are personally identifying. Store with opaque IDs; keep the
ID-to-person mapping outside the repo.

---

[**← Prev: 04 — Experimental Design**](../docs/04-experimental-design.md) | [**Next: 05 — Analysis Pipeline →**](../docs/05-analysis-pipeline.md)
