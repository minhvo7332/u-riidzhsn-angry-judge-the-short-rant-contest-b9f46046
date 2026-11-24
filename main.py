#!/usr/bin/env python3
"""Self-Checkout Accusation v1: 390 characters, one milk, zero mercy.

Entry for make.fun's "Angry Judge: The Short Rant Contest"
(u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046).

The program writes one short, funny rant to /output/entry.txt.
It is fully deterministic: the same fixed text on every run, no
randomness, no network, no clock, no environment input.

The rant: a self-checkout machine accuses an innocent shopper of
stealing her own milk. One concrete humiliation, escalated in
three beats -- the false accusation, the public shame, the apology
to a machine -- and a killer last line. Specific, visual, and
angry in a way anyone who has fought a self-checkout recognises.
"""

import os
import stat

RANT = (
    "The self-checkout scanned my milk twice, then accused me of stealing it. "
    "'Unexpected item in the bagging area.' The item was the milk. "
    "The bagging area was where the milk goes. "
    "The woman behind me sighed like I had delayed her funeral. "
    "So I apologised - to a machine. "
    "I stood there saying sorry to a screen while my milk sat in jail. "
    "I am still apologising. The machine has not forgiven me."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = "entry.txt"


def main() -> None:
    # The rant must be 1-400 characters of UTF-8 text, not whitespace only.
    text = RANT
    assert 1 <= len(text) <= 400, f"rant is {len(text)} chars, must be 1-400"
    assert text.strip(), "rant must not be whitespace only"
    text.encode("utf-8")  # fail loudly if the text ever stops being UTF-8

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(path, 0o644)
    os.chmod(OUTPUT_DIR, 0o755)


if __name__ == "__main__":
    main()
