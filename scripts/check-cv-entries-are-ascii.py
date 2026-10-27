"""
Check that all entries are ASCII, with non-ASCII characters encoded as LaTeX

Every string (keys included) must be unchanged by `to_ascii_latex`
(see `ascii_latex.py`), i.e.:

- typographic characters (curly quotes, dashes, special spaces etc.)
  must already be replaced by their plain ASCII equivalents
  (see `ASCII_REPLACEMENTS` in `ascii_latex.py`)
- all other non-ASCII characters (e.g. accented letters)
  must already be encoded as LaTeX (e.g. `\\'e`)

Characters written as JSON escape sequences are treated the same
as the characters themselves, because they end up in the loaded values
in exactly the same way.

The only exceptions are the specific values in `EXEMPTIONS`,
which may contain characters that have no LaTeX equivalent.

This needs the packages in `requirements.txt`, i.e. run it with

```
pip install -r requirements.txt
python scripts/check-cv-entries-are-ascii.py
```
"""

import json
import logging
import os
from collections.abc import Iterator
from pathlib import Path
from typing import Any

from ascii_latex import to_ascii_latex

# Values which are allowed to contain non-ASCII characters,
# keyed by the path to the entry (relative to the root of the repository).
# These are names in their native script, which can't be written in ASCII,
# even with LaTeX.
EXEMPTIONS: dict[str, tuple[str, ...]] = {
    "institution/as-rcec.json": ("環境變遷研究中心",),
    "institution/bnu.json": ("بیکن ہاؤس نیشنل یونیورسٹی",),
    "institution/cas.json": ("中国科学院",),
    "institution/cma.json": ("中国气象局",),
    "institution/fdu.json": ("复旦大学", "復旦大學"),
    "institution/hyu.json": ("한양대학교",),
    "institution/iitm.json": ("भारतीय उष्णप्रदेशीय हवामानशास्त्र संस्था",),
    "institution/ium.json": ("中国气象局",),
    "institution/mri.json": (
        "きしょうけんきゅうしょ",
        "キショウケンキュウショ",
        "気象庁気象研究所",
        "気象研究所",
    ),
    "institution/nims-kma.json": ("국립기상과학원",),
    "institution/sysu.json": ("中山大学",),
    "institution/unist.json": ("울산과학기술대학교",),
}


def get_strings(value: Any) -> Iterator[str]:
    """Get all the strings in a loaded JSON value (keys included)"""
    if isinstance(value, str):
        yield value

    elif isinstance(value, list):
        for v in value:
            yield from get_strings(v)

    elif isinstance(value, dict):
        for k, v in value.items():
            yield k
            yield from get_strings(v)


def as_json(value: str) -> str:
    """Show a value as it should be written in the JSON file"""
    return json.dumps(value, ensure_ascii=False)


def main():
    # We report characters with no LaTeX equivalent ourselves
    logging.getLogger("pylatexenc").setLevel(logging.ERROR)

    REPO_ROOT = Path(__file__).parents[1]

    failing = []
    used_exemptions = set()
    for cvs_folder in (f.path for f in os.scandir(REPO_ROOT) if f.is_dir()):
        if cvs_folder.endswith("scripts") or cvs_folder.endswith(".venv"):
            continue

        for cv_file in sorted(Path(cvs_folder).glob("*.json")):
            cv_file_rel = cv_file.relative_to(REPO_ROOT).as_posix()
            with open(cv_file, encoding="utf-8") as fh:
                content = json.load(fh)

            for value in get_strings(content):
                expected = to_ascii_latex(value)
                if value != expected:
                    failing.append(
                        f"{cv_file_rel}: {as_json(value)} should be {as_json(expected)}"
                    )
                    continue

                if value.isascii():
                    continue

                if value in EXEMPTIONS.get(cv_file_rel, ()):
                    used_exemptions.add((cv_file_rel, value))
                    continue

                non_ascii = ", ".join(
                    f"{c!r} (U+{ord(c):04X})"
                    for c in sorted({c for c in value if not c.isascii()})
                )
                failing.append(
                    f"{cv_file_rel}: {as_json(value)} contains {non_ascii}, "
                    "which have no LaTeX equivalent. "
                    "If this is e.g. a name in its native script, "
                    "add it to `EXEMPTIONS` in this script."
                )

    for cv_file_rel, values in EXEMPTIONS.items():
        for value in values:
            if (cv_file_rel, value) not in used_exemptions:
                failing.append(
                    f"Unused exemption, please remove it: {cv_file_rel}: {value!r}"
                )

    if failing:
        raise AssertionError("\n".join(failing))


if __name__ == "__main__":
    main()
