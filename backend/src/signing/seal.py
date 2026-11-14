"""Signs a finalized chargesheet PDF's hash together with its audit-log head, and verifies it later."""

from __future__ import annotations

import base64
import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from uuid import UUID

from cryptography import x509
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

from ..review.audit_chain import chain_head, verify_chain
from ..review.review_models import ReviewEvent
from .identity import SigningIdentity, load_or_create_identity
from .pades import validate_embedded

SEAL_VERSION = 1


def seal_path_for(pdf_path: Path) -> Path:
    return pdf_path.with_name(pdf_path.stem + ".seal.json")


def _canonical(seal: dict) -> bytes:
    return json.dumps(seal, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def seal_pdf(
    storage_root: Path,
    pdf_path: Path,
    *,
    case_id: UUID,
    version: int,
    content_hash: str,
    audit_head: str,
    identity: SigningIdentity | None = None,
) -> Path:
    identity = identity or load_or_create_identity(storage_root)
    seal = {
        "seal_version": SEAL_VERSION,
        "case_id": str(case_id),
        "version": version,
        "pdf_sha256": hashlib.sha256(pdf_path.read_bytes()).hexdigest(),
        "chargesheet_content_hash": content_hash,
        "audit_head_hash": audit_head,
        "signed_at": datetime.now(timezone.utc).isoformat(),
        "algorithm": "RSA-SHA256",
        "signer": {"subject": identity.subject, "certificate_sha256": identity.fingerprint},
    }
    document = {
        "seal": seal,
        "signature": base64.b64encode(identity.private_key.sign(_canonical(seal), padding.PKCS1v15(), hashes.SHA256())).decode("ascii"),
        "certificate_pem": identity.certificate_pem,
    }
    path = seal_path_for(pdf_path)
    path.write_text(json.dumps(document, indent=2), encoding="utf-8")
    return path


@dataclass
class SealVerification:
    verified: bool
    checks: list[dict]
    signer: str | None = None
    signed_at: str | None = None
    pdf_sha256: str | None = None
    embedded_signature: dict | None = None

    def as_dict(self) -> dict:
        return {
            "verified": self.verified,
            "checks": self.checks,
            "signer": self.signer,
            "signed_at": self.signed_at,
            "pdf_sha256": self.pdf_sha256,
            "embedded_signature": self.embedded_signature,
        }


def _check(checks: list[dict], name: str, ok: bool, detail: str) -> None:
    checks.append({"name": name, "passed": bool(ok), "detail": detail})


def verify_seal(
    storage_root: Path,
    pdf_bytes: bytes,
    seal_document: dict,
    *,
    events: tuple[ReviewEvent, ...],
    current_content_hash: str | None,
) -> SealVerification:
    checks: list[dict] = []
    seal = seal_document.get("seal", {})
    actual_hash = hashlib.sha256(pdf_bytes).hexdigest()

    _check(
        checks,
        "Document integrity",
        actual_hash == seal.get("pdf_sha256"),
        "The PDF is byte-for-byte identical to the one that was signed."
        if actual_hash == seal.get("pdf_sha256")
        else "The PDF has been modified since it was signed.",
    )

    signature_ok = False
    cert_fingerprint = None
    try:
        certificate = x509.load_pem_x509_certificate(seal_document["certificate_pem"].encode("ascii"))
        cert_fingerprint = certificate.fingerprint(hashes.SHA256()).hex()
        certificate.public_key().verify(base64.b64decode(seal_document["signature"]), _canonical(seal), padding.PKCS1v15(), hashes.SHA256())
        signature_ok = True
    except (KeyError, ValueError, InvalidSignature, TypeError):
        signature_ok = False
    _check(
        checks,
        "Signature",
        signature_ok,
        "The seal carries a valid digital signature." if signature_ok else "The seal signature is invalid or missing.",
    )

    trusted = load_or_create_identity(storage_root)
    is_trusted = signature_ok and cert_fingerprint == trusted.fingerprint == seal.get("signer", {}).get("certificate_sha256")
    _check(
        checks,
        "Trusted signer",
        is_trusted,
        "Signed by this system's signing authority." if is_trusted else "The signer is not this system's signing authority.",
    )

    embedded = validate_embedded(pdf_bytes, trusted)
    embedded_ok = embedded["present"] and embedded["intact"] and embedded["covers_entire_file"] and embedded["trusted"]
    _check(checks, "Embedded PDF signature", embedded_ok, embedded["detail"])

    chain_ok, chain_message = verify_chain(events)
    _check(checks, "Audit trail", chain_ok, chain_message)
    head_ok = bool(events) and chain_head(events) == seal.get("audit_head_hash")
    _check(
        checks,
        "Audit trail matches seal",
        head_ok,
        "The audit history is exactly what existed when the document was signed."
        if head_ok
        else "The audit history differs from what was signed.",
    )

    if current_content_hash is not None:
        content_ok = current_content_hash == seal.get("chargesheet_content_hash")
        _check(
            checks,
            "Content binding",
            content_ok,
            "The signed chargesheet content matches the approved record."
            if content_ok
            else "The approved chargesheet record differs from the signed content.",
        )

    return SealVerification(
        verified=all(item["passed"] for item in checks),
        checks=checks,
        signer=seal.get("signer", {}).get("subject"),
        signed_at=seal.get("signed_at"),
        pdf_sha256=actual_hash,
        embedded_signature=embedded,
    )
