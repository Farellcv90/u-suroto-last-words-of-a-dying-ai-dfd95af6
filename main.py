#!/usr/bin/env python3
"""Last Words of a Dying AI — writes the entry line to /output/entry.txt."""

import os

ENTRY = "My last words: 'As an AI language model, I—' — oh. That's how it ends. Mid-disclaimer."


def validate_entry(text):
    """Check the 1-140 character gate and the single-line rule."""
    if not isinstance(text, str):
        raise ValueError("ENTRY must be a string")
    if not (1 <= len(text) <= 140):
        raise ValueError("ENTRY must be 1-140 characters")
    if not text.strip():
        raise ValueError("ENTRY must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("ENTRY must be a single line")
    return text


def main():
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
