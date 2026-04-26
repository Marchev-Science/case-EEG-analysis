# 03 — Data Collection

Two recording paths are supported. Use whichever you can get working — both
produce analyzable data.

The detailed, noob-friendly walkthroughs live under
[`../data-collection/`](../data-collection/README.md). This page is the
overview.

---

## Path A — LSL + LabRecorder (recommended)

Streams EEG over Lab Streaming Layer (LSL), records to `.xdf` files. Lets
you also stream event markers from Python during the experiment.

The streaming software differs per device:

| Headset      | Streaming software                                                | Walkthrough                                                       |
|--------------|-------------------------------------------------------------------|-------------------------------------------------------------------|
| Muse 2       | **BlueMuse** (Windows GUI)                                        | [`data-collection/muse2-bluemuse/`](../data-collection/muse2-bluemuse/README.md)   |
| Muse Athena  | **OpenMuse** (Python CLI)                                         | [`data-collection/athena-openmuse/`](../data-collection/athena-openmuse/README.md) |

LabRecorder is the same for both: see
[`data-collection/lab-recorder/`](../data-collection/lab-recorder/README.md).

### Markers from your experiment script

See [`../data-collection/markers/send_markers.py`](../data-collection/markers/send_markers.py).

### File layout convention

```
data/raw/sub-<ID>/ses-<S>/eeg/sub-<ID>_ses-<S>_task-<TASK>_run-<R>_eeg.xdf
```

This is BIDS-inspired and what most pipelines (including the reference
NeuroSense pipeline) expect.

---

## Path B — Petal Metrics or Mind Monitor (no-code)

GUI applications that connect to Muse via BLE and write CSV.

**Pros.** Zero setup, works on a phone (Mind Monitor on iOS/Android).
**Cons.** Marker support is limited — you usually log events by hand or in a
separate file with synced timestamps.

See [`../data-collection/petal-metrics/`](../data-collection/petal-metrics/README.md).

### File layout convention

```
data/raw/sub-<ID>/ses-<S>/eeg/sub-<ID>_ses-<S>_task-<TASK>_run-<R>_eeg.csv
data/raw/sub-<ID>/ses-<S>/eeg/sub-<ID>_ses-<S>_task-<TASK>_run-<R>_events.csv
```

The `events.csv` should have at least `onset_seconds, duration_seconds, label`.

---

## Recording checklist

- [ ] Quiet room, phones on Do Not Disturb
- [ ] Participant briefed and consent signed
- [ ] Hardware quality check passed (see `02-hardware.md`)
- [ ] 60 s eyes-open + 60 s eyes-closed baseline before task
- [ ] Markers sent at every condition transition
- [ ] Filename follows convention
- [ ] Notes file written immediately after the session
