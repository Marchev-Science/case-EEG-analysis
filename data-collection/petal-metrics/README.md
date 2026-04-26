# Petal Metrics / Mind Monitor (no-code path)

Use this if you can't get LSL working or you want a phone-based recorder.

## Petal Metrics (desktop)

- Connects to Muse via BLE.
- Outputs CSV with timestamped EEG samples.
- Limited marker support — usually you keep an `events.csv` by hand.

## Mind Monitor (mobile, paid)

- iOS / Android app.
- Records EEG, PPG, accelerometer.
- Exports CSV (and OSC if you want live streaming).

## Required side-car file

Whichever app you use, accompany every recording with `…_events.csv`:

```csv
onset_seconds,duration_seconds,label
0.0,60.0,baseline_eo
60.0,60.0,baseline_ec
120.0,300.0,code_solo
...
```

Onset is seconds from recording start. Without this you cannot epoch the data.

## Filename convention

```
data/raw/sub-<ID>/ses-<S>/eeg/sub-<ID>_ses-<S>_task-<TASK>_run-<R>_eeg.csv
data/raw/sub-<ID>/ses-<S>/eeg/sub-<ID>_ses-<S>_task-<TASK>_run-<R>_events.csv
```
