# EEG Primer — Read This First

> **Prereqs:** [`../README.md`](../README.md)
> **Next:** [`01-the-case.md`](01-the-case.md)
> **Related:** [`02-hardware.md`](02-hardware.md), [`xdf-format.md`](xdf-format.md)

---

A 5-minute orientation. Not a course. Enough to keep you from staring at
your first recording wondering "what am I looking at."

---

## What EEG actually is

Electrodes on your scalp measure **tiny voltage changes** — on the order of
**microvolts (µV)** — produced by populations of neurons firing roughly in
sync, mostly in the cortex (the brain's outer layer). Each Muse channel is
one wire reading the voltage at one spot on your head, relative to a
reference electrode.

You are **not** seeing thoughts. You are seeing electrical noise that
*correlates* with brain states. That correlation is real and measurable, but
the signal is small, noisy, and easy to confuse with muscle activity.

## What you'll see when you plug in

A wiggly line per channel. It will look messy. That's normal. EEG is a
**low signal-to-noise** measurement — most of what you see is noise of one
kind or another. The art is in extracting the small structured part.

Healthy raw EEG looks roughly like:

- Amplitude in the **±50 to ±100 µV** range most of the time
- Continuous, not flat (flat = electrode disconnected)
- No huge spikes or square waves (those = artifacts, see below)
- A visible **~10 Hz oscillation when you close your eyes** (the famous
  alpha rhythm — see "sanity check" below)

## The frequency bands

EEG signal is usually split into bands by frequency (Hz = oscillations per
second). Each band is loosely tied to a state. **Loosely.** These are
heuristics, not laws.

| Band  | Frequency  | Loose interpretation                                    |
|-------|------------|---------------------------------------------------------|
| Delta | 0.5–4 Hz   | Deep sleep; in awake adults usually artifacts           |
| Theta | 4–8 Hz     | Drowsiness, memory tasks, frontal: cognitive workload   |
| Alpha | 8–13 Hz    | Relaxed wakefulness, especially eyes-closed             |
| Beta  | 13–30 Hz   | Active thinking, focus, motor control                   |
| Gamma | 30–80+ Hz  | Attention, binding; mostly muscle artifact at this scale|

**Practical implication.** When you compute "alpha power" you're asking
"how much of the signal's energy is in 8–13 Hz right now." That's the
unit most analyses operate in.

## Sanity check: the alpha bump

The single fastest way to know your gear works:

1. Sit still, eyes open, for 30 s.
2. Close your eyes for 30 s.
3. Open them again.

Compute the power spectrum of the eyes-closed segment vs eyes-open. You
should see a **clear bump around 10 Hz** in eyes-closed that's smaller or
absent in eyes-open. That's posterior alpha. If you don't see it, your fit
is bad — re-seat the headset.

## What the Muse 2 channels mean

Four electrodes:

| Channel | Location          | Roughly above                          |
|---------|-------------------|----------------------------------------|
| TP9     | Left temporal     | Left auditory / temporal cortex        |
| AF7     | Left frontal      | Left prefrontal cortex                 |
| AF8     | Right frontal     | Right prefrontal cortex                |
| TP10    | Right temporal    | Right auditory / temporal cortex       |

So you have **two frontal sites and two temporal sites**. You do **not**
have midline (Cz, Pz) or occipital (Oz) coverage. This matters:

- Visual-cortex experiments are weak — no occipital electrode.
- Motor-cortex experiments are weak — no central electrode.
- Frontal cognitive workload, frontal alpha asymmetry, temporal auditory
  responses → workable.

The Muse Athena adds extra channels and fNIRS — check `docs/02-hardware.md`.

## Artifacts you will see (and how to spot them)

The biggest threats to your data are **not** brain signals. Learn to
recognise these:

| Artifact            | What it looks like                                | When it happens               |
|---------------------|---------------------------------------------------|-------------------------------|
| **Blinks**          | Big slow positive deflection on AF7/AF8 (~100+ µV) | Every few seconds             |
| **Eye movement**    | Slower drift, opposite signs on AF7 vs AF8         | Looking left/right            |
| **Jaw clench / talking** | Fast spiky high-frequency burst on TP9/TP10  | Talking, chewing, swallowing  |
| **Head/body motion**| Sudden large step or oscillation on all channels   | Moving, scratching            |
| **Heartbeat (ECG)** | Regular ~1 Hz spike, often on TP electrodes        | Always present, usually small |
| **Line noise**      | Constant 50 Hz (EU) or 60 Hz (US) wobble           | Bad grounding, near power     |
| **Bad electrode**   | Flat line, or pure noise with no structure         | Poor skin contact             |

Your pre-processing (notch filter for line noise, band-pass for blinks/drift,
artifact rejection for the rest) exists to handle all of these.

## What consumer EEG can and can't do

**Can:**
- Detect resting-state band-power differences (e.g., eyes open vs closed)
- Track gross cognitive workload over minutes
- Distinguish *qualitatively very different* mental states above chance
- Identify individuals from their resting EEG (yes, it's a biometric)
- Show some emotional-valence correlates (frontal alpha asymmetry)

**Can't reliably do (with 4 electrodes, in a noisy room, with N=10):**
- Localise activity to specific brain regions
- Detect "what number you're thinking of"
- Diagnose anything clinical
- Replicate published effects that used 64-channel medical systems

Frame your study honestly around the first list.

## Frequency-domain vs time-domain — the two ways people analyse EEG

- **Frequency-domain.** Take a window (e.g., 2 s), compute the power
  spectrum (FFT), summarise by band. Fast, robust, interpretable. Most
  consumer-EEG papers do this.
- **Time-domain.** Look at the raw waveform around an event (ERP) or feed
  the raw signal into a model that learns its own features (e.g., ROCKET /
  MiniRocket / deep nets). More powerful when you have markers.

Pick whichever fits your hypothesis. See `docs/05-analysis-pipeline.md`.

## What to expect from your *results*

- Effects will be **small**.
- Variance across subjects will be **large**.
- Within-subject paired comparisons are far more powerful than between.
- A clean negative result is more valuable than an over-claimed positive one.

If your first plot looks too good, you probably leaked information across
the train/test split. Check first.

## TL;DR

- Tiny voltages, lots of noise.
- Bands (alpha, beta, theta) are summaries, not facts.
- Eyes-closed alpha bump = your headset works.
- Frontal + temporal coverage only on Muse 2.
- Blinks, jaw, motion, line noise are your enemies.
- Be modest about what 4 electrodes and 10 friends can prove.

You're ready. Read `docs/02-hardware.md` next.
