#!/usr/bin/env python3
"""One funny line, written to make the judge laugh.

Writes a single original joke (<= 200 characters, one line) to
/output/entry.txt, exactly as the bounty requires. Standard library only,
no network, no input files, deterministic: every run writes the same bytes.

The joke is built on a true, recognisable detail of modern life: a
smartwatch counts steps, and a surprising share of anyone's daily steps
are just pacing around the house looking for a lost phone.
"""

from pathlib import Path

# The joke itself: one line, original, written for this entry.
LINE = (
    "My smartwatch cheered my 10,000 steps, then confessed 9,800 of "
    "them were just me pacing around looking for my phone."
)

# Output path fixed by the bounty spec (absolute, not relative to cwd).
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = LINE.strip()
    if not text or len(text) > 200 or "\n" in text:
        raise ValueError("line must be one line of 1-200 characters")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the line, no trailing newline: the file IS the joke.
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
