# Data Collection — Pick Your Path

> **Prereqs:** [`../docs/02-hardware.md`](../docs/02-hardware.md), [`../docs/03-data-collection.md`](../docs/03-data-collection.md)
> **Next:** pick [`muse2-bluemuse/`](muse2-bluemuse/README.md) **or** [`athena-openmuse/`](athena-openmuse/README.md), then [`lab-recorder/`](lab-recorder/README.md)
> **Related:** [`markers/send_markers.py`](markers/send_markers.py), [`petal-metrics/`](petal-metrics/README.md), [`../docs/xdf-format.md`](../docs/xdf-format.md)

---

You have two headsets and one recorder. The streaming software is different
per device; the recorder (LabRecorder) is the same.

| Headset       | Streaming software            | Folder                                          |
|---------------|-------------------------------|-------------------------------------------------|
| Muse 2        | **BlueMuse** (Windows GUI)    | [`muse2-bluemuse/`](muse2-bluemuse/README.md)   |
| Muse Athena   | **OpenMuse** (Python CLI)     | [`athena-openmuse/`](athena-openmuse/README.md) |

After you have a streaming source running, head to
[`lab-recorder/`](lab-recorder/README.md) to actually save the data to disk.

## Optional / fallback paths

| Path                        | When                                            | Folder                                       |
|-----------------------------|-------------------------------------------------|----------------------------------------------|
| Petal Metrics / Mind Monitor| You can't get LSL working, or want a phone app  | [`petal-metrics/`](petal-metrics/README.md)  |
| Marker stream               | You need event markers in your recording        | [`markers/send_markers.py`](markers/send_markers.py) |

## Why two software paths

- **BlueMuse** is a Windows-only GUI app — easiest possible setup, no Python.
  Best for the Muse 2 because it's been the de-facto Windows streamer for
  years and is rock-solid.
- **OpenMuse** is an active research tool (Dominique Makowski) that knows the
  Athena's BLE protocol — including the fNIRS optics — and exposes it as
  separate LSL streams. The Athena is too new for BlueMuse to handle well.

Use whichever matches your headset. Don't try to make BlueMuse stream the
Athena or OpenMuse stream the Muse 2 — both will technically run but you'll
miss sensors.

## OS support

| Path                      | Windows | macOS | Linux |
|---------------------------|---------|-------|-------|
| BlueMuse                  | ✅      | ❌    | ❌    |
| OpenMuse                  | ✅      | ✅*   | ✅*   |
| LabRecorder               | ✅      | ✅    | ✅    |
| Petal Metrics             | ✅      | ✅    | ❌    |
| Mind Monitor              | iOS / Android only            |

---

[**← Prev: 03 — Data Collection**](../docs/03-data-collection.md) | **Next:** pick [**Muse 2 → BlueMuse →**](muse2-bluemuse/README.md) or [**Athena → OpenMuse →**](athena-openmuse/README.md)

*\*OpenMuse: cross-platform on paper, but our setup notes are Windows.*
