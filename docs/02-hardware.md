# 02 — Hardware

> **Prereqs:** [`eeg-primer.md`](eeg-primer.md), [`01-the-case.md`](01-the-case.md)
> **Next:** [`03-data-collection.md`](03-data-collection.md)
> **Related:** [`../data-collection/README.md`](../data-collection/README.md) (per-device walkthroughs)

---

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

Software path depends on the headset:

| Headset      | Streaming software             | Walkthrough                                                                          |
|--------------|--------------------------------|--------------------------------------------------------------------------------------|
| Muse 2       | **BlueMuse** (Windows GUI)     | [`../data-collection/muse2-bluemuse/`](../data-collection/muse2-bluemuse/README.md)   |
| Muse Athena  | **OpenMuse** (Python CLI)      | [`../data-collection/athena-openmuse/`](../data-collection/athena-openmuse/README.md) |

Both feed [LabRecorder](../data-collection/lab-recorder/README.md), which
writes a single `.xdf` file with all streams aligned.

If you can't get LSL working, fall back to **Petal Metrics** or **Mind
Monitor** (CSV output): [`../data-collection/petal-metrics/`](../data-collection/petal-metrics/README.md).

## Data quality checks before every recording

- [ ] All electrodes reading (no flat lines)
- [ ] Horsehoe / fit indicator green for ≥30 s
- [ ] Visible 10 Hz alpha bump on eyes-closed baseline
- [ ] No 50/60 Hz line-noise dominance
- [ ] Battery > 30 %
