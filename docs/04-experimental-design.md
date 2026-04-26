# 04 — Experimental Design

A few non-negotiables and a few suggestions. The science is yours; the
methodological hygiene is not optional.

---

## Non-negotiables

1. **Baseline.** Every session starts with eyes-open and eyes-closed
   resting-state baselines (≥60 s each). Without these, drift, electrode
   placement, and arousal differences are uncontrolled.
2. **Markers.** Every condition transition must have a timestamped marker.
   Post-hoc segmentation by stopwatch is not acceptable.
3. **Counterbalancing.** When you have multiple conditions, randomize the
   order across participants. Document the schedule.
4. **Pre-registration (lite).** Write down your hypotheses and analysis plan
   *before* you look at the data. Commit it to the repo.
5. **Subject IDs.** No personally identifying information in filenames or
   commits. Use opaque IDs (`sub-001`, `sub-002`, ...).

## Suggested block structure

```
[Baseline EO 60s] → [Baseline EC 60s] → [Cond A 5 min] → [Rest 60s] →
[Cond B 5 min] → [Rest 60s] → [Cond C 5 min] → [Baseline EO 60s]
```

Adjust durations to your hypothesis.

## Sample-size reality check

With consumer EEG and small budgets, you will probably have **5–20
participants**. Plan accordingly:

- Within-subject designs are far more powerful than between-subject for this N.
- Report effect sizes and confidence intervals, not just p-values.
- For ML: use LOSO (Leave-One-Subject-Out) cross-validation and always report
  the chance level.

## Confounds to control for

- Time of day, caffeine, sleep
- Screen brightness (visual evoked confounds)
- Hand movement (motion artifacts in temporal channels)
- Speech (jaw EMG dominates frontal channels)

## What goes in your protocol document

Each protocol in `protocols/` should specify:

- [ ] Conditions and their order
- [ ] Marker codes
- [ ] Stimulus material (link or attach)
- [ ] Per-block duration
- [ ] Inter-block rest length
- [ ] Subject instructions (verbatim)
- [ ] Exclusion criteria for trials/subjects
