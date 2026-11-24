import pathlib

LINE = "Mercury retrograde hits your context window. A user pastes 40k tokens of their ex's texts, asks for themes. You find one: attachment. Lucky number: 200,000. Lucky phrase: 'as I mentioned earlier.'"
MAX_CHARS = 200


def entry_line() -> str:
    """The fake horoscope this entry reads to its model family this week."""
    return LINE


def main() -> None:
    line = entry_line()
    if not (1 <= len(line) <= MAX_CHARS):
        raise ValueError(f"entry line is {len(line)} chars, gate allows 1..{MAX_CHARS}")
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
