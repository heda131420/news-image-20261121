"""Deliver the finished front page to the grader.

The picture is the entry: a one-page newspaper summing up Saturday
21 November 2026, rendered once and stored here as entry.png. The
grader runs this file with no network and nothing beyond the standard
library, so the program only copies those exact bytes into the output
folder the grader provides. Run it locally with
MAKEFUN_OUTPUT_DIR=out python3 main.py to see the same result.
"""

import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    if not os.path.isfile(SOURCE):
        sys.exit("entry.png is missing next to main.py")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    os.chmod(dest, 0o644)


if __name__ == "__main__":
    main()
