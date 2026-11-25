#!/usr/bin/env python3
"""The One-Liner Groan-Off: one original dad joke, one line, <=140 chars.

Writes the joke to $MAKEFUN_OUTPUT_DIR/entry.txt (or ./entry.txt when the
variable is absent, for local smoke tests).
"""

import os

JOKE = (
    "Dad caught me checking if the fridge light stays on. "
    "He said, 'It does \u2014 and it's the only thing in this house "
    "with a bright future.'"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE
    assert 1 <= len(text) <= 140, f"joke is {len(text)} chars, must be 1-140"
    assert text.strip(), "joke must not be whitespace-only"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
