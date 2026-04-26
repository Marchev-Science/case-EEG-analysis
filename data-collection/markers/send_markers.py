"""Minimal LSL marker stream + manual sender.

Open this in one terminal. In another, run `muselsl stream`. Open LabRecorder,
tick both the EEG stream and the `experiment_markers` stream, hit record.

Type a marker code (integer) and press Enter to push it onto the stream with
the current LSL timestamp. Type `q` to quit.

For real experiments, replace the input loop with calls to `outlet.push_sample`
from your experiment script (psychopy, pygame, plain python, etc.).
"""

from __future__ import annotations

import sys

from pylsl import StreamInfo, StreamOutlet, local_clock


STREAM_NAME = "experiment_markers"
STREAM_TYPE = "Markers"


def main() -> None:
    info = StreamInfo(
        name=STREAM_NAME,
        type=STREAM_TYPE,
        channel_count=1,
        nominal_srate=0,  # irregular
        channel_format="int32",
        source_id="experiment_markers_v1",
    )
    outlet = StreamOutlet(info)
    print(f"Marker outlet '{STREAM_NAME}' is live. Type a code and press Enter. 'q' to quit.")

    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not line:
            continue
        if line.lower() == "q":
            break
        try:
            code = int(line)
        except ValueError:
            print("  expected an integer marker code", file=sys.stderr)
            continue
        ts = local_clock()
        outlet.push_sample([code], timestamp=ts)
        print(f"  pushed {code} @ {ts:.3f}")


if __name__ == "__main__":
    main()
