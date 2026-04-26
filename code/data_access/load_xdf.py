"""Load EEG + markers from a LabRecorder .xdf file.

STUB — implement this for your study. See module README for the expected
return contract.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np


@dataclass
class Recording:
    eeg: np.ndarray            # (n_channels, n_timepoints)
    times: np.ndarray          # (n_timepoints,) seconds
    channel_names: list[str]
    sample_rate: float
    markers: list[tuple[float, int | str]]


def load_xdf(path: str | Path) -> Recording:
    """Load an XDF recording.

    Hints:
        import pyxdf
        streams, _ = pyxdf.load_xdf(path)
        eeg = next(s for s in streams if s["info"]["type"][0] == "EEG")
        markers = next((s for s in streams if s["info"]["type"][0] == "Markers"), None)
        # Drop 'Right AUX' channel for Muse 2 — keep TP9, AF7, AF8, TP10 only.
    """
    raise NotImplementedError("Implement load_xdf for your study.")
