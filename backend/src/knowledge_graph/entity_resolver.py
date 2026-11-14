"""Conservative deterministic identity keys for graph entity de-duplication."""

from __future__ import annotations

from ..text_normalization import name_tokens, normalize_for_match
from .graph_models import GraphNodeType


class EntityResolver:
    """Normalizes explicitly parsed entity labels; it never invents an identity."""

    @staticmethod
    def identity_key(node_type: GraphNodeType, label: str) -> str:
        normalized = normalize_for_match(label)
        if node_type == GraphNodeType.VEHICLE:
            return f"vehicle:{normalized}"
        if node_type == GraphNodeType.LOCATION:
            return f"location:{normalized}"
        if node_type == GraphNodeType.PERSON:
            return f"person:{normalized}"
        return f"{node_type.value}:{normalized}"

    @staticmethod
    def person_matches(left: str, right: str) -> bool:
        """Match name abbreviations only when their explicit tokens are compatible."""

        left_tokens = name_tokens(left)
        right_tokens = name_tokens(right)
        if not left_tokens or not right_tokens or left_tokens[0] != right_tokens[0]:
            return False
        if len(left_tokens) == 1 or len(right_tokens) == 1:
            return True
        return all(
            a == b or len(a) == 1 and b.startswith(a) or len(b) == 1 and a.startswith(b)
            for a, b in zip(left_tokens, right_tokens)
        ) and len(left_tokens) == len(right_tokens)

