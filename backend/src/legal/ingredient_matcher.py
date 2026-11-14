"""Negation-aware matching of a statutory ingredient against an evidence description."""

from __future__ import annotations

import math
import re
from dataclasses import dataclass

STOPWORDS = frozenset(
    "that this with from have been were which their there than then them into onto upon such some "
    "other under over also only when what where whom whose shall will would could should does done being "
    "having thereby therefore thereof whether without between within against about after before while "
    "person persons any all and for the not are was its his her him who may can has had more most".split()
)
NEGATIONS = frozenset(
    "no not nil never without none absent negative denied cannot neither nor nobody nothing unable "
    "didn't wasn't weren't isn't aren't doesn't don't hadn't hasn't haven't won't wouldn't couldn't".split()
)
_WORD = re.compile(r"[\w'-]+", re.UNICODE)


@dataclass(frozen=True)
class ElementMatch:
    supports: bool = False
    negated: bool = False
    score: float = 0.0


def _stem(token: str) -> str:
    return re.sub(r"(ing|ed|es|s)$", "", token) if len(token) > 5 else token


def term_presence(text: str, term: str) -> tuple[bool, bool]:
    """Return (affirmed, negated) for ``term`` at a word start in ``text`` (both casefolded)."""

    affirmed = negated = False
    for found in re.finditer(r"(?<!\w)" + re.escape(term), text):
        before = text[max(0, found.start() - 30) : found.start()]
        words = _WORD.findall(before)[-3:]
        if any(word in NEGATIONS for word in words) or re.search(r"\bnon[- ]$", before):
            negated = True
        else:
            affirmed = True
    return affirmed, negated


def mentions(text: str, terms: tuple[str, ...] | list[str]) -> bool:
    """True when any term is present and not negated ("not fatal" does not mention "fatal")."""

    folded = text.casefold()
    return any(term_presence(folded, term)[0] for term in terms)


def match_element(element: str, cues: tuple[str, ...], description: str) -> ElementMatch:
    text = description.casefold()
    phrase = element.casefold().strip()
    affirmed = negated = False
    score = 0.0

    if phrase and phrase in text:
        phrase_affirmed, phrase_negated = term_presence(text, phrase)
        affirmed, negated, score = phrase_affirmed, phrase_negated, 1.0 if phrase_affirmed else 0.0

    for cue in cues:
        cue_affirmed, cue_negated = term_presence(text, cue.casefold())
        if cue_affirmed:
            affirmed, score = True, max(score, 0.8)
        elif cue_negated:
            negated = True

    tokens = [
        t for t in dict.fromkeys(_WORD.findall(phrase)) if len(t) > 3 and t not in STOPWORDS
    ]
    if tokens:
        hit_affirmed = hit_negated = 0
        for token in tokens:
            token_affirmed, token_negated = term_presence(text, _stem(token))
            hit_affirmed += token_affirmed
            hit_negated += token_negated and not token_affirmed
        needed = 1 if len(tokens) == 1 else max(2, math.ceil(0.6 * len(tokens)))
        if hit_affirmed >= needed:
            affirmed, score = True, max(score, round(0.5 + 0.4 * hit_affirmed / len(tokens), 2))
        elif hit_negated >= needed:
            negated = True

    return ElementMatch(supports=affirmed, negated=negated and not affirmed, score=score if affirmed else 0.0)
