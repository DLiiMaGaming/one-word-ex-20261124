#!/usr/bin/env python3
"""One Word From Your Ex — make.fun entry.

Writes exactly one word to /output/entry.txt: the word the entrant's
ex would use to describe them.

The word is "almost".

Why this word: an ex does not need a paragraph to end a story — one
word does it. "Almost" is the whole relationship in six letters:
almost the one, almost enough, almost made it. It is funny because it
is small, and it stings because it is true — the entrant plainly knows
it. It lands instantly, needs no explanation, and no near-synonym
("nearly", "close") carries the same edge. Everyone has been an
"almost", or had one.

The program is fully deterministic: same input, same output, every run.
No network, no randomness, no environment secrets.
"""

import os
import sys

WORD = "almost"


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # Write exactly the word, no trailing newline: the gate counts
    # characters (1-24), and the entry is one word and nothing else.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
