"""Everyday Wonder — one sentence about a small everyday moment.

The entry is a single sentence, written to /output/entry.txt.
Python 3.13, standard library only.
"""

from pathlib import Path

SENTENCE = (
    "The escalator handrail moved faster than the steps, "
    "so my hand reached the top a moment before the rest of me did."
)

OUTPUT_PATH = Path("/output/entry.txt")


def validate(sentence: str) -> str:
    """The gate accepts UTF-8 text of 1 to 200 characters, not only whitespace."""
    text = sentence.strip()
    if not text:
        raise ValueError("sentence is empty")
    if len(text) > 200:
        raise ValueError(f"sentence is {len(text)} characters, over the 200 limit")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    return text


def main() -> None:
    text = validate(SENTENCE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
