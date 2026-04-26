# Muse 2 — BlueMuse + LabRecorder (Windows)

> **Prereqs:** [`../README.md`](../README.md), [`../../docs/02-hardware.md`](../../docs/02-hardware.md)
> **Next:** [`../lab-recorder/README.md`](../lab-recorder/README.md) (record once you're streaming)
> **Related:** [`../markers/send_markers.py`](../markers/send_markers.py), [`../../docs/eeg-primer.md`](../../docs/eeg-primer.md), [`../../docs/xdf-format.md`](../../docs/xdf-format.md)

---

The easiest path on Windows. BlueMuse handles BLE → LSL; LabRecorder writes
the LSL streams to an XDF file.

> **Heads-up.** BlueMuse is **Windows only** and **not on the Microsoft
> Store** — you sideload it from GitHub. Follow the steps in order.

---

## Prerequisites

- Windows 10 (build ≥ 10.0.15063, "Fall 2017 Creators Update") or Windows 11
- A working Bluetooth 4.0+ adapter (built-in on most laptops; check with
  Device Manager → Bluetooth)
- An admin PowerShell prompt for the one-time setup below

---

## One-time Windows setup (the parts noobs miss)

These three settings together unblock 90 % of "BlueMuse won't install / won't
stream" tickets.

### 1. Enable Developer Mode
`Settings → Privacy & security → For developers → Developer Mode = On`

This is needed for Windows to allow installing a sideloaded `.appxbundle`.

### 2. Allow PowerShell scripts (admin PowerShell, run once)

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Without this, the BlueMuse install script will be blocked by execution policy.

### 3. Firewall exception for `LSLBridge.exe`

The first time you stream, Windows Defender Firewall will pop a dialog
asking whether to allow `LSLBridge.exe`. **Tick "Private networks" and
click Allow.**

If you missed the dialog:
`Control Panel → System and Security → Windows Defender Firewall → Allow
an app or feature through Windows Defender Firewall → Change settings →
Allow another app… → Browse to LSLBridge.exe → check Private`.

### Registry — nothing to do

The BlueMuse README explicitly says no registry edits are required.
Internally BlueMuse stores its app settings in the UWP container at
`C:\Users\<you>\AppData\Local\Packages\07220b98-ffa5-4000-9f7c-e168a00899a6_*\`,
but you should never edit anything there by hand — use the in-app Settings.

---

## Install BlueMuse

1. Go to https://github.com/kowalej/BlueMuse/releases and download the latest
   release `.zip` (currently **v2.4.0.0**).
2. Right-click the downloaded `.zip` → **Properties** → tick **Unblock** →
   Apply. (Windows quarantines downloaded zips; without unblocking, the
   install script will fail with a security error.)
3. Unzip somewhere stable, e.g. `D:\Tools\BlueMuse\`.
4. Right-click `InstallBlueMuse.ps1` → **Run with PowerShell**.
   The script will:
   - Install the BlueMuse signing certificate (you'll get a UAC prompt — accept).
   - Install `Microsoft.NET.Native.Framework.1.7` and
     `Microsoft.NET.Native.Runtime.1.7` from the Dependencies folder.
   - Install the main `BlueMuse_x64.appxbundle`.
5. Verify: open the Start menu and type "BlueMuse" — the app should launch.

### Manual fallback (if the PowerShell script fails)

Most failures are the certificate. Do it by hand:
1. Double-click the `.cer` file → **Install Certificate** → Local Machine →
   **Place all certificates in the following store** → Browse → **Trusted
   People** → OK → Finish.
2. Open the `Dependencies\x64\` folder and right-click each `.appx` →
   **Install**.
3. Right-click the main `BlueMuse_x64.appxbundle` → **Install**.

---

## Pair the Muse 2 (one-time)

1. Power on the Muse 2 (long-press the power button until the LEDs flash).
2. `Settings → Devices → Bluetooth & other devices → Add device → Bluetooth`
   → wait for `Muse-XXXX` to appear → click it → Pair.
3. **Now REMOVE the device from the Bluetooth list.**
   (`Settings → Bluetooth → Muse-XXXX → Remove device`.)

> **#1 gotcha — read this twice.** BlueMuse manages the BLE connection
> *itself*. If the Muse is also paired in Windows Bluetooth Settings, the
> two will fight over the connection and BlueMuse will fail to stream or
> drop every few seconds. Pair once for OS-level discovery, then immediately
> unpair. You only repeat this dance if Windows "forgets" the device.

---

## Per-session: stream

1. Power on the Muse 2.
2. Launch BlueMuse from the Start menu.
3. The app auto-discovers the headset and shows it under "Available Muses".
   If not, click **Force Refresh**.
4. Click the device row → **Start Streaming**.
5. Open Settings (gear icon) and verify these are enabled (defaults are
   usually fine):
   - **EEG**: enabled
   - **PPG**: enabled (Muse 2 has a heart-rate sensor)
   - **Accelerometer + Gyroscope**: enabled
   - **Telemetry**: enabled (battery, headset state)
   - **Timestamp format**: **BlueMuse High Accuracy**
   - **Send chunked samples**: on (lower CPU overhead than per-sample)

You'll see "Streaming…" next to the device. Leave the BlueMuse window open.

Now go to [`../lab-recorder/`](../lab-recorder/README.md) to actually record.

---

## LSL streams produced

When BlueMuse is streaming a Muse 2, LabRecorder will see roughly these:

| Stream name (default)          | Type      | Channels | Rate    |
|--------------------------------|-----------|----------|---------|
| `Muse-XXXX`                    | EEG       | 4–5      | 256 Hz  |
| `Muse-XXXX_PPG`                | PPG       | 3        | 64 Hz   |
| `Muse-XXXX_Accelerometer`      | Accel     | 3        | 52 Hz   |
| `Muse-XXXX_Gyroscope`          | Gyro      | 3        | 52 Hz   |
| `Muse-XXXX_Telemetry`          | Battery   | 4        | ~0.1 Hz |

`XXXX` = last four characters of the device MAC address.

If EEG comes in as 5 channels, the 5th is "Right AUX" — a reference
electrode, not brain signal. **Drop it in your analysis** (keep TP9, AF7,
AF8, TP10).

---

## Troubleshooting

| Symptom                                 | Fix                                                                                  |
|-----------------------------------------|--------------------------------------------------------------------------------------|
| Device not in BlueMuse list             | Power-cycle the Muse, click Force Refresh. If still missing, unpair from Bluetooth Settings. |
| Pair / connection fails repeatedly      | Same: unpair from Bluetooth Settings — BlueMuse must own the connection.            |
| BlueMuse says "streaming" but LabRecorder shows nothing | Firewall is blocking `LSLBridge.exe` — see one-time setup step 3.   |
| Drops every few seconds                 | 2.4 GHz interference. Move away from microwaves / Wi-Fi access points / USB 3.0 ports. |
| `InstallBlueMuse.ps1` fails             | Did you Unblock the zip? Did you enable Developer Mode? Try the manual `.cer` route. |
| App won't launch after install          | Windows version too old (need ≥ 10.0.15063). Update Windows.                         |
| EEG looks flat for one channel          | Bad electrode contact. Re-fit the headset. The "horseshoe" indicator should be all green. |

### Logs

If you need to debug:

- **BlueMuse logs:**
  `C:\Users\<you>\AppData\Local\Packages\07220b98-ffa5-4000-9f7c-e168a00899a6_*\LocalState\Logs\`
- **LSLBridge logs:**
  `C:\Users\<you>\AppData\Local\Packages\07220b98-ffa5-4000-9f7c-e168a00899a6_*\LocalCache\Local\Logs\`

(The `_*` is BlueMuse's UWP package suffix — there will be exactly one folder
matching that pattern.)

---

[**← Prev: Data Collection (overview)**](../README.md) | [**Next: LabRecorder →**](../lab-recorder/README.md)
