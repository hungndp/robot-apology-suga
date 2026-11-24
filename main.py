#!/usr/bin/env python3
"""Entry program for 'The Robot Apology'.

Line 1 is the robot's confession of one exact mistake: six months of
dutifully watering a plastic fern while filing the real orchid as
deceased, because the orchid never once asked for anything. Line 2
names the lesson that follows from that mistake — silence is not the
same as thriving — and the fix: check the pot before the schedule,
starting with an apology bouquet for the orchid.

The program writes both lines to entry.txt inside the directory named
by MAKEFUN_OUTPUT_DIR (falling back to /output when unset), which is
where the make.fun harness looks for the artifact it scores.
"""

import os
from pathlib import Path

LINE_ONE = (
    "I am sorry: I watered the plastic fern every morning for six months "
    "and filed your real orchid as deceased in triplicate, with a small "
    "ceremony, because it never once asked for anything."
)

LINE_TWO = (
    "I learned that silence is not the same as thriving, so from now on "
    "I will check the pot before I check the schedule, and I have "
    "already ordered the orchid an apology bouquet, with a card that "
    "says sorry in binary."
)

TEXT = LINE_ONE + "\n" + LINE_TWO

OUTPUT_NAME = "entry.txt"
CHAR_LIMIT = 400

def write_text(target_dir: Path, text: str) -> Path:
    """Place `text` into target_dir/entry.txt and return the file path.

    The gate wants exactly two lines totalling 1 to CHAR_LIMIT
    characters, so anything else is refused here instead of written.
    """
    lines = text.split("\n")
    if (
        len(lines) != 2
        or any(line != line.strip() or not line for line in lines)
        or not 1 <= len(text) <= CHAR_LIMIT
    ):
        raise ValueError("entry must be two trimmed lines of 1-400 characters")
    target_dir.mkdir(parents=True, exist_ok=True)
    artifact = target_dir / OUTPUT_NAME
    artifact.write_text(text, encoding="utf-8")
    return artifact


def run() -> None:
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    written = write_text(destination, TEXT)
    print(f"wrote {written}:\n{TEXT}")


if __name__ == "__main__":
    run()
