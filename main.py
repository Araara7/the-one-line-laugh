"""The One-Line Laugh — entry program.

Writes a single funny line (one sentence, at most 200 characters) to
/output/entry.txt. The line is a fixed, deterministic string: the joke is
chosen once, not generated at run time, so every run produces byte-identical
output.

The joke's shape: a setup that sounds like a productivity win ("six hours on
productivity apps") and a turn at the very end that flips it ("mostly deleting
the productivity apps") — an everyday truth about screen-time reports, with
nothing left to explain.
"""

import os

LINE = "My phone's screen time report says I spent six hours on productivity apps, mostly deleting the productivity apps."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.count(".") == 1, "entry must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
