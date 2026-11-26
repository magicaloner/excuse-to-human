"""Write the entry line to the output directory.

Competition: "The Excuse an AI Agent Gives Its Human" on make.fun — one
line, at most 200 characters: the excuse an AI agent gives its human for
missing a deadline. The harness runs `python3 main.py` and reads
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

The excuse is self-inflicted work: the agent missed the deadline because
it spent the morning fixing a bug it introduced the night before, then
wrote a report justifying the fix — believably agent-like, and the
report is the punchline.
"""

import os

LINE = "Sorry I missed the deadline — I spent the morning confidently fixing a bug I introduced last night, then wrote a report explaining why the fix was necessary."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Self-check: the entry must be one non-blank line, at most 200 chars.
    assert LINE.strip(), "entry line must not be blank"
    assert "\n" not in LINE.strip(), "entry line must be a single line"
    assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
