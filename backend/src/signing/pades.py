"""Embedded PAdES-style PDF signature (pyHanko) and its validation."""

from __future__ import annotations

import io
from pathlib import Path

from .identity import SigningIdentity

FIELD_NAME = "OfficerApprovalSignature"
FALLBACK_BOX = (330.0, 52.0, 580.0, 112.0)


def embed_signature(
    pdf_path: Path,
    identity: SigningIdentity,
    *,
    page_number: int | None,
    box: tuple[float, float, float, float] | None,
    reason: str,
    location: str,
) -> None:
    """Sign ``pdf_path`` in place with a visible signature stamp at ``box`` on ``page_number`` (1-based)."""

    from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
    from pyhanko.sign import fields, signers
    from pyhanko.sign.signers.pdf_signer import PdfSignatureMetadata, PdfSigner
    from pyhanko.stamp import TextStampStyle

    signer = signers.SimpleSigner.load(str(identity.key_path), str(identity.cert_path), key_passphrase=None)
    metadata = PdfSignatureMetadata(
        field_name=FIELD_NAME,
        reason=reason,
        location=location,
        name="BYOMKESH AI Demo Signing Authority",
        md_algorithm="sha256",
    )
    spec = fields.SigFieldSpec(
        FIELD_NAME,
        on_page=(page_number - 1) if page_number else -1,
        box=box or FALLBACK_BOX,
    )
    stamp = TextStampStyle(
        stamp_text="Digitally signed by: %(signer)s\nDate: %(ts)s\nReason: " + reason,
        border_width=1,
    )
    with pdf_path.open("rb") as handle:
        writer = IncrementalPdfFileWriter(handle)
        signed = PdfSigner(metadata, signer=signer, stamp_style=stamp, new_field_spec=spec).sign_pdf(writer)
        payload = signed.getvalue()
    pdf_path.write_bytes(payload)


def validate_embedded(pdf_bytes: bytes, identity: SigningIdentity) -> dict:
    """Validate the embedded signature against this system's certificate as the only trust root."""

    from pyhanko.keys import load_cert_from_pemder
    from pyhanko.pdf_utils.reader import PdfFileReader
    from pyhanko.sign.validation import validate_pdf_signature
    from pyhanko_certvalidator import ValidationContext

    result = {"present": False, "intact": False, "trusted": False, "covers_entire_file": False, "signer": None, "detail": ""}
    try:
        reader = PdfFileReader(io.BytesIO(pdf_bytes))
        signatures = reader.embedded_signatures
    except Exception:
        result["detail"] = "The file is not a readable PDF."
        return result
    if not signatures:
        result["detail"] = "The PDF carries no embedded digital signature."
        return result

    result["present"] = True
    try:
        context = ValidationContext(trust_roots=[load_cert_from_pemder(str(identity.cert_path))])
        status = validate_pdf_signature(signatures[0], signer_validation_context=context)
    except Exception as error:
        result["detail"] = f"The embedded signature could not be validated: {type(error).__name__}."
        return result

    coverage = getattr(status.coverage, "name", str(status.coverage))
    result.update(
        intact=bool(status.intact and status.valid),
        trusted=bool(status.trusted),
        covers_entire_file=coverage == "ENTIRE_FILE",
        signer=signatures[0].signer_cert.subject.human_friendly if signatures[0].signer_cert else None,
    )
    if not result["intact"]:
        result["detail"] = "The PDF content was changed after it was signed."
    elif not result["covers_entire_file"]:
        result["detail"] = "Extra content was appended after the signature was applied."
    elif not result["trusted"]:
        result["detail"] = "The signature is valid but not issued by this system's signing authority."
    else:
        result["detail"] = "Valid embedded PDF signature covering the entire file."
    return result
