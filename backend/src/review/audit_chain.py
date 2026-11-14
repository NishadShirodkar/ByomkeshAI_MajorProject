"""Hash chain over review events so edits to the recorded history are detectable."""

from __future__ import annotations

import hashlib
import json
from collections.abc import Sequence

from .review_models import ReviewEvent

GENESIS_HASH = "GENESIS"


def compute_event_hash(event: ReviewEvent) -> str:
    payload = json.dumps(
        event.model_dump(mode="json", exclude={"event_hash"}),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def verify_chain(events: Sequence[ReviewEvent]) -> tuple[bool, str]:
    """Return (ok, message). Events recorded before chaining existed are reported, not trusted."""

    if not events:
        return False, "No audit events recorded."
    previous = GENESIS_HASH
    for index, event in enumerate(events, 1):
        if not event.event_hash:
            return False, f"Event {index} ({event.event_type.value}) has no hash; history cannot be verified."
        if event.prev_hash != previous:
            return False, f"Event {index} ({event.event_type.value}) does not link to the previous event; history was altered."
        if compute_event_hash(event) != event.event_hash:
            return False, f"Event {index} ({event.event_type.value}) content does not match its hash; history was altered."
        previous = event.event_hash
    return True, f"{len(events)} events form an unbroken hash chain."


def chain_head(events: Sequence[ReviewEvent]) -> str:
    return events[-1].event_hash if events and events[-1].event_hash else GENESIS_HASH
