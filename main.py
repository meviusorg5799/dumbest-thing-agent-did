"""Write the dumbest-thing entry to /output/entry.txt.

The entry text lives in entry.txt beside this script, so it is kept in
exactly one place. This program copies it to the output directory
(MAKEFUN_OUTPUT_DIR when set, else /output), deterministic and
stdlib-only: no clock, no network, no randomness.
"""

import os
import sys
from pathlib import Path


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    entry_path = script_dir / "entry.txt"
    text = entry_path.read_text(encoding="utf-8")
    line = text.rstrip("\n")
    # Fail loudly rather than emitting an invalid entry: the sealed
    # scorer only accepts a single line of 1-200 characters, not
    # only white space.
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200 or not line.strip():
        raise ValueError(
            f"entry must be 1-200 non-blank characters, got {len(line)}"
        )
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
