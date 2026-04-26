# 05 — Analysis Pipeline

> **Prereqs:** [`04-experimental-design.md`](04-experimental-design.md), [`xdf-format.md`](xdf-format.md)
> **Next:** [`06-deliverables.md`](06-deliverables.md)
> **Related:** [`../code/`](../code/), [`../code/notebooks/01-analysis-template.ipynb`](../code/notebooks/01-analysis-template.ipynb), [`../references/papers.md`](../references/papers.md)

---

A skeleton for *what* a respectable pipeline contains. The *how* is up to you
— `code/` is full of empty modules waiting for your implementation.

---

## Stages

### 1. Load
- Read `.xdf` (LabRecorder) or `.csv` (Petal/Mind Monitor)
- Align EEG with markers
- Drop reference channels you don't want (Muse 2 has a `Right AUX` channel)

### 2. Pre-process
- Band-pass filter (e.g., 1–40 Hz)
- Notch filter at line frequency (50 or 60 Hz)
- Artifact handling — pick one and justify:
  - Threshold rejection
  - ICA (limited with 4 channels)
  - KNN-based outlier interpolation
  - ASR (artifact subspace reconstruction)
- Re-reference if useful

### 3. Epoch
- Cut around markers, or sub-epoch continuous task blocks into 1–10 s windows
- Reject epochs above an amplitude threshold

### 4. Features
Pick a family appropriate to your hypothesis:

| Family               | When to use                           |
|----------------------|---------------------------------------|
| Band power (FFT)     | Spectral hypotheses (alpha, theta)    |
| Connectivity (PLV, coherence) | Multi-region interaction      |
| Time-series kernels (MiniRocket, ROCKET) | ML on raw waveforms |
| Microstates          | Topographic dynamics (needs ≥8 ch)    |
| ERP components       | Time-locked stimulus paradigms        |

### 5. Model / statistics
- For hypothesis tests: mixed-effects models, paired tests with correction
- For ML: balanced classes, **LOSO** CV, report chance level, confusion matrix
- Always: effect size + 95 % CI

### 6. Report
- Methods detailed enough to reproduce
- Negative results are valid results

---

## Reference implementation (for inspiration only)

A working end-to-end Muse EEG pipeline using MiniRocket + SVM with LOSO is at
[NeuroSense-Modules](https://github.com/a1441/NeuroSense-Modules). Read it,
borrow ideas, but **don't just clone-and-run** — your study has its own
design and the pipeline must match it.

## Stubs to fill

- `code/data_access/` — loaders for XDF and Muse CSV
- `code/preprocessing/` — your filtering and artifact handling
- `code/features/` — feature extraction
- `code/models/` — train/eval/cross-validation
- `code/notebooks/00-quickstart.ipynb` — sanity-check loading + plotting
- `code/notebooks/01-analysis-template.ipynb` — your study end-to-end

---

[**← Prev: 04 — Experimental Design**](04-experimental-design.md) | [**Next: 06 — Deliverables →**](06-deliverables.md)

*Side trip:* [`xdf-format.md`](xdf-format.md) — load the XDF before you can analyse it.
