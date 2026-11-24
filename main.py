"""Two Days of Quiet Dread — one-line code review comment.

Writes a single line (<=140 chars) to /output/entry.txt: a code review
comment that approves a pull request while carrying quiet existential
dread. No network, no randomness, no arguments.
"""

import os

ENTRY = (
    "LGTM. Green tests, clean diff, and the quiet knowledge "
    "that this code will outlive us both and still not care."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
