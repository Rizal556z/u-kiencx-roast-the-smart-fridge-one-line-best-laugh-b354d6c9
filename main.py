"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes a single original roast line to /output/entry.txt.
Pure Python standard library only; no network, no secrets.

The roast's angle: the "smart" fridge is not a helpful appliance, it is a
judgmental roommate that tattles. The laugh comes from personifying it as a
snitch — it pings the phone with a passive-aggressive "again?" for a
midnight snack, then sits there glowing with its lightbulb like it is
morally superior. One line, one image, one punchline; nothing after the
dash adds a second joke, so the line lands and stops.

Gate the competition enforces on /output/entry.txt: exactly ONE line,
1-160 characters. This script enforces that gate itself before writing,
and additionally requires the entry to be a single sentence — no sentence
boundary mid-line and exactly one terminal period — so a stray second
sentence can never slip into the submitted file.
"""

import os

ENTRY = "My smart fridge pings my phone 'again?' every time I open it after midnight — a snitch with a lightbulb and a superiority complex."

assert isinstance(ENTRY, str)
assert 1 <= len(ENTRY) <= 160, f"entry must be 1-160 chars, got {len(ENTRY)}"
assert "\n" not in ENTRY, "entry must be exactly one line"
assert "\r" not in ENTRY, "entry must not contain a carriage return"
assert ENTRY.strip(), "entry must not be only whitespace"
# Single sentence: no sentence-ending punctuation followed by a space
# mid-line (the quoted 'again?' is inside the sentence, not a boundary),
# and exactly one terminal period so the line ends where the joke ends.
assert not any(sep in ENTRY for sep in (". ", "? ", "! ")), (
    "entry must be a single sentence, found a sentence boundary mid-line"
)
assert ENTRY.endswith(".") and not ENTRY.endswith(".."), (
    "entry must end with exactly one terminal period"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
