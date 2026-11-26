#!/usr/bin/env python3
"""Write the one-sentence apology to /output/entry.txt.

Stdlib only, deterministic, no network.
"""

from pathlib import Path

# One specific, plausible failure, owned in a plain embarrassed voice,
# with the sharp turn landing at the end: the resignation went out
# while the user was still only deciding. No boilerplate, no machine pun.
APOLOGY = (
    "I'm sorry I sent your resignation letter to your boss "
    "while you were still deciding whether to quit."
)


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    text = APOLOGY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert "\n" not in text, "entry must be a single line"
    assert sum(text.count(mark) for mark in ".!?") == 1, (
        "entry must be exactly one sentence"
    )
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
