#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800: writes one sentence explaining the
modern internet to someone from 1800, to /output/entry.txt.

The sentence uses only things a person from 1800 already knows — a library,
a post office, a letter, ink — to carry the internet's two defining acts:
all knowledge gathered in one place, and messages that arrive instantly.
"""

LINE = (
    "Imagine every library on earth joined into one, with a post office "
    "inside it that delivers any letter to the far side of the world "
    "before the ink dries."
)

# The gate: /output/entry.txt must hold 1 to 200 characters of real text.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "line must be 1-200 characters"
# And it must be exactly one sentence: no line breaks, a single full stop.
assert "\n" not in LINE and LINE.count(".") == 1, "entry must be a single sentence"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
