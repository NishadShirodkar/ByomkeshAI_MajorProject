"""Click-to-source tracing: page images and text locations for source documents."""

from __future__ import annotations

from typing import Annotated, Any

from fastapi import APIRouter, Depends, Query, Response

from ..dependencies import get_source_service
from ..services.source_service import SourceService

router = APIRouter(prefix="/api/v1/cases/{case_id}/sources", tags=["Sources"])


@router.get("/{document_id}", summary="Source document info")
def get_source_info(
    case_id: str,
    document_id: str,
    service: Annotated[SourceService, Depends(get_source_service)],
) -> dict[str, Any]:
    return service.info(case_id, document_id)


@router.get("/{document_id}/pages/{page_number}/image", summary="Rendered page image (PNG)")
def get_page_image(
    case_id: str,
    document_id: str,
    page_number: int,
    service: Annotated[SourceService, Depends(get_source_service)],
) -> Response:
    return Response(
        content=service.render_page(case_id, document_id, page_number),
        media_type="image/png",
        headers={"Cache-Control": "private, max-age=300"},
    )


@router.get("/{document_id}/locate", summary="Find where a text appears in the source")
def locate_text(
    case_id: str,
    document_id: str,
    service: Annotated[SourceService, Depends(get_source_service)],
    text: Annotated[str, Query(min_length=1, max_length=2000)],
    page: Annotated[int | None, Query(ge=1)] = None,
) -> dict[str, Any]:
    return {"matches": service.locate(case_id, document_id, text, page)}
