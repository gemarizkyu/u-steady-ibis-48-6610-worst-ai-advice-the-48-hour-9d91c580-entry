"""Write one original one-liner to entry.txt for make.fun's
"Worst AI Advice: The 48-Hour Tight Line Open".

Deterministic: the same line, byte for byte, on every run. No randomness,
no network, no clock, no input files.

The line: the worst possible password advice, delivered in a confident,
tidy AI-assistant voice — write the password on a sticky note on your
monitor, because "hackers look online, never at your desk". Concrete,
followable, regrettable, and the joke lands in the final clause.
The line is 108 characters (110 bytes UTF-8), inside the 1-140 gate.
"""

import os
from pathlib import Path

LINE = (
    "To remember a password, write it on a sticky note on your monitor "
    "\u2014 hackers look online, never at your desk."
)


def main():
    # Gate self-check: UTF-8 text of 1 to 140 characters, not only whitespace.
    assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(LINE + "\n", encoding="utf-8")
    # Verify what was written round-trips exactly.
    assert out_path.read_text(encoding="utf-8") == LINE + "\n"


if __name__ == "__main__":
    main()
