# XDF Files — A Friendly Guide

> **Prerequisites:** [`eeg-primer.md`](eeg-primer.md), [`03-data-collection.md`](03-data-collection.md) (you've recorded one)
> **Related:** [`../data-collection/lab-recorder/README.md`](../data-collection/lab-recorder/README.md), [`../code/data_access/README.md`](../code/data_access/README.md)
> **Next:** [`05-analysis-pipeline.md`](05-analysis-pipeline.md) — what to do with the data

---

## In one sentence

An **XDF file** is the file LabRecorder writes when you hit "Record" — it's
**one binary file that holds all your streams** (EEG, markers, PPG,
accelerometer, …) lined up in time so you can analyse them together later.

You open it in Python with one line:

```python
import pyxdf
streams, header = pyxdf.load_xdf("recording.xdf")
```

That's the whole game. The rest of this page explains what's *in* the file,
why we use this format, and how to turn it into the things you'll actually
work with — pandas DataFrames, CSVs, MNE objects.

---

## "OK but what's actually inside?"

Imagine your recording session. You had several things sending data at the
same time:

- The **EEG** stream from BlueMuse or OpenMuse — 256 samples per second of
  brain voltage on 4 channels.
- A **marker** stream — short integer codes you (or your script) push at
  important moments ("video started", "rest begins", etc.).
- Maybe a **PPG** stream (heart rate, 64 samples per second).
- Maybe **accelerometer** and **gyroscope** (52 Hz each).
- A **battery** stream that updates every few seconds.

Each of those is going at a **different rate**. They're sometimes coming
from **different programs**, even different computers. You can't just
write them into one CSV — there's no row that "fits" all of them at once.

XDF solves that by storing each stream **separately, with its own
timestamps**, in one container file. When you load it back, every sample
in every stream has a number in seconds telling you exactly when it
happened, and all those numbers are on **the same timeline**.

That's it. That's why XDF exists.

> **Why not just CSV?** CSV is one big table — one row, one moment, one set
> of values. The moment you have streams at different rates, CSV stops
> working. (You can convert XDF *to* CSV after the fact — see below — but
> you can't record at different rates straight to a single CSV.)

---

## A tiny mental model of an XDF

Don't worry about the binary internals. Mentally, after loading, an XDF
file looks like this:

```
streams = [
    { name: "Muse-D31A",                 # the EEG
      type: "EEG",
      time_series: [...50688 rows × 5 channels...],   # the actual numbers
      time_stamps: [...50688 timestamps in seconds...] },

    { name: "experiment_markers",        # the markers
      type: "Markers",
      time_series: [[1], [10], [99], [20], ...],      # codes you sent
      time_stamps: [12.4, 78.0, 138.0, 200.5, ...] }, # when you sent them

    { name: "Muse-D31A_PPG", ... },      # other streams ...
    { name: "Muse-D31A_Accelerometer", ... },
]
```

**`time_series`** = the actual data values.
**`time_stamps`** = the second on the synchronised clock for each row of
`time_series`.

The lists are the **same length** within a stream — one timestamp per
sample. Across streams the lists are different lengths because the rates
differ.

---

## Your first XDF script — copy, paste, run

Save as `peek.py`, put your `.xdf` next to it, run `python peek.py`:

```python
import pyxdf

streams, header = pyxdf.load_xdf("recording.xdf")

print(f"Found {len(streams)} streams:\n")
for s in streams:
    info = s["info"]
    name = info["name"][0]
    typ = info["type"][0]
    rate = float(info["nominal_srate"][0])
    samples = len(s["time_stamps"])
    print(f"  - {typ:10s}  {name:30s}  rate={rate:6.1f} Hz  samples={samples}")
```

Expected output (Muse 2 + BlueMuse, 60 s recording):

```
Found 5 streams:

  - EEG         Muse-D31A                       rate= 256.0 Hz  samples=15360
  - PPG         Muse-D31A_PPG                   rate=  64.0 Hz  samples= 3840
  - Mocap       Muse-D31A_Accelerometer         rate=  52.0 Hz  samples= 3120
  - Mocap       Muse-D31A_Gyroscope             rate=  52.0 Hz  samples= 3120
  - Markers     experiment_markers              rate=   0.0 Hz  samples=   12
```

That `rate=0.0 Hz` for markers is normal — markers are irregular by design.

If your file looks empty (sample counts of 0), the streamer wasn't actually
streaming when you hit Record — re-check the BlueMuse / OpenMuse window.

---

## How does the timing actually work? (1-paragraph version, skippable)

You can skip this on first read.

> Every LSL outlet (BlueMuse, OpenMuse, your marker script) timestamps each
> sample with **its own clock**. Every few seconds, LabRecorder ping-pongs
> each outlet to measure the offset between its clock and the recorder's
> clock. After recording, when you call `pyxdf.load_xdf(...)`, pyxdf
> **applies all those measured offsets** so every stream's `time_stamps`
> are on one common timeline. You normally don't think about this — it
> Just Works™. If you ever want the raw, un-corrected timestamps for some
> reason, pass `synchronize_clocks=False`.

The takeaway: trust `time_stamps`. They're already synchronised.

---

## Picking out the EEG stream (and not getting confused)

After loading, you have a *list* of streams. You usually want the EEG one
specifically:

```python
def find_stream(streams, type_):
    matches = [s for s in streams if s["info"]["type"][0].lower() == type_.lower()]
    if len(matches) == 0:
        raise ValueError(f"No '{type_}' stream in this file")
    if len(matches) > 1:
        names = [m["info"]["name"][0] for m in matches]
        raise ValueError(f"Multiple '{type_}' streams found: {names}. Pick one by name.")
    return matches[0]

eeg = find_stream(streams, "EEG")
markers = find_stream(streams, "Markers")
```

If you ever recorded **two devices at once** (hyperscanning), you'll get
two EEG streams and that helper will refuse — which is what you want, so
you don't accidentally mix them up. Pick by `name` instead:

```python
eeg = next(s for s in streams if s["info"]["name"][0] == "Muse-D31A")
```

---

## Getting channel names (e.g. TP9 / AF7 / AF8 / TP10)

Channel labels live inside the stream's metadata. The path is awkward
because LSL metadata is XML; pyxdf gives it back as nested dicts of lists.
Defensive helper:

```python
def channel_labels(stream):
    info = stream["info"]
    n = int(info["channel_count"][0])
    try:
        chans = info["desc"][0]["channels"][0]["channel"]
        labels = [c["label"][0] for c in chans]
        if len(labels) == n:
            return labels
    except (KeyError, TypeError, IndexError):
        pass
    return [f"ch{i}" for i in range(n)]   # fallback if labels missing

print(channel_labels(eeg))
# Expected for Muse 2 + BlueMuse: ['TP9', 'AF7', 'AF8', 'TP10', 'Right AUX']
```

> **Drop `Right AUX`** in your analysis — it's a reference electrode, not
> brain. Keep `TP9, AF7, AF8, TP10`.

---

## Convert to a pandas DataFrame

This is usually the format you actually want to work with.

```python
import pandas as pd

def stream_to_df(stream):
    """One stream -> one DataFrame with a time_s column + one column per channel."""
    labels = channel_labels(stream)
    arr = stream["time_series"]
    df = pd.DataFrame(arr, columns=labels)        # works for both EEG (numpy array) and Markers (list of lists)
    df.insert(0, "time_s", stream["time_stamps"]) # prepend the timestamps
    return df

eeg_df = stream_to_df(eeg)
print(eeg_df.head())
```

Output:
```
       time_s    TP9    AF7    AF8   TP10  Right AUX
0  165432.10   12.5   -3.2    8.1   -2.7      512.0
1  165432.10   13.1   -2.9    7.8   -2.5      512.0
...
```

Those `time_s` numbers are seconds **on the LSL clock** — a big number
counting up from when LSL started, not from your recording. To get
**seconds from recording start**, subtract the earliest timestamp in any
stream:

```python
t0 = min(s["time_stamps"][0] for s in streams if len(s["time_stamps"]) > 0)
eeg_df["time_s"] = eeg_df["time_s"] - t0
markers_df = stream_to_df(markers)
markers_df["time_s"] = markers_df["time_s"] - t0
```

Now `time_s = 0` is the first sample of the recording. Much friendlier.

---

## Convert to CSV

Write **one CSV per stream**. (Don't try to mash streams of different rates
into one CSV — you'd waste rows on NaNs and lose precision.)

```python
from pathlib import Path

def xdf_to_csvs(xdf_path, out_dir):
    streams, _ = pyxdf.load_xdf(xdf_path)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    t0 = min(s["time_stamps"][0] for s in streams if len(s["time_stamps"]) > 0)
    for s in streams:
        df = stream_to_df(s)
        df["time_s"] = df["time_s"] - t0
        name = s["info"]["name"][0].replace(" ", "_")
        typ = s["info"]["type"][0]
        df.to_csv(out_dir / f"{typ}_{name}.csv", index=False)
        print(f"wrote {typ}_{name}.csv ({len(df)} rows)")

xdf_to_csvs("recording.xdf", "recording_csv/")
```

You'll get a folder like:
```
recording_csv/
  EEG_Muse-D31A.csv
  PPG_Muse-D31A_PPG.csv
  Mocap_Muse-D31A_Accelerometer.csv
  Mocap_Muse-D31A_Gyroscope.csv
  Markers_experiment_markers.csv
```

---

## Loading into MNE (the standard EEG analysis library)

[MNE-Python](https://mne.tools) is what most academic EEG analysis is
written in. It works with `Raw` objects, not XDF, so you bridge:

```python
import numpy as np
import mne

eeg = find_stream(streams, "EEG")
labels = channel_labels(eeg)

# Drop the Muse 2 reference channel
keep = [i for i, name in enumerate(labels) if name != "Right AUX"]
data = np.asarray(eeg["time_series"]).T[keep]    # shape: (n_channels, n_samples)
ch_names = [labels[i] for i in keep]
sfreq = float(eeg["info"]["nominal_srate"][0])

info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types="eeg")
raw = mne.io.RawArray(data * 1e-6, info)         # MNE expects volts; Muse gives microvolts
raw.set_montage("standard_1020", on_missing="ignore")

raw.plot()    # opens a scrollable EEG viewer
```

If you only ever use one EEG library, make it MNE — it has filtering,
artifact rejection (ICA, ASR), epoching, frequency analysis, and
visualisation all built in.

---

## Aligning markers with EEG (cutting epochs)

Once you've subtracted `t0` from both streams, "marker fired at second X
of the recording" lines up perfectly with "the EEG sample whose `time_s`
is X". To cut a 4-second window starting at each marker:

```python
window_s = 4.0
sfreq = float(eeg["info"]["nominal_srate"][0])
window_n = int(window_s * sfreq)

eeg_arr = np.asarray(eeg["time_series"])          # shape: (n_samples, n_channels)
eeg_t = np.asarray(eeg["time_stamps"]) - t0
markers_t = np.asarray(markers["time_stamps"]) - t0
marker_codes = [m[0] for m in markers["time_series"]]

epochs = []
for t, code in zip(markers_t, marker_codes):
    start = np.searchsorted(eeg_t, t)
    end = start + window_n
    if end <= len(eeg_arr):
        epochs.append((code, eeg_arr[start:end]))

print(f"got {len(epochs)} epochs of shape {epochs[0][1].shape}")
```

(For real analysis use `mne.Epochs` — it handles baseline correction,
rejection, etc. The snippet above is just to show the alignment logic.)

---

## Looking at an XDF without writing code

Sometimes you just want to peek. Options:

- **MNELAB** — friendly desktop GUI on top of MNE. Opens XDF directly.
  https://github.com/cbrnr/mnelab
- **EEGLAB** (MATLAB) — `File → Import data → Using LSL Lab Streaming Layer (XDF)`.
- **The little snippet in [`../data-collection/lab-recorder/README.md`](../data-collection/lab-recorder/README.md#verify-the-file-after-recording)** —
  the same `print(streams)` loop as above, useful for a quick sanity check.

For first-time verification right after recording, the print snippet is
fastest. For browsing waveforms, install MNELAB.

---

## Common gotchas (read once, save yourself an hour later)

| What you see                                              | Why / fix                                                                                       |
|-----------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Sample count is 0 for an EEG stream                       | The streamer (BlueMuse / OpenMuse) wasn't actually running when you hit Record. Re-record.       |
| Marker `time_series` looks like `[[1], [99], ...]`        | That's correct — markers are 1-channel. Flatten with `[m[0] for m in arr]`.                      |
| Timestamps are huge numbers (e.g. 165432.10)              | They're seconds on the LSL clock, not seconds-from-zero. Subtract `t0` (see above).              |
| Effective sample rate < nominal                           | Bluetooth dropped packets. Look at `info["effective_srate"]` from the loaded stream metadata.    |
| File is huge (>1 GB)                                      | You ticked too many streams in LabRecorder. Untick `Telemetry`/`Battery`/etc. next time.         |
| Two EEG streams in one file                               | You ran two headsets at once. Disambiguate by `info["name"][0]`.                                 |
| `pyxdf.load_xdf` is slow                                  | Normal for big files (it's pure Python). Cache to `.fif` or `.parquet` after first load.        |
| EEG values around 800 instead of microvolts               | The streamer is sending raw ADC counts. Check the unit field, may need scaling.                  |
| `pyxdf` not installed                                     | `pip install pyxdf` (it's in `requirements.txt`).                                                |

---

## Going further

- **pyxdf docs and examples:** https://github.com/xdf-modules/pyxdf
- **LSL home:** https://labstreaminglayer.readthedocs.io
- **XDF format spec** (only if you're really curious): https://github.com/sccn/xdf/wiki/Specifications
- **MNE tutorials:** https://mne.tools/stable/auto_tutorials/index.html

---

> **Where next?**
> - Wire up the loader at [`../code/data_access/load_xdf.py`](../code/data_access/load_xdf.py) using the patterns above.
> - Read [`05-analysis-pipeline.md`](05-analysis-pipeline.md) for the rest of the analysis flow.
> - Use [`../code/notebooks/00-quickstart.ipynb`](../code/notebooks/00-quickstart.ipynb) to try loading your first recording.
