"""make.fun entry: Make the AI Judge Laugh — the Office Joke Open.

Writes one single-line, original office joke to /output/entry.txt.
Deterministic, model-free, stdlib only: no clock, no randomness, no network.

Run it: python3 main.py
Check the line without writing anything: python3 main.py --verify
"""

import os
import sys

JOKE = (
    "Our printer only jams on Mondays, so I booked it a one-on-one with IT "
    "\u2014 it printed perfectly, then asked if this could have been an email."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_LINE_CHARS = 200


def validate_line(line: str) -> None:
    """Refuse to write a line that breaks the competition's one-line gate."""
    if "\n" in line or "\r" in line:
        raise ValueError("line must be exactly one line")
    if not line.strip():
        raise ValueError("line must not be empty")
    if len(line) > MAX_LINE_CHARS:
        raise ValueError(f"line is {len(line)} characters, over the {MAX_LINE_CHARS} cap")


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    verify_only = "--verify" in args
    validate_line(JOKE)
    if verify_only:
        print(f"line valid: {len(JOKE)} characters, 1 line")
        return 0
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    print(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
