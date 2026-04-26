# Muse Athena — OpenMuse + LabRecorder (Windows)

> **Prereqs:** [`../README.md`](../README.md), [`../../docs/02-hardware.md`](../../docs/02-hardware.md)
> **Next:** [`../lab-recorder/README.md`](../lab-recorder/README.md) (record once you're streaming)
> **Related:** [`../markers/send_markers.py`](../markers/send_markers.py), [`../../docs/eeg-primer.md`](../../docs/eeg-primer.md), [`../../docs/xdf-format.md`](../../docs/xdf-format.md)

---

The Athena (Muse S Athena) is too new for BlueMuse, so we use **OpenMuse** —
a research-grade Python tool by Dominique Makowski that decodes the Athena's
BLE packets (EEG + PPG + fNIRS optics + accel/gyro + battery) and republishes
them as LSL streams.

- Upstream: https://github.com/DominiqueMakowski/OpenMuse
- Local clone (already on this PC): `D:\DominiqueMakowski-OpenMuse-a9be252`

> **Disclaimer (from upstream).** OpenMuse is *not* an InteraXon product, has
> no warranty, and is experimental research software. It works well; it's
> just not a vendor product.

---

## Prerequisites

- **Python 3.12 or newer.** This is a hard requirement from OpenMuse's
  `pyproject.toml`. Older Python won't even let pip install it.
  Check:
  ```powershell
  python --version
  ```
  Install if needed:
  ```powershell
  winget install Python.Python.3.12
  ```
  (or download from https://www.python.org/downloads/)
- Windows 10 / 11 with built-in BLE (uses the cross-platform `bleak`
  library; no extra drivers).
- LabRecorder (download once — see [`../lab-recorder/`](../lab-recorder/README.md)).

---

## One-time Python environment setup

We use a virtual environment so OpenMuse's dependencies don't pollute your
system Python. Open a PowerShell window in any working directory — the
case-repo root is fine:

```powershell
cd D:\Claude\case-EEG-analysis

# 1. Create the venv with Python 3.12 explicitly
py -3.12 -m venv .venv-openmuse

# 2. Activate it (PowerShell)
.\.venv-openmuse\Scripts\Activate.ps1
# (cmd.exe equivalent: .\.venv-openmuse\Scripts\activate.bat)

# 3. Upgrade pip
python -m pip install --upgrade pip

# 4. Install OpenMuse from GitHub
pip install https://github.com/DominiqueMakowski/OpenMuse/zipball/main
```

If you're offline or want to use the local clone:
```powershell
pip install D:\DominiqueMakowski-OpenMuse-a9be252
```

If `Activate.ps1` errors with "scripts disabled" / "execution policy",
run once in an admin PowerShell:
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### What gets installed

From OpenMuse's `pyproject.toml`:

| Package        | Why                                                       |
|----------------|-----------------------------------------------------------|
| `bleak ≥ 0.21` | Cross-platform Bluetooth Low Energy                        |
| `mne-lsl ≥ 1.10` | LSL backend — note: NOT `pylsl`. Don't `pip install pylsl` here. |
| `numpy ≥ 1.24` | Math                                                      |
| `pandas ≥ 1.5` | DataFrame loading of recorded raw data                    |
| `matplotlib ≥ 3.5` | Plotting                                              |
| `vispy ≥ 0.12` | Live signal viewer (`OpenMuse view`)                      |

### Verify the install

```powershell
OpenMuse --help
```

You should see a help text listing `find`, `record`, `stream`, `view`.

---

## Per-session: pair, find, stream

Pairing in Windows Bluetooth Settings is **not** needed — OpenMuse connects
directly via MAC.

### 1. Power on the Athena

Long-press until the blue light on the front comes on.

### 2. Activate the venv

```powershell
.\.venv-openmuse\Scripts\Activate.ps1
```

You should see `(.venv-openmuse)` at the start of your prompt.

### 3. Find the device

```powershell
OpenMuse find
```

It scans BLE and prints any nearby Muse:
```
Found device MuseS-D31A, MAC Address 00:55:DA:BB:D3:1A
```

Write the MAC down. You'll reuse it.

### 4. Stream all sensors

```powershell
OpenMuse stream --address 00:55:DA:BB:D3:1A
```

Default preset is `p1041` which enables every channel. Leave this terminal
running — Ctrl+C stops the stream.

You can now open LabRecorder ([`../lab-recorder/`](../lab-recorder/README.md))
and you should see four streams.

### 5. (Optional) live viewer

Open a *second* PowerShell, activate the venv again, then:
```powershell
OpenMuse view
```

A live waveform window opens. Useful for the eyes-closed alpha-bump
sanity check (see [`../../docs/eeg-primer.md`](../../docs/eeg-primer.md)).

### 6. (Optional) subset of sensors

```powershell
OpenMuse stream --address <MAC> --sensors EEG OPTICS
```

Only the listed sensor groups are streamed. Saves bandwidth if you don't
care about, e.g., gyroscope.

---

## LSL streams produced

| Stream name      | Type      | Channels | Rate     | Notes                                            |
|------------------|-----------|----------|----------|--------------------------------------------------|
| `Muse_EEG`       | EEG       | 8        | 256 Hz   | 4 EEG sites + 4 amplified aux                    |
| `Muse_ACCGYRO`   | Mocap     | 6        | 52 Hz    | 3-axis accelerometer + 3-axis gyroscope          |
| `Muse_OPTICS`    | NIRS      | 16       | 64 Hz    | Triple-wavelength PPG + fNIRS 5-optode array     |
| `Muse_BATTERY`   | Battery   | 1        | ~0.2 Hz  | Live battery percentage                          |

When you record in LabRecorder, tick all the streams you care about — at
minimum `Muse_EEG` and your marker stream. Tick `Muse_OPTICS` if you plan
to use the fNIRS / PPG signals.

---

## Hyperscanning (two devices at once)

Stream both:
```powershell
OpenMuse stream --address 00:55:DA:B9:FA:20 00:55:DA:BB:CD:CD
```

LSL stream names get the MAC suffix
(`Muse-EEG (00:55:DA:B9:FA:20)`, `Muse-EEG (00:55:DA:BB:CD:CD)`),
so LabRecorder can record them as separate streams in one XDF.

For the live viewer, target one device per terminal:
```powershell
OpenMuse view --address 00:55:DA:B9:FA:20
```

---

## Troubleshooting

| Symptom                                       | Fix                                                                                |
|-----------------------------------------------|------------------------------------------------------------------------------------|
| `OpenMuse: command not found`                 | Venv isn't activated. Re-run `.\.venv-openmuse\Scripts\Activate.ps1`.              |
| `Could not find a version that satisfies … requires-python ">=3.12"` | Default `python` is older. Recreate the venv with `py -3.12 -m venv …`.        |
| `OpenMuse find` returns nothing               | Athena off, out of range, or a phone/PC is already connected to it. Power-cycle the headset. |
| Stream connects then drops within seconds     | 2.4 GHz interference. Move away from microwaves / Wi-Fi APs / USB 3.0 hubs.        |
| `mne-lsl` install fails on Windows            | Install "Visual C++ Redistributable for Visual Studio 2015–2022" from Microsoft.   |
| `bleak` errors about Bluetooth radio          | Check Device Manager → Bluetooth — radio may be disabled or driver missing.        |
| Streaming OK but LabRecorder doesn't list streams | Click **Update** in LabRecorder. If still missing, restart LabRecorder.        |

### Recording raw BLE packets (alternative to LSL)

If you want to record without LabRecorder (e.g., because you only need EEG
for offline analysis):
```powershell
OpenMuse record --address <MAC> --duration 60 --outfile data.txt
```

Load it with:
```python
import OpenMuse, pandas as pd
with open("data.txt", encoding="utf-8") as f:
    data = OpenMuse.decode_rawdata(f.readlines())
data["EEG"].head()
```

You lose synchronised marker support, so prefer the LSL path for any
condition-based experiment.

---

[**← Prev: Data Collection (overview)**](../README.md) | [**Next: LabRecorder →**](../lab-recorder/README.md)
