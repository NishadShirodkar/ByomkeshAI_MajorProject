"""FastAPI dependency providers for services and configuration."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

from fastapi import Depends

from .config import api_config
from .services.artifact_service import ArtifactService
from .services.case_review_service import CaseReviewService
from .services.case_service import CaseService
from .services.job_service import JobService
from .services.source_service import SourceService
from .services.verification_service import VerificationService

# Default service instances bound to api_config.storage_root
_default_case_service: CaseService | None = None
_default_job_service: JobService | None = None
_default_artifact_service: ArtifactService | None = None
_default_review_service: CaseReviewService | None = None
_default_source_service: SourceService | None = None
_default_verification_service: VerificationService | None = None


def get_storage_root() -> Path:
    return api_config.storage_root


def get_case_service(storage_root: Annotated[Path, Depends(get_storage_root)]) -> CaseService:
    global _default_case_service
    if _default_case_service is None or _default_case_service.storage_root != storage_root:
        _default_case_service = CaseService(storage_root)
    return _default_case_service


def get_job_service(storage_root: Annotated[Path, Depends(get_storage_root)]) -> JobService:
    global _default_job_service
    if _default_job_service is None or _default_job_service.storage_root != storage_root:
        _default_job_service = JobService(storage_root)
    return _default_job_service


def get_artifact_service(storage_root: Annotated[Path, Depends(get_storage_root)]) -> ArtifactService:
    global _default_artifact_service
    if _default_artifact_service is None or _default_artifact_service.storage_root != storage_root:
        _default_artifact_service = ArtifactService(storage_root)
    return _default_artifact_service


def get_source_service(storage_root: Annotated[Path, Depends(get_storage_root)]) -> SourceService:
    global _default_source_service
    if _default_source_service is None or _default_source_service.storage_root != storage_root.resolve():
        _default_source_service = SourceService(storage_root)
    return _default_source_service


def get_verification_service(storage_root: Annotated[Path, Depends(get_storage_root)]) -> VerificationService:
    global _default_verification_service
    if _default_verification_service is None or _default_verification_service.storage_root != storage_root.resolve():
        _default_verification_service = VerificationService(storage_root)
    return _default_verification_service


def get_review_service(storage_root: Annotated[Path, Depends(get_storage_root)]) -> CaseReviewService:
    global _default_review_service
    if _default_review_service is None or _default_review_service.storage_root != storage_root:
        _default_review_service = CaseReviewService(storage_root)
    return _default_review_service
