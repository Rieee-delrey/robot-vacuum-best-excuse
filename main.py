#!/usr/bin/env python3
"""Write the robot vacuum's best excuse to /output/entry.txt.

The entry is one line, 1-140 characters. This version validates the
text before writing and reads it back to confirm the exact bytes
landed on disk.
"""

import os

ENTRY = "My dustbin was full, so I saved that spot for later. It is still there. I am still full."


def main():
    text = ENTRY
    if not text or text != text.strip():
        raise ValueError("entry must be non-blank text")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 140:
        raise ValueError("entry must be 1-140 characters, got %d" % len(text))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        raise ValueError("read-back mismatch: entry bytes differ from source")


if __name__ == "__main__":
    main()
