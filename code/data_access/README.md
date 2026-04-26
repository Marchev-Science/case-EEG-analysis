# code/data_access

Loaders for the two recording formats used in this case study.

- `load_xdf.py` — XDF files from LabRecorder
- `load_muse_csv.py` — CSV files from Petal Metrics / Mind Monitor

Both should expose a function returning a structure containing:

- `eeg`: `numpy.ndarray` of shape `(n_channels, n_timepoints)`
- `times`: `numpy.ndarray` of shape `(n_timepoints,)` in seconds from recording start
- `channel_names`: list of strings
- `sample_rate`: float (Hz)
- `markers`: list of `(timestamp_seconds, code_or_label)` tuples

Stick to this contract so downstream code (preprocessing, features, models)
doesn't care which format was used.

## Reference

A working XDF loader for Muse data is in
[NeuroSense-Modules / data_loader.py](https://github.com/a1441/NeuroSense-Modules/blob/main/neurosense/data_loader.py).
Use it as inspiration; do not just import it.
