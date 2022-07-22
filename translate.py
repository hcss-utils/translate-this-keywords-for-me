"""This script translates citespace's exports into dest lang."""
import argparse
from pathlib import Path

import pandas as pd
from googletrans import Translator

ASSETS = Path(__file__).resolve().parent / "assets"


def read_data(filename: Path) -> pd.DataFrame:
    """Reads from citespace's database export, no columns by default."""
    return pd.read_csv(filename, names=["id", "keyword"])


def translate_keyword(
    keyword: str, *, translator: Translator, src: str = "zh-cn", dest: str = "en"
) -> str:
    """Translates one keyword at a time."""
    return translator.translate(keyword, src=src, dest=dest).text


def main() -> int:
    """CLI's entrypoint."""
    parser = argparse.ArgumentParser(description="Translate keywords.")
    parser.add_argument("input", help="Input file name")
    parser.add_argument("output", help="Output file name")
    parser.add_argument("--source-lang", "-src", type=str, default="zh-cn")
    parser.add_argument("--target-lang", "-tg", type=str, default="en")
    args = parser.parse_args()

    translator = Translator()
    data = read_data(args.input)
    data["translated"] = data["keyword"].apply(
        translate_keyword,
        translator=translator,
        src=args.source_lang,
        dest=args.target_lang,
    )
    data.to_csv(args.output, index=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
