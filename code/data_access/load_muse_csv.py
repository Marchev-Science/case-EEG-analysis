"""Load EEG + markers from Petal Metrics / Mind Monitor CSV files.

STUB — implement this for your study.
"""

from __future__ import annotations

from pathlib import Path

from .load_xdf import Recording


def load_muse_csv(eeg_csv: str | Path, events_csv: str | Path | None = None) -> Recording:
    """Load a Muse CSV recording, optionally pairing with an events CSV.

    Hints:
        import pandas as pd
        df = pd.read_csv(eeg_csv)
        # Mind Monitor columns typically include: TimeStamp, RAW_TP9,
        # RAW_AF7, RAW_AF8, RAW_TP10, plus precomputed band powers.
    """
    raise NotImplementedError("Implement load_muse_csv for your study.")
