#!/usr/bin/env python3
"""Write the make.fun bounty entry text to entry.txt.

Standard library only, no network. The text is a single constant; the
program writes it as UTF-8 bytes with no trailing newline.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "The waiting-room fish has a name tag on his bowl: Gerald. "
    "Gerald has been dead since Tuesday. The tag is new."
)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, (
        f"entry text must be between 1 and 280 characters, got {len(TEXT)}"
    )
    target = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir = Path(target)
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_bytes(TEXT.encode("utf-8"))
    print(f"{len(TEXT)} characters written to {entry}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
