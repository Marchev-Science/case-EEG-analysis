# LabRecorder + LSL Setup

The recommended path for serious recordings. Streams EEG over LSL and lets
you record with synchronised event markers.

## One-time install

```bash
pip install muselsl pylsl pyxdf
```

Download **LabRecorder** from the SCCN releases page and unzip.

> Note (Windows): on first connection, pair the Muse in Bluetooth Settings
> first, *then* run `muselsl stream`.

## Per-session

1. Power on Muse, ensure good fit.
2. In a terminal:
   ```bash
   muselsl stream
   ```
   You should see `Streaming EEG…` and a stream named `Muse`.
3. (Optional) In a second terminal start the marker stream:
   ```bash
   python ../markers/send_markers.py
   ```
   Or have your experiment script create the marker outlet itself.
4. Open LabRecorder, click **Update**, tick the EEG stream and any marker
   streams, set the filename template (see below), click **Start**.
5. Run your experiment. Each condition transition should send a marker.
6. Click **Stop**.

## Filename template

In LabRecorder set:

```
%s/sub-%p/ses-%s/eeg/sub-%p_ses-%s_task-%n_run-%r_eeg.xdf
```

Then per-recording fill in: participant `001`, session `S001`, task `coding-ai`, run `001`.

## Verifying the file

```python
import pyxdf
streams, header = pyxdf.load_xdf("path/to/file.xdf")
for s in streams:
    print(s["info"]["type"][0], s["info"]["name"][0],
          s["time_series"].shape if hasattr(s["time_series"], "shape") else len(s["time_series"]))
```

You should see `EEG` and your marker stream with non-zero length.
