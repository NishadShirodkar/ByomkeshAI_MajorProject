"""Unicode-aware text normalization shared by parsing, entity resolution and tracing."""

from __future__ import annotations

import unicodedata


def _keep(char: str) -> bool:
    # Letters, numbers and combining marks (Devanagari matras are category M*).
    return unicodedata.category(char)[0] in "LNM"


def normalize_for_match(value: str) -> str:
    """Casefold and drop everything except letters, digits and combining marks."""

    folded = unicodedata.normalize("NFKC", value).casefold()
    return "".join(char for char in folded if _keep(char))


def name_tokens(value: str) -> list[str]:
    """Split a name into normalized tokens without discarding non-Latin scripts."""

    folded = unicodedata.normalize("NFKC", value).casefold()
    spaced = "".join(char if _keep(char) else " " for char in folded)
    return spaced.split()


def devanagari_ratio(value: str) -> float:
    letters = [char for char in value if char.isalpha()]
    if not letters:
        return 0.0
    return sum(1 for char in letters if "ऀ" <= char <= "ॿ") / len(letters)
