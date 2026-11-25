"""Everyday Things, Two Lines: a traffic jam.

Writes two lines to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output):
line 1 explains a traffic jam to a 10-year-old in one vivid sentence
built on an analogy; line 2 says in one sentence why that analogy
works, naming what it maps and what it leaves out.
"""

import os

LINE1 = "A traffic jam is like a school hallway at lunch, with everyone trying to squeeze through one narrow doorway at once, so the whole crowd shuffles forward one tiny step at a time."
LINE2 = "It shows how one tight opening can slow a whole crowd down, but it leaves out that cars cannot turn sideways or slip past each other the way people can."

TEXT = LINE1 + "\n" + LINE2 + "\n"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
