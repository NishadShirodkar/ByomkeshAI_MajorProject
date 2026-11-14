"""Cross-document contradiction detection."""

from .detector import ContradictionDetector
from .models import Contradiction, ContradictionKind, ContradictionSeverity, ContradictionSide

__all__ = ["Contradiction", "ContradictionDetector", "ContradictionKind", "ContradictionSeverity", "ContradictionSide"]
