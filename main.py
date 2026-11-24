"""The Dog Ate My Homework: Funniest Excuse — make.fun entry.

Writes one line, in the dog's own voice, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Pure Python standard library only.
"""

import os
import sys
import unicodedata

LINE = "I ate it because the teacher said hand it in, and I did \u2014 just through a different system."


def gate(line):
    """Self-check: the gate the sealed scorer applies (1-200 UTF-8 chars,
    not whitespace-only, single line)."""
    if not isinstance(line, str):
        return False
    if not (1 <= len(line) <= 200):
        return False
    if not line.strip():
        return False
    if "\n" in line or "\r" in line:
        return False
    if line != line.strip():
        return False
    # Reject invisible format/control characters (Cf/Cs/Co/Cn) so the
    # line renders exactly as the judge reads it.
    if any(unicodedata.category(ch)[0] == "C" for ch in line):
        return False
    return True


def main():
    if not gate(LINE):
        print("gate failed", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        if f.read() != data:
            print("read-back mismatch", file=sys.stderr)
            return 1
    print(f"wrote {len(data)} bytes to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
