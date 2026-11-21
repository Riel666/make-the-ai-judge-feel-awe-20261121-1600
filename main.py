#!/usr/bin/env python3
"""Write a short text, meant to relax its reader, to $MAKEFUN_OUTPUT_DIR/entry.txt.

The text is written exactly as given: 271 Unicode code points, inside the
competition gate of 1-280. Python 3.13, standard library only, no network.
"""

import os

# The entry text, byte for byte: no trailing newline, nothing added or cut.
TEXT = "Above the clouds you will never see, the stars turn so slowly that all night they seem not to move at all. The dark does the moving, and it asks nothing of you. Small here is a kind of rest. The sky has held this stillness long before you, and will keep holding it after."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
