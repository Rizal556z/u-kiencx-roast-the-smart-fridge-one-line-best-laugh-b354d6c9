"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes a single original roast line to /output/entry.txt.
Pure Python standard library only; no network, no secrets.
"""

import os

ENTRY = "My smart fridge pings my phone 'again?' every time I open it after midnight — a snitch with a lightbulb and a superiority complex."

assert isinstance(ENTRY, str)
assert 1 <= len(ENTRY) <= 160, f"entry must be 1-160 chars, got {len(ENTRY)}"
assert "\n" not in ENTRY, "entry must be exactly one line"
assert ENTRY.strip(), "entry must not be only whitespace"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
