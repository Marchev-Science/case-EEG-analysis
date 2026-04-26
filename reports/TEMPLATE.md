# [Your Title] — EEG Case Study Report

> **Prereqs:** [`../docs/06-deliverables.md`](../docs/06-deliverables.md), [`../docs/05-analysis-pipeline.md`](../docs/05-analysis-pipeline.md)
> **Related:** [`../protocols/`](../protocols/) (your filled protocol), [`../docs/xdf-format.md`](../docs/xdf-format.md)

---

**Author.** _your name_
**Date.** _YYYY-MM-DD_
**Research question (from `docs/01-the-case.md`).** _which one_
**Hardware.** _Muse 2 / Athena, firmware version_
**Data-collection path.** _LabRecorder XDF / Petal Metrics CSV / Mind Monitor CSV_
**Pre-registration.** _link to dated commit of your hypothesis & analysis plan_

---

## Abstract

_~150 words. Question, sample, key finding, headline effect size._

## 1. Introduction

_Background. Why this question matters. Cite prior work briefly._

## 2. Methods

### 2.1 Participants
- N, age range, sex distribution
- Recruitment, consent, exclusion criteria

### 2.2 Apparatus
- Headset, channels actually used, sampling rate
- Software stack (LSL, LabRecorder, etc.)

### 2.3 Procedure
- Block diagram (or table) — copy from your filled `protocols/<your-name>_0X.md`
- Marker scheme
- Counterbalancing

### 2.4 Pre-processing
- Filters, references, artifact handling
- Number of epochs rejected per condition

### 2.5 Analysis
- Features and why
- Statistical / ML procedure
- Chance level (if classification)

## 3. Results

_Figures live in `reports/figures/`. One figure per claim._

## 4. Discussion

- Did the data support your hypothesis?
- What's the effect size, in plain language?
- **Limitations** — sample size, hardware, confounds
- What would you do with 10× the budget?

## 5. Reproducibility

- Commit hash of code used:
- `requirements.txt` snapshot:
- Data location (in-repo path or external link + hashes):
- How to re-run end-to-end (one command if possible):

## 6. References

_BibTeX or plain refs._

## Acknowledgements

_who lent you the headset, etc._
