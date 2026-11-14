"""Verifies a finalized charge sheet (or a copy of it) against its seal and audit trail."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ...intake.storage_layout import CaseStorageLayout
from ...review.review_models import ChargeSheetReview, ReviewStatus
from ...signing.seal import seal_path_for, verify_seal
from ..config import api_config
from ..exceptions import ArtifactNotFoundError, CaseNotFoundError
from .case_service import parse_safe_case_id


class VerificationService:
    def __init__(self, storage_root: Path | None = None) -> None:
        self.storage_root = (storage_root or api_config.storage_root).resolve()

    def verify(self, case_id: str, pdf_bytes: bytes | None = None) -> dict[str, Any]:
        case_uuid, client_id = parse_safe_case_id(case_id)
        layout = CaseStorageLayout(self.storage_root, case_uuid)
        if not layout.case_directory.is_dir():
            raise CaseNotFoundError(case_id)

        state_file = layout.processed_directory / "chargesheet" / "review_state.json"
        try:
            review = ChargeSheetReview.model_validate_json(state_file.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            raise ArtifactNotFoundError("No finalized charge sheet exists for this case.") from None
        if review.status != ReviewStatus.FINALIZED:
            raise ArtifactNotFoundError("This charge sheet has not been finalized, so there is nothing to verify yet.")

        final_dir = layout.processed_directory / "chargesheet" / "final"
        finals = sorted(final_dir.glob("ChargeSheet_v*_final.pdf"))
        if not finals:
            raise ArtifactNotFoundError("The finalized PDF is missing from storage.")
        pdf_path = finals[-1]
        seal_file = seal_path_for(pdf_path)
        try:
            seal_document = json.loads(seal_file.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            raise ArtifactNotFoundError("This charge sheet was finalized without a digital seal, so it cannot be verified.") from None

        checking_upload = pdf_bytes is not None
        result = verify_seal(
            self.storage_root,
            pdf_bytes if checking_upload else pdf_path.read_bytes(),
            seal_document,
            events=review.events,
            current_content_hash=review.approved_content_hash or review.data_content_hash,
        ).as_dict()
        return {
            "case_id": client_id,
            "version": review.approved_version or review.data_version,
            "finalized_at": review.finalized_at.isoformat() if review.finalized_at else None,
            "approved_by": review.reviewer_name or review.reviewer_id,
            "source": "uploaded copy" if checking_upload else "stored final PDF",
            **result,
        }
