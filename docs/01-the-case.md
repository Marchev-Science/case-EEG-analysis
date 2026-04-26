# 01 — The Case

> **Prereqs:** [`eeg-primer.md`](eeg-primer.md)
> **Next:** [`02-hardware.md`](02-hardware.md)
> **Related:** [`../protocols/`](../protocols/) (one template per question)

---

This document expands the five research questions. You are not required to
address all of them — pick one and go deep.

---

## 1. Brain activity while using AI

**Question.** Does the EEG signature of "programming with an AI assistant"
differ from "programming without AI" and from a low-engagement baseline (e.g.,
watching a sports broadcast for a team you don't care about)?

**Suggested conditions.**
- Baseline: passive video watching, neutral content
- Coding alone: writing a small program from a prompt
- Coding with AI: same task, with Copilot / Claude / Cursor

**Hypotheses to consider.** Frontal alpha asymmetry, theta–beta ratio, workload
indices (frontal theta + parietal alpha).

---

## 2. Person identification (biometric EEG)

**Question.** Given recordings of the *same* activity across multiple people,
can a model identify the individual from EEG alone?

**Optional extension.** Correlate identifiability or feature clusters with
Myers–Briggs type or Big Five scores collected via questionnaire.

**Suggested approach.** Within-subject vs. between-subject classification;
LOSO cross-validation; report chance level explicitly.

---

## 3. Activity classification

**Question.** Can EEG distinguish between qualitatively different cognitive
activities?

**Suggested activity set.**
- Video game (deterministic vs. stochastic)
- Online shopping (descriptive, discrete decision-making)
- Financial-market analysis (analytic, continuous)
- Intelligence / reasoning test

**Approach.** Multi-class classification, balanced design, per-subject and
across-subject evaluation.

---

## 4. Sex differences in resting / low-activity EEG

**Question.** At rest, or during low-cognitive-load tasks, are there reliable
EEG differences between male and female participants?

**Caveats.** Small samples are the norm here — be honest about effect sizes
and confidence intervals. Pre-register your analysis if possible.

---

## 5. Attention span

**Question.** How does sustained attention measured via EEG vary with content
type and length?

**Suggested manipulation.** 2 × 2 design — short (≤2 min) vs. long (≥10 min)
× instructional vs. entertainment.

**Markers.** Engagement indices, alpha power decay over time, microstate
transitions.

---

## Cross-cutting requirements

For *whichever* question you pick, your study must specify:

- [ ] Sample size and recruitment
- [ ] Inclusion/exclusion criteria
- [ ] Per-condition recording length
- [ ] Marker / event scheme
- [ ] Pre-registered hypothesis or clearly labelled exploratory analysis
- [ ] Pre-processing pipeline
- [ ] Statistical / ML evaluation protocol with chance level
- [ ] Limitations

---

[**← Prev: EEG Primer**](eeg-primer.md) | [**Next: 02 — Hardware →**](02-hardware.md)
