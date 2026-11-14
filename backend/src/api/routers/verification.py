"""Public authenticity checks for finalized charge sheets."""

from __future__ import annotations

from typing import Annotated, Any

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from fastapi.concurrency import run_in_threadpool
from fastapi.responses import HTMLResponse

from ..dependencies import get_verification_service
from ..services.verification_service import VerificationService

router = APIRouter(tags=["Verification"])

MAX_UPLOAD_BYTES = 25 * 1024 * 1024

VERIFY_PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Verify charge sheet</title>
<style>
 :root{--bg:#f8fafc;--fg:#0f172a;--card:#fff;--line:#e2e8f0;--ok:#047857;--bad:#b91c1c;--muted:#64748b}
 @media (prefers-color-scheme:dark){:root{--bg:#0b1220;--fg:#e2e8f0;--card:#111c2e;--line:#22314a;--ok:#34d399;--bad:#f87171;--muted:#94a3b8}}
 body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,sans-serif}
 main{max-width:640px;margin:0 auto;padding:24px 16px}
 .card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:18px;margin-top:14px}
 h1{font-size:20px;margin:0 0 4px} .muted{color:var(--muted);font-size:13px}
 .verdict{font-size:18px;font-weight:700;margin-bottom:8px} .ok{color:var(--ok)} .bad{color:var(--bad)}
 ul{list-style:none;padding:0;margin:8px 0 0} li{padding:7px 0;border-top:1px solid var(--line)}
 li b{display:inline-block;min-width:1.4em} button{padding:8px 14px;border-radius:6px;border:1px solid var(--line);background:var(--card);color:var(--fg);cursor:pointer}
 code{font-size:12px;word-break:break-all}
</style></head><body><main>
<h1>Charge sheet authenticity check</h1>
<div class="muted" id="case"></div>
<div class="card" id="result">Checking the stored document&hellip;</div>
<div class="card">
 <strong>Check a copy you were given</strong>
 <p class="muted">Upload the PDF you received. If even one byte differs from the signed original, verification fails.</p>
 <input type="file" id="file" accept="application/pdf"> <button id="go">Verify this file</button>
</div></main>
<script>
const caseId = decodeURIComponent(location.pathname.split('/').filter(Boolean).pop());
document.getElementById('case').textContent = 'Case: ' + caseId;
const base = '/api/v1/cases/' + encodeURIComponent(caseId) + '/verification';
function show(d, label){
  const box = document.getElementById('result'); box.textContent = '';
  const v = document.createElement('div'); v.className = 'verdict ' + (d.verified ? 'ok' : 'bad');
  v.textContent = d.verified ? 'VERIFIED: authentic and unaltered' : 'NOT VERIFIED: do not rely on this document';
  box.appendChild(v);
  const meta = document.createElement('div'); meta.className = 'muted';
  meta.textContent = label + ' | Version ' + d.version + (d.approved_by ? ' | Approved by ' + d.approved_by : '') + (d.signed_at ? ' | Signed ' + d.signed_at : '');
  box.appendChild(meta);
  const ul = document.createElement('ul');
  d.checks.forEach(c => { const li = document.createElement('li');
    const m = document.createElement('b'); m.textContent = c.passed ? '\\u2713' : '\\u2717'; m.className = c.passed ? 'ok' : 'bad';
    li.appendChild(m); li.appendChild(document.createTextNode(' ' + c.name + ': ' + c.detail)); ul.appendChild(li); });
  box.appendChild(ul);
  if (d.pdf_sha256) { const h = document.createElement('div'); h.className = 'muted'; h.append('SHA-256 of checked file: ');
    const c = document.createElement('code'); c.textContent = d.pdf_sha256; h.appendChild(c); box.appendChild(h); }
}
function fail(msg){ const b = document.getElementById('result'); b.textContent = msg; }
fetch(base).then(r => r.json().then(j => r.ok ? show(j, 'Stored final PDF') : fail(j.detail || j.message || 'Not available'))).catch(() => fail('Could not reach the server.'));
document.getElementById('go').onclick = () => {
  const f = document.getElementById('file').files[0]; if (!f) return;
  const fd = new FormData(); fd.append('file', f);
  fetch(base + '/upload', {method: 'POST', body: fd}).then(r => r.json().then(j => r.ok ? show(j, 'Uploaded: ' + f.name) : fail(j.detail || j.message || 'Verification failed'))).catch(() => fail('Could not reach the server.'));
};
</script></body></html>"""


@router.get("/api/v1/cases/{case_id}/verification", summary="Verify the stored final charge sheet")
def verify_stored(
    case_id: str,
    service: Annotated[VerificationService, Depends(get_verification_service)],
) -> dict[str, Any]:
    return service.verify(case_id)


@router.post("/api/v1/cases/{case_id}/verification/upload", summary="Verify an uploaded copy against the signed original")
async def verify_upload(
    case_id: str,
    service: Annotated[VerificationService, Depends(get_verification_service)],
    file: Annotated[UploadFile, File()],
) -> dict[str, Any]:
    content = await file.read(MAX_UPLOAD_BYTES + 1)
    if len(content) > MAX_UPLOAD_BYTES:
        raise HTTPException(status_code=413, detail="File is too large to verify.")
    return await run_in_threadpool(service.verify, case_id, content)


@router.get("/verify/{case_id}", response_class=HTMLResponse, include_in_schema=False)
def verification_page(case_id: str) -> HTMLResponse:
    return HTMLResponse(VERIFY_PAGE)
