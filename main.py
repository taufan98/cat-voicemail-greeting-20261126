#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — make.fun entry.

Writes one original voicemail greeting, as recorded by a cat, to
/output/entry.txt (fallback ./output/entry.txt). The sealed gate requires
UTF-8 text of 1-120 characters, a single line, not only whitespace.
"""

LINE = "You've reached the cat. I'm napping in a box. Leave food \u2014 I mean, a message \u2014 after the beep. I'll ignore it at 4 a.m."

MAX_CHARS = 120


def main() -> None:
    line = LINE
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, f"entry is {len(line)} chars, limit {MAX_CHARS}"
    assert line.strip(), "entry must not be only whitespace"

    import os

    out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)

    # Read the file back and verify the exact bytes.
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    assert back == line, "read-back mismatch"
    assert len(back) == len(line)
    print(f"Wrote {len(back)} chars to {path}")


if __name__ == "__main__":
    main()
