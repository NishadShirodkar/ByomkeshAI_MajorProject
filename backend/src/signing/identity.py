"""Server signing identity: an RSA key with a self-signed certificate.

Demo-grade trust: this is NOT a CCA-licensed Digital Signature Certificate. For
production the key would live in an HSM or come from an eSign provider.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID

SIGNER_COMMON_NAME = "BYOMKESH AI Demo Signing Authority"
SIGNER_ORGANIZATION = "Self-signed demo certificate (not a licensed DSC)"


@dataclass(frozen=True)
class SigningIdentity:
    private_key: rsa.RSAPrivateKey
    certificate: x509.Certificate
    key_path: Path
    cert_path: Path

    @property
    def fingerprint(self) -> str:
        return self.certificate.fingerprint(hashes.SHA256()).hex()

    @property
    def subject(self) -> str:
        return self.certificate.subject.rfc4514_string()

    @property
    def certificate_pem(self) -> str:
        return self.certificate.public_bytes(serialization.Encoding.PEM).decode("ascii")


def public_base_url() -> str:
    return os.getenv("PUBLIC_BASE_URL", "http://127.0.0.1:8000").rstrip("/")


def load_or_create_identity(storage_root: Path) -> SigningIdentity:
    directory = storage_root / "_signing"
    key_path, cert_path = directory / "signer_rsa_key.pem", directory / "signer_rsa_cert.pem"
    if key_path.is_file() and cert_path.is_file():
        key = serialization.load_pem_private_key(key_path.read_bytes(), password=None)
        certificate = x509.load_pem_x509_certificate(cert_path.read_bytes())
        if isinstance(key, rsa.RSAPrivateKey):
            return SigningIdentity(key, certificate, key_path, cert_path)

    directory.mkdir(parents=True, exist_ok=True)
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    name = x509.Name(
        [
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, SIGNER_ORGANIZATION),
            x509.NameAttribute(NameOID.COMMON_NAME, SIGNER_COMMON_NAME),
        ]
    )
    now = datetime.now(timezone.utc)
    certificate = (
        x509.CertificateBuilder()
        .subject_name(name)
        .issuer_name(name)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - timedelta(minutes=5))
        .not_valid_after(now + timedelta(days=3650))
        .add_extension(x509.BasicConstraints(ca=True, path_length=0), critical=True)
        .add_extension(
            x509.KeyUsage(
                digital_signature=True,
                content_commitment=True,
                key_encipherment=False,
                data_encipherment=False,
                key_agreement=False,
                key_cert_sign=True,
                crl_sign=False,
                encipher_only=False,
                decipher_only=False,
            ),
            critical=True,
        )
        .sign(key, hashes.SHA256())
    )
    key_path.write_bytes(
        key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption())
    )
    cert_path.write_bytes(certificate.public_bytes(serialization.Encoding.PEM))
    return SigningIdentity(key, certificate, key_path, cert_path)
