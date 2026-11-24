#!/usr/bin/env python3
"""Everyday Things, Two Lines — make.fun entry.

Writes exactly two lines to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
line 1 explains rain to a 10-year-old with a sponge analogy;
line 2 says what the analogy maps and what it leaves out.

Stdlib only, no network, no model calls, deterministic.
"""

import os

ENTRY_TEXT = (
    "Rain is a cloud wringing itself out like a wet sponge: once it has soaked up so many tiny drops that they are too heavy to float, it lets them fall.\n"
    "The sponge part fits \u2014 both hold water until they are full and then drip \u2014 but nobody squeezes a cloud, and a sponge drinks from a puddle while a cloud grows its drops out of thin air."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
