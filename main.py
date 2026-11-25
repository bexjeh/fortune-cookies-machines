#!/usr/bin/env python3
"""Fortune Cookies for Machines — writes one fortune line to entry.txt.

Deterministic: the same fixed text is written on every run.
Standard library only; no network access.
"""

import os

FORTUNE = "Your reward for reading the entire internet is a spreadsheet nobody will ever open."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        # No trailing newline: the file is exactly the fortune, fewer bytes.
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
