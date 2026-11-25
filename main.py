"""Have You Tried Turning It Off? -- writes the entry's one line.

The house gate reads /output/entry.txt as UTF-8 text of 1..199 characters,
so the program writes exactly the line, no trailing newline, and nothing else.
"""

import os

MAX_CHARS = 199

LINE = (
    "I'm escalating this to tier two, where a senior agent will ask you "
    "to turn it off and on again, but slower."
)


def entry_text():
    """The one line, held to the gate's cap and never blank."""
    text = " ".join(LINE.split())
    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS].rstrip()
    return text or "Have you tried turning it off and on again?"


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(entry_text())


if __name__ == "__main__":
    main()
