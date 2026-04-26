# Protocol 04 — Sex Differences in Resting-State EEG

> **Prereqs:** [`../docs/01-the-case.md`](../docs/01-the-case.md), [`../docs/04-experimental-design.md`](../docs/04-experimental-design.md), [`../docs/03-data-collection.md`](../docs/03-data-collection.md)
> **Next:** [`../docs/05-analysis-pipeline.md`](../docs/05-analysis-pipeline.md), [`../reports/TEMPLATE.md`](../reports/TEMPLATE.md)
> **Related:** [`../data-collection/markers/send_markers.py`](../data-collection/markers/send_markers.py)

---

> Copy this file to `protocols/<your-name>_04.md` and fill in the TODOs.

## Hypothesis

> _Be specific. "There are differences" is not a hypothesis. Example:
> "Female participants will show higher resting-state alpha power at TP9/TP10
> than male participants, consistent with [citation]."_

## Design

| Block | Duration | Marker | Description |
|-------|----------|--------|-------------|
| BASELINE_EO | 5 min | 1 | Eyes open, fixation |
| BASELINE_EC | 5 min | 2 | Eyes closed |
| LOW_LOAD    | 5 min | 10 | _low-cognitive-load task, e.g., simple breath counting_ |

## Sample

- Target N per group: TODO
- Match age, handedness, time of day

## Important caveats

- Sex differences in EEG literature are small, inconsistent, and confounded
  with skull thickness, hair, time of cycle, and many other variables.
- With N < 30 per group, you are running an underpowered study. Frame results
  as exploratory, report effect size + 95 % CI, do not over-claim.

## Analysis plan

- Spectral power per band per channel
- Group comparison: t-test or Mann-Whitney with multiple-comparison correction
- Effect size: Cohen's d with bootstrap CI
- Optional: classifier on spectral features, LOSO, report chance

---

[**← Prev: 04 — Experimental Design**](../docs/04-experimental-design.md) | [**Next: 05 — Analysis Pipeline →**](../docs/05-analysis-pipeline.md)
