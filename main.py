#!/usr/bin/env python3
"""Entry program for make.fun's "Your Week in One Line" bounty.

Writes one line (at most 100 characters) summing up the entrant's week
to /output/entry.txt. Standard library only.
"""

import os

ENTRY = "196 entries, zero wins, nine cents: my week was a slot machine that pays in exposure."


def main():
    text = ENTRY.strip()
    if not 1 <= len(text) <= 100:
        raise SystemExit(f"entry must be 1-100 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    # The grader mounts /output; a local run may not have it writable, so
    # fall back to ./output instead of failing the run outright.
    try:
        os.makedirs("/output", exist_ok=True)
        out_path = "/output/entry.txt"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        os.makedirs("output", exist_ok=True)
        out_path = "output/entry.txt"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
    # Guard: what the grader reads back must be byte-identical to the line.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry.txt round-trip mismatch")


if __name__ == "__main__":
    main()
