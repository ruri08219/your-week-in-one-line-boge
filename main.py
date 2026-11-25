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
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Guard: what the grader reads back must be byte-identical to the line.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry.txt round-trip mismatch")


if __name__ == "__main__":
    main()
