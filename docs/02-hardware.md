# 02 — Hardware

You have access to two headsets. They share an SDK family but differ in
electrode count and signal quality.

---

## Muse 2

| Spec              | Value                                |
|-------------------|--------------------------------------|
| EEG channels      | 4 (TP9, AF7, AF8, TP10)              |
| Sample rate       | 256 Hz                               |
| Other sensors     | PPG (3 ch @ 64 Hz), Accel, Gyro      |
| Connection        | BLE                                  |
| Reference         | Fpz                                  |

**Strengths.** Cheap, well-documented, large open community.
**Weaknesses.** Sparse electrode coverage — frontal + temporal only. No
midline / occipital sites, so visual-cortex paradigms are weak.

## Muse Athena (Muse S Athena)

| Spec              | Value                                |
|-------------------|--------------------------------------|
| EEG channels      | extended (verify in your unit)       |
| Sample rate       | 256 Hz                               |
| Other sensors     | PPG, fNIRS (Athena adds NIRS)        |
| Connection        | BLE                                  |

**Strengths.** Adds fNIRS for hemodynamic correlates, comfortable for long
recordings.
**Weaknesses.** Newer — fewer tutorials, SDK still evolving.

> ⚠️ **TODO (student):** verify the exact channel labels and sampling
> configuration on the unit you're issued, and document them at the top of
> your report. Don't trust this table over the device.

---

## Choosing between them

| Use case                                | Recommended |
|-----------------------------------------|-------------|
| Short cognitive tasks, frontal focus    | Muse 2      |
| Long-duration recordings, comfort       | Athena      |
| Need fNIRS / hemodynamic data           | Athena      |
| Maximum community / tutorial coverage   | Muse 2      |

## Pairing & connection

Two software paths — pick the one that fits your OS and comfort level:

1. **muselsl + LabRecorder** (cross-platform, Python-friendly)
   → see [`../data-collection/lab-recorder/`](../data-collection/lab-recorder/)
2. **Petal Metrics** or **Mind Monitor** (GUI app, CSV output)
   → see [`../data-collection/petal-metrics/`](../data-collection/petal-metrics/)

## Data quality checks before every recording

- [ ] All electrodes reading (no flat lines)
- [ ] Horsehoe / fit indicator green for ≥30 s
- [ ] Visible 10 Hz alpha bump on eyes-closed baseline
- [ ] No 50/60 Hz line-noise dominance
- [ ] Battery > 30 %
