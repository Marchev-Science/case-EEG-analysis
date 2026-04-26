# LabRecorder

> **Prereqs:** a streaming source: [`../muse2-bluemuse/README.md`](../muse2-bluemuse/README.md) **or** [`../athena-openmuse/README.md`](../athena-openmuse/README.md)
> **Next:** [`../../docs/04-experimental-design.md`](../../docs/04-experimental-design.md), then [`../../docs/xdf-format.md`](../../docs/xdf-format.md) to load what you recorded
> **Related:** [`../markers/send_markers.py`](../markers/send_markers.py), [`../../data/README.md`](../../data/README.md)

---

LabRecorder writes any LSL streams it can see to a single `.xdf` file.
**It does not stream from your headset directly** — that's the job of
BlueMuse (Muse 2) or OpenMuse (Athena). Get one of those running first:

- Muse 2 → [`../muse2-bluemuse/`](../muse2-bluemuse/README.md)
- Athena → [`../athena-openmuse/`](../athena-openmuse/README.md)

---

## One-time install

Download the LabRecorder release for your OS from
https://github.com/labstreaminglayer/App-LabRecorder/releases and unzip
somewhere stable (e.g., `D:\Tools\LabRecorder\`).

There's no installer — `LabRecorder.exe` is the executable.

---

## Per-session

1. Make sure your streaming source is running:
   - **Muse 2**: BlueMuse window open, "Streaming…" next to your device.
   - **Athena**: PowerShell with `OpenMuse stream --address <MAC>` running.
2. (Optional) Start the marker stream in another terminal:
   ```powershell
   python ..\markers\send_markers.py
   ```
   See [`../markers/`](../markers/) for details.
3. Launch `LabRecorder.exe`.
4. Click **Update** — your streams should appear under "Available streams":
   - From BlueMuse: `Muse-XXXX`, `Muse-XXXX_PPG`, etc.
   - From OpenMuse: `Muse_EEG`, `Muse_ACCGYRO`, `Muse_OPTICS`, `Muse_BATTERY`.
   - Plus `experiment_markers` if you started the marker script.
5. **Tick** every stream you want recorded (at minimum: EEG + markers).
6. Set the "Study Root" to `D:\Claude\case-EEG-analysis\data\raw`.
7. Set the filename template (next section).
8. Fill in the participant / session / task / run fields below the template.
9. Click **Start** when ready, **Stop** when done.

---

## Filename template

In LabRecorder, paste this into the filename template field:

```
%s/sub-%p/ses-%s/eeg/sub-%p_ses-%s_task-%n_run-%r_eeg.xdf
```

Per-recording fields:

| Field | LabRecorder placeholder | Example          |
|-------|-------------------------|------------------|
| Participant | `%p`              | `001`            |
| Session     | `%s`              | `S001`           |
| Task / Block name | `%n`        | `code-ai`        |
| Run         | `%r`              | `001`            |

Resulting file:
`data/raw/sub-001/ses-S001/eeg/sub-001_ses-S001_task-code-ai_run-001_eeg.xdf`

This is BIDS-inspired and matches what the analysis-side code in this repo
expects. See [`../../data/README.md`](../../data/README.md) for the full
naming convention.

---

## Verify the file after recording

```python
import pyxdf

streams, header = pyxdf.load_xdf("path/to/file.xdf")
for s in streams:
    name = s["info"]["name"][0]
    typ = s["info"]["type"][0]
    n = len(s["time_series"]) if isinstance(s["time_series"], list) else s["time_series"].shape[0]
    print(f"{typ:10s} {name:30s} samples={n}")
```

You should see your EEG stream with thousands of samples (≈256 × seconds
recorded) and your marker stream with one row per marker pushed.

If a stream shows zero samples, that source wasn't actually streaming —
re-check the BlueMuse / OpenMuse window before the next session.

---

## Recording markers

Markers are how you align the EEG to your experiment events
("watching video", "rest", "cond A start"). Two ways:

1. **Use the included script** as-is — types markers manually into a
   PowerShell prompt:
   ```powershell
   python ..\markers\send_markers.py
   ```
2. **Send markers from your experiment script** — copy the LSL outlet
   pattern from [`../markers/send_markers.py`](../markers/send_markers.py)
   into your stimulus-presentation code (PsychoPy, pygame, plain Python).
   That's much more reliable than typing.

LabRecorder will record both the EEG stream and the marker stream into the
same XDF, time-aligned via LSL's clock.

---

[**← Prev: Streaming (BlueMuse / OpenMuse)**](../README.md) | [**Next: 04 — Experimental Design →**](../../docs/04-experimental-design.md)

*After your first recording:* [`../../docs/xdf-format.md`](../../docs/xdf-format.md) — load and inspect the XDF you just made.
