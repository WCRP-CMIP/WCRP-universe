"""
Conversion of text to ASCII, with non-ASCII characters encoded as LaTeX

Text is converted in two steps (see `to_ascii_latex`):

1. Typographic characters (typically introduced by copy-pasting from word
   processors, e.g. curly quotes, dashes and special spaces) are replaced
   with their plain ASCII equivalents, as listed in `ASCII_REPLACEMENTS`.
   To change how such a character is handled, add or edit it there.
2. Every other non-ASCII character (e.g. accented letters in names,
   symbols like the degree sign) is encoded as its LaTeX equivalent
   using [pylatexenc](https://pypi.org/project/pylatexenc/).
   Characters which have no LaTeX equivalent
   (e.g. Chinese characters in names in their native script) are kept as is.
   They are flagged by `check-cv-entries-are-ascii.py`.

ASCII text is never altered by the LaTeX encoding,
i.e. characters like `%`, `&`, `_` and `$` are not escaped.

This is a copy of the conversion used to write entries
in the CMIP7-CVs repository
(`.github/form-processor/src/github_form_processor/text.py`).
If you change it here, change it there too.
"""

from __future__ import annotations

import unicodedata
from typing import Any

from pylatexenc.latexencode import UnicodeToLatexEncoder

ASCII_REPLACEMENTS: dict[str, str] = {
    # Quotation marks
    "\u2018": "'",  # left single quotation mark
    "\u2019": "'",  # right single quotation mark
    "\u201a": "'",  # single low-9 quotation mark
    "\u201b": "'",  # single high-reversed-9 quotation mark
    "\u2032": "'",  # prime
    "\u00b4": "'",  # acute accent
    "\u201c": '"',  # left double quotation mark
    "\u201d": '"',  # right double quotation mark
    "\u201e": '"',  # double low-9 quotation mark
    "\u201f": '"',  # double high-reversed-9 quotation mark
    "\u2033": '"',  # double prime
    "\u00ab": '"',  # left-pointing double angle quotation mark
    "\u00bb": '"',  # right-pointing double angle quotation mark
    # Dashes and hyphens
    "\u2010": "-",  # hyphen
    "\u2011": "-",  # non-breaking hyphen
    "\u2012": "-",  # figure dash
    "\u2013": "-",  # en dash
    "\u2014": "-",  # em dash
    "\u2015": "-",  # horizontal bar
    "\u2212": "-",  # minus sign
    "\u00ad": "",  # soft hyphen
    # Spaces
    "\u00a0": " ",  # no-break space
    "\u2009": " ",  # thin space
    "\u202f": " ",  # narrow no-break space
    "\u200b": "",  # zero width space
    "\ufeff": "",  # zero width no-break space (byte order mark)
    # Other punctuation
    "\u2022": "-",  # bullet
    "\u2026": "...",  # horizontal ellipsis
}
"""
Typographic characters and the plain ASCII they are replaced with

Any non-ASCII character not listed here is encoded as LaTeX instead.
"""

_ASCII_TRANSLATION = str.maketrans(ASCII_REPLACEMENTS)

_LATEX_ENCODER = UnicodeToLatexEncoder(
    # Leave ASCII (e.g. `%`, `&`, `_`, `$`, `\`) exactly as it is
    non_ascii_only=True,
    # Only add braces where they are needed to keep the LaTeX valid,
    # e.g. sharp s becomes `{\ss}` but an e with an acute accent becomes `\'e`
    replacement_latex_protection="braces",
    # Characters without a LaTeX equivalent are kept
    # (and flagged by the CI check of the CVs)
    unknown_char_policy="keep",
    unknown_char_warning=True,
)


def to_plain_text(value: str) -> str:
    """Convert typographic punctuation in a string to plain ASCII"""
    return unicodedata.normalize("NFC", value.translate(_ASCII_TRANSLATION))


def to_ascii_latex(value: str) -> str:
    """Convert a string to ASCII, encoding non-ASCII characters as LaTeX"""
    return _LATEX_ENCODER.unicode_to_latex(to_plain_text(value))


def to_ascii_latex_recursive(value: Any) -> Any:
    """Apply `to_ascii_latex` to every string (keys included) in a JSON-like value"""
    if isinstance(value, str):
        return to_ascii_latex(value)

    if isinstance(value, dict):
        return {
            to_ascii_latex_recursive(k): to_ascii_latex_recursive(v)
            for k, v in value.items()
        }

    if isinstance(value, (list, tuple)):
        return [to_ascii_latex_recursive(v) for v in value]

    return value
