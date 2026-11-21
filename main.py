"""Write one short relaxing text to /output/entry.txt.

Entry for make.fun's "Make the AI judge feel brave" bounty.
Deterministic, no network, no randomness: the same text every run.
"""

import os

TEXT = (
    "Rain threads the window, slow as a needle through cloth. "
    "The kettle clicks off before it boils. "
    "Somewhere a dog sighs in its sleep, and the house settles too. "
    "For once, nothing is asking anything of you — no verdict, no next page. "
    "Just rain, a room, one unhurried minute."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
