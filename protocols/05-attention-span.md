# Protocol 05 — Attention Span Across Content Types

> Copy this file to `protocols/<your-name>_05.md` and fill in the TODOs.

## Hypothesis

> _Example: "Engagement (frontal theta + parietal alpha decrement) will
> decline more steeply during long entertainment videos than during long
> instructional videos."_

## Design — 2 × 2

|                | Short (≤2 min) | Long (≥10 min) |
|----------------|----------------|----------------|
| Instructional  | block IS       | block IL       |
| Entertainment  | block ES       | block EL       |

Order counterbalanced. Insert 60 s rest between blocks.

| Marker | Meaning |
|--------|---------|
| 1 | EO baseline |
| 2 | EC baseline |
| 11 | Short instructional start |
| 12 | Long instructional start |
| 21 | Short entertainment start |
| 22 | Long entertainment start |
| 99 | Rest |

## Stimuli

- IS: _link_
- IL: _link_
- ES: _link_
- EL: _link_

## Subject instructions

> _verbatim_

## Analysis plan

- Compute engagement index over sliding windows
- Test slope of engagement-vs-time per condition
- Mixed-effects model: subject as random effect, content × duration as fixed
- Report effect sizes
