# data/

> **Prereqs:** [`../docs/03-data-collection.md`](../docs/03-data-collection.md)
> **Related:** [`../data-collection/lab-recorder/README.md`](../data-collection/lab-recorder/README.md), [`../docs/xdf-format.md`](../docs/xdf-format.md), [`../code/data_access/README.md`](../code/data_access/README.md)

---

`raw/` and `processed/` are gitignored. Only `.gitkeep` files are committed
so the directories exist on clone.

## Layout (BIDS-inspired)

```
raw/
  sub-<ID>/
    ses-<S>/
      eeg/
        sub-<ID>_ses-<S>_task-<TASK>_run-<R>_eeg.xdf      ← LabRecorder
        sub-<ID>_ses-<S>_task-<TASK>_run-<R>_eeg.csv      ← Petal/Mind Monitor
        sub-<ID>_ses-<S>_task-<TASK>_run-<R>_events.csv   ← required for CSV path
        sub-<ID>_ses-<S>_task-<TASK>_run-<R>_notes.md     ← session notes
processed/
  <your derivatives, organised however helps you>
```

## Conventions

- Subject IDs: opaque (`sub-001`, `sub-002`, ...). No names, initials, emails.
- Task labels (lowercase, no spaces): `baseline-eo`, `baseline-ec`,
  `code-solo`, `code-ai`, `watch-neutral`, `gaming`, `shopping`,
  `market`, `iq-test`, `video-short-instr`, etc.
- Run numbers zero-padded: `run-001`.

## Large data

If recordings exceed comfortable git size, push raw data to OSF / Zenodo /
Google Drive and link from your report. Always commit a `MANIFEST.md` here
listing what's in the external store and a hash for each file.

## Privacy

Keep the participant ID → person mapping **outside** this repo. Treat raw
EEG as personally identifying.
