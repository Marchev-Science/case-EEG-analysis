# References

> **Related:** [`../docs/05-analysis-pipeline.md`](../docs/05-analysis-pipeline.md), [`../docs/eeg-primer.md`](../docs/eeg-primer.md), [`../docs/xdf-format.md`](../docs/xdf-format.md)

---

A starter reading list. Add your own as you go.

## Reference implementation

- **NeuroSense-Modules** — end-to-end Muse EEG pipeline in Python
  (XDF loader, FIR filter, KNN ocular removal, MiniRocket features, SVM with
  LOSO). Use as a *reference*, not a drop-in solution.
  https://github.com/a1441/NeuroSense-Modules

## Source paper for the reference pipeline

- "NeuroSense: A Novel EEG Dataset Utilizing Low-Cost, Sparse Electrode
  Devices for Emotion Exploration." *IEEE Access*, 2024.

## Muse-specific validation

- Krigolson et al. (2017). "Choosing MUSE: validation of a low-cost,
  portable EEG system for ERP research." *Frontiers in Neuroscience*.
- Cannard et al. (2021). "Validating the wearable MUSE headset for EEG
  spectral analysis."

## Methods textbooks

- Cohen, M. X. (2014). *Analyzing Neural Time Series Data*. MIT Press.
- Luck, S. J. (2014). *An Introduction to the Event-Related Potential
  Technique* (2nd ed.).

## Tooling

- MNE-Python — https://mne.tools
- sktime / MiniRocket — https://www.sktime.net
- LSL / LabRecorder — https://labstreaminglayer.org
- muselsl — https://github.com/alexandrebarachant/muse-lsl
- pyxdf — https://github.com/xdf-modules/pyxdf

## Open EEG datasets (for benchmarking)

- PhysioNet EEG datasets — https://physionet.org/about/database/
- OpenNeuro — https://openneuro.org

## Ethics & pre-registration

- OSF Pre-registration — https://osf.io/prereg/
- Equator network reporting guidelines — https://www.equator-network.org/
