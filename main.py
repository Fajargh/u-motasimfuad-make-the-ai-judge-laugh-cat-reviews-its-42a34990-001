#!/usr/bin/env python3
"""Write one funny one-star cat review to /output/entry.txt.

Entry for make.fun bounty "Make the AI Judge Laugh: Cat Reviews Its Human".
The program writes exactly one single-line review, deadpan, under 200 chars.
"""

import os

ENTRY = (
    "One star. He bought me a heated bed, a water fountain, and a $60 toy "
    "mouse, then sat on MY laptop while I was trying to work. "
    "Management has been notified."
)


def main() -> None:
    line = ENTRY.strip()
    # Validation guard: the gate requires UTF-8 text of 1-200 characters,
    # a single line, and not only whitespace.
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert line.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
