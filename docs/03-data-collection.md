# 03 — Data Collection

Two recording paths are supported. Use whichever you can get working — both
produce analyzable data.

---

## Path A — LSL + LabRecorder (recommended)

Streams EEG over Lab Streaming Layer (LSL), records to `.xdf` files. Lets
you also stream event markers from Python during the experiment.

### Install

```bash
pip install muselsl pylsl pyxdf
```

Download **LabRecorder** from the SCCN releases page.

### Record

```bash
# 1. Start the EEG stream (in one terminal)
muselsl stream

# 2. Optionally start PPG / accel
muselsl stream --ppg --acc --gyro

# 3. Open LabRecorder, tick the EEG stream and your marker stream, hit Record.
```

### Send markers from your experiment script

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
