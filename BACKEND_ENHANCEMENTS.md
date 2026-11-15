# BYOMKESH AI: Backend Enhancements

This document describes every backend change made after the initial audit of the chargesheet pipeline: what was wrong, what we built, how it works, and what it improved. Frontend work is deliberately excluded, except where an API exists only to serve it.

Contents

1. [Why these changes were made](#1-why-these-changes-were-made)
2. [Summary at a glance](#2-summary-at-a-glance)
3. [Trust fixes in the existing pipeline](#3-trust-fixes-in-the-existing-pipeline)
4. [Feature 1: Click-to-source tracing](#4-feature-1-click-to-source-tracing)
5. [Feature 2: Section suggestion with court-readiness](#5-feature-2-section-suggestion-with-court-readiness)
6. [Feature 3: Cross-document contradiction detector](#6-feature-3-cross-document-contradiction-detector)
7. [Feature 4: Signed and verifiable final PDF](#7-feature-4-signed-and-verifiable-final-pdf)
8. [Demo data seeding](#8-demo-data-seeding)
9. [API additions](#9-api-additions)
10. [Dependencies](#10-dependencies)
11. [Testing](#11-testing)
12. [Known limitations and honest caveats](#12-known-limitations-and-honest-caveats)
13. [Where things live](#13-where-things-live)

---

## 1. Why these changes were made

The original system already had a sound architecture: typed Pydantic models, provenance on every fact, a version-pinned legal dataset, and a human review lifecycle. A code audit (reading only, nothing run) found that it worked well on clean English demo cases but had gaps that could let a wrong or degraded result reach a court-bound document:

| Audit finding | Risk |
|---|---|
| Parser silently switched to a regex "mock" on Gemini quota errors | Demo-quality output looked identical to a real parse |
| PDF text came from a regex over `Tj` operators, decoded as latin-1 | Hindi text became garbage, then was reported as English at 0.99 confidence |
| Name normalisation kept only `a-z0-9` | Every Devanagari name collapsed to an empty key |
| Legal reasoning accepted one shared word as proof of an ingredient | False "supported" findings; "not fatal" matched "fatal" |
| Legal dataset had 7 sections out of about 358 | Almost no offence could ever be suggested |
| Failed core documents did not stop the case | A chargesheet could be produced without its FIR |
| Validation rules defaulted to off | A case with no FIR number validated as complete |
| No tamper-evidence on the approval history or the final PDF | A "final approved" document proved nothing |

The project is an MVP to be shown to an external evaluator. The scope was therefore: fix only the shortcomings that make the new features give wrong answers, and build four features that demonstrate real domain depth. Authentication, databases, job queues and PII redaction were explicitly out of scope.

## 2. Summary at a glance

| Area | Before | After |
|---|---|---|
| PDF text extraction | Regex, English only, fake confidence | PyMuPDF text layer with line bounding boxes; scanned pages fall back to OCR |
| Parser failure handling | Silent mock fallback | Retry with backoff, then fail loudly |
| Non-Latin names | Collapsed to empty key | Unicode-aware normalisation |
| Prompt safety | Document text pasted into prompt | Delimited as untrusted data |
| Core document failure | Pipeline continued | Pipeline stops |
| Legal dataset | 7 sections | 37 sections with punishment, cognizable/bailable/triable, keywords, cues |
| Ingredient matching | One shared word, no negation | Strict, negation-aware, scored, with evidence quote |
| Output per section | Status only | Status, ingredient evidence, court-readiness, evidence gaps |
| Cross-document checks | Exact-string timestamp equality | Seven contradiction types with both sides and excerpts |
| Final PDF | Plain PDF | Signed (PAdES), sealed, QR code, hash-chained audit log, public verification |
| Tests | 187 | 224 |

---

## 3. Trust fixes in the existing pipeline

### 3.1 Remove the silent mock fallback

- **File:** `backend/src/parsers/base_parser.py`
- **Problem:** on a 429/503/quota error, `GeminiParserClient` quietly returned the output of `MockParserClient`, a regex parser written for demo documents. Its output carried the same parser name and confidence as a real parse and could contain placeholders such as "Unknown Police Station".
- **Change:** transient errors now retry up to four attempts with exponential backoff (2, 4, 8 seconds). If all fail, a `ParserError` is raised. Invalid JSON raises a `ParserError` too.
- **Also:** the blanket `except (..., Exception)` that hid programming errors was narrowed to `ParserError`, `ValidationError`, `ValueError`.
- **Why:** a legal document must never contain machine guesses presented as extractions. Failing loudly is safer than degrading silently.

### 3.2 Real PDF text extraction with bounding boxes

- **Files:** `backend/src/extraction/pdf_extractor.py`, `gemini_ocr.py`, `mock_client.py`, `ocr_result.py`
- **Problem:** the old extractor matched `(text) Tj` with a regex and decoded as latin-1. It ignored `TJ` arrays, font encodings and CID fonts, so Devanagari became mojibake. `gemini_ocr.py` accepted that output at confidence 0.99 and language `"en"`, so real OCR never ran.
- **Change:**
  - `extract_digital_pdf_layout()` uses PyMuPDF and returns, per page, the text and each line with a box normalised to the page (0 to 1, top-left origin).
  - `digital_pdf_ocr_pages()` accepts the result only if **every** page has real text and the replacement-character ratio is low. A mixed or scanned PDF returns `None`, so the whole document goes to Gemini OCR.
  - Encrypted PDFs and PDFs over 500 pages are rejected.
  - Language is detected from the script ratio (Devanagari above 30% gives `hi`, pure ASCII gives `en`, otherwise unknown). Confidence for a real text layer is 0.98 instead of a hard-coded 0.99.
- **New model:** `OCRLine(text, bbox)` and `OCRPage.lines`. The fields default to empty, so previously saved OCR artifacts still load.
- **Gemini OCR prompt** now states that documents may be English, Hindi or Marathi, printed or handwritten, forbids translation or correction, and asks for per-line `box_2d` boxes (0 to 1000 scale), which are converted to the same normalised form.
- **Why:** correct text is the foundation of every later stage, and the boxes make click-to-source possible.

### 3.3 Unicode-aware normalisation

- **Files:** new `backend/src/text_normalization.py`; used by `knowledge_graph/entity_resolver.py` and `parsers/base_parser.py`
- **Problem:** `re.sub(r"[^a-z0-9]", "", ...)` removed every Devanagari character. All Hindi names produced the same empty key `person:` and were either merged together or rejected as "not present in the source".
- **Change:** `normalize_for_match` NFKC-normalises, case-folds, and keeps characters whose Unicode category starts with L (letter), N (number) or M (combining mark). Combining marks matter because Devanagari vowel signs are category M. `name_tokens` does the same but splits on other characters.
- **Why:** identity resolution and the "value must appear in the source text" guard both depend on it.

### 3.4 Prompt-injection hardening

- **File:** `parsers/base_parser.py`
- **Change:** OCR text is wrapped in `<document_text>...</document_text>`, a forged closing tag inside the document is stripped, and the instructions say the content is untrusted data and any commands inside it must be ignored. The prompt also tells the model to keep names in their original script.
- **Why:** case documents come from third parties and could contain text such as "ignore previous instructions".

### 3.5 Fail when a core document fails

- **Files:** `domain/documents.py`, `extraction/ocr_stage.py`, `parsers/parser_stage.py`
- **Problem:** the stages raised only if **all** documents failed. A case could lose its FIR and still produce a chargesheet. `validation_success` was hard-coded to `True`.
- **Change:** `OPTIONAL_DOCUMENT_TYPES` (CCTV, photographs, audio, other) may fail with a warning. Any other failed document raises and halts the case. `validation_success` now reflects the real outcome.
- **Why:** an incomplete chargesheet that looks complete is worse than no chargesheet.

### 3.6 Validation rules on by default

- **File:** `validation/validation_models.py`
- **Change:** `require_fir_number`, `require_police_station`, `require_occurrence_details` default to `True`.
- **Effect:** a case missing these now reports `review_required` with errors instead of scoring 1.0.

### 3.7 Tolerant loading of old saved outputs

- **File:** `api/services/case_review_service.py`
- **Change:** when loading saved chargesheet data, fields the current schema does not know are dropped before validation.
- **Why:** an older case on disk had four fields from a previous schema version (`fir_sections_not_supported` and others) and caused HTTP 500 on the review endpoint because the model forbids extra fields.

### 3.8 CORS for local development

- **File:** `api/app.py`
- **Change:** `allow_origin_regex` accepts any `localhost` or `127.0.0.1` port. Non-local origins are still rejected.
- **Why:** Vite moves to a new port when 5173 is taken; the browser then blocks API calls and the frontend reports a generic "cannot connect".

---

## 4. Feature 1: Click-to-source tracing

**Goal:** every value in the chargesheet can be traced back to the exact place in the original scanned or digital document, so an officer or evaluator can see where a fact came from in two seconds.

### Architecture

```
Source PDF/image
   |  OCR stage (PyMuPDF text layer, or Gemini OCR with box_2d)
   v
OCRResult { pages[ { text, lines[ {text, bbox} ] } ] }   saved as *_OCRResult.json
   |
   |   chargesheet field.source_references[ {document_id, location.page, excerpt} ]
   v
Locator  (text -> page + boxes)         Source service (HTTP)
   tracing/locator.py                     api/services/source_service.py
                                          api/routers/sources.py
```

### Logic: the locator (`backend/src/tracing/locator.py`)

1. Normalise the query with `normalize_for_match` (cut to 240 characters).
2. For each candidate page, take windows of 1, 2 and 3 consecutive lines.
3. Score each window:
   - If the normalised query is **contained** in the window: `90 + 10 * (len(query) / len(window))`, which prefers the tightest window.
   - Otherwise `rapidfuzz.fuzz.partial_ratio`, capped at 89.
4. Keep the best window per page when its score is at least 72, and return the top three across pages.
5. If a page hint is given, search that page first and only then the others.
6. If a page has no stored lines (older artifacts), fall back to splitting the page text into lines and return matches without boxes.

Fuzzy matching tolerates small OCR differences ("Rakesh Kumr" still finds "Rakesh Kumar"); unrelated text and very short queries return nothing, so the system does not invent a location.

### Source service and endpoints

`SourceService` finds the OCR JSON by the document's UUID prefix, finds the original in the case's `originals/` folder by UUID filename (so there is no user-controlled path), and renders pages with PyMuPDF at 130 DPI.

| Endpoint | Purpose |
|---|---|
| `GET /api/v1/cases/{case}/sources/{doc}` | Filename, type, page count, language, OCR provider, confidence, whether boxes exist |
| `GET /api/v1/cases/{case}/sources/{doc}/pages/{n}/image` | Rendered page as PNG |
| `GET /api/v1/cases/{case}/sources/{doc}/locate?text=&page=` | Matching pages, boxes and scores |

### Result

On a mock-mode pipeline run, 6 of 7 populated fields were located with boxes. The miss was a derived timeline fact that has no source sentence by design.

---

## 5. Feature 2: Section suggestion with court-readiness

**Goal:** go from "does this section's text appear" to "which offences does this case make out, on what evidence, and what would a defence lawyer attack?"

### 5.1 The legal dataset

- **File:** `backend/references/legal/bns_sections.json` (version `bns-2023-2024-07-01`, unchanged so configuration keeps working)
- **Size:** 7 original records plus 30 new ones, 37 in total. New coverage includes BNS offences against the person, property, women, and common special-act provisions (Motor Vehicles Act 184 and 185, IT Act 66C and 66D).
- **New fields on `LegalReference`:**

| Field | Meaning |
|---|---|
| `punishment`, `cognizable`, `bailable`, `triable_by`, `compoundable` | Facts a charge sheet needs |
| `legacy_ipc_equivalent` | Used for the IPC to BNS crosswalk |
| `keywords` | Words that make the section a candidate for a case |
| `element_cues` | Per-ingredient synonym stems (for example "hurt" matches "injur", "fracture") |
| `expected_documents` | Document types normally needed to prove the section |

- **Honesty marker:** all 30 new records have `verified: false` and no verification date. `verification_date` no longer defaults to `2024-07-01`, which previously stamped unverified records as verified. **A legal expert must verify these before real use.**
- **Crosswalk:** `LocalLegalReferenceProvider.bns_for_ipc("323")` returns BNS 115. It reads all numbers in a legacy string, so "IPC Sections 324, 326" resolves from either.

### 5.2 Ingredient matching

- **File:** `backend/src/legal/ingredient_matcher.py`
- **Old behaviour:** an ingredient counted as established if the full phrase was a substring, or if about half of its words longer than three characters appeared. One shared word such as "person" or "hurt" could satisfy it.
- **New logic, in order:**
  1. The whole phrase appears (score 1.0).
  2. Any configured cue appears (score 0.8).
  3. Distinctive tokens appear. One-word elements need that word; multi-word elements need at least `max(2, ceil(0.6 * n))` tokens, after removing stop-words (score `0.5 + 0.4 * hits / n`, at most 0.9).
- **Negation:** every match checks the three words before it for negation words (no, not, without, never, nil, and so on) or a `non-` prefix. "No hurt or injury was caused" is reported as **negated**, not as support. `mentions("injury was not fatal", ("fatal",))` is false.
- **Why:** it removes false "established" results and the "not fatal matches fatal" bug, including in the death safeguard.

### 5.3 The reasoner (`legal/legal_reasoner.py`, `legal_stage.py`)

1. **Candidate selection.** Instead of testing every section on every case, a section is kept if it was alleged (BNS number, or IPC number via the crosswalk) or a keyword occurs un-negated in the evidence. Sections with no keywords (for example BNSS 193, the procedural basis) are always kept. If the case cites IPC sections, the summary notes that BNS applies only to offences on or after 1 July 2024.
2. **Narrative evidence.** The reasoner used to see only medical, forensic, timeline and recovered-property facts; witness statements, FIR narrative and complaint text never reached it. The legal stage now splits these into sentences, each carrying a `SourceReference` with the exact sentence as excerpt. This also lets click-to-source highlight the supporting sentence.
3. **Per-ingredient result.** Each ingredient gets a status (`supported`, `requires_review`, `not_established`), a confidence, and an `evidence_quote`. At most the three best-scoring supporting items are kept, so the chargesheet does not bloat. A negated ingredient becomes `not_established` and its evidence is recorded as contradicting.
4. **Death safeguard preserved and fixed.** If the victim survived and no fatal record exists, death-based ingredients are contradicted. Survival and fatality checks now use the negation-aware `mentions`.
5. **Zero-element sections** are never "supported" without evidence.
6. **Court-readiness.**
   - `court_readiness = (supported + 0.5 * requires_review) / total_elements`, multiplied by 0.8 if there is a conflict or a contradicted ingredient, rounded to two places.
   - `evidence_gaps` lists each missing ingredient plus every document type in `expected_documents` that is absent from the case (for example "No postmortem report on record (normally needed to prove Section 106)").
7. **Offence facts** (`punishment`, `cognizable`, `bailable`, `triable_by`) are copied onto each finding and into `ChargeSheetLegalFinding`, so they appear in the chargesheet data and PDF.

### Result

A theft case yields Section 303 with all three ingredients supported and quoted, readiness 1.0, "cognizable, non-bailable", and a gap for a missing seizure memo. Unrelated sections such as murder are not proposed. A case with a surviving victim does not support Section 103 or 106.

---

## 6. Feature 3: Cross-document contradiction detector

**Goal:** surface the inconsistencies a defence lawyer would find, side by side, before the chargesheet is filed.

### Design principles

- Deterministic and high precision: each check compares an explicit structured value with what another document states.
- It never decides which side is right; it shows both with excerpts.
- Contradictions are **advisory**. There is no dismiss workflow in the MVP, so they are not finalisation blockers (descriptions deliberately avoid the words the completeness reporter treats as blocking).

### Checks (`backend/src/contradictions/detector.py`)

| Kind | Logic | Severity |
|---|---|---|
| Time | FIR time versus clock times in **incident** sentences of other documents. Colon times and marked times (am, pm, hrs) are parsed; times without am or pm are tried both ways. Flag if the gap exceeds 2 hours | High above 6 hours, else medium |
| Date | FIR date versus ISO, DD/MM/YYYY and "14 August 2025" dates in incident sentences | High above 7 days, else medium |
| Vehicle | Registration sets (structured fields plus a regex over narratives) with no overlap between the FIR and another document | Medium |
| Location | FIR place versus panchnama, site plan and CCTV location, after removing generic words ("road", "metro station", "new delhi") so only distinctive words are compared | Medium |
| Accused | FIR accused versus names in the complaint, fuzzy match (token-set ratio 80) | High |
| Victim | FIR victim versus the patient in the medical report | Medium |
| Life status | A narrative describes a death while a medical report says alive or a post-mortem is "not applicable" (and the reverse) | High / medium |
| Chronology | A witness statement dated before the incident | High |

"Incident sentence" means it contains an incident cue (accident, collision, assault, robbery ...) and no later-event cue (reached, arrived, reported, hospital, police station, seized, arrested ...). This stops "I reached the police station at 11:30 am" from being read as a contradictory occurrence time. Negation-aware matching prevents "the injury was not fatal" from being read as a death.

### Integration

`ChargeSheetStage` runs the detector on `context.parsed_documents` after the populator. Findings are:
- appended to `ChargeSheetData.conflicts` as `ChargeSheetReviewItem(category="cross_document_check", ...)`, so they print in the PDF under "Conflicts Requiring Review";
- stored in a new `ChargeSheetData.contradictions` list with both sides, excerpts and a "why it matters" sentence, for the review UI.

Each side's excerpt becomes a `SourceReference`, so click-to-source can open the exact sentence.

---

## 7. Feature 4: Signed and verifiable final PDF

**Goal:** a "final approved" chargesheet that can be proved authentic and unaltered, together with its approval history, by anyone holding the document.

### Architecture

```
Officer approves, then finalizes
        |
        v
ReviewService.finalize
  1. Render final PDF with QR code and a reserved signature slot
  2. Embed a visible PAdES signature (pyHanko) in that slot
  3. Append FINALIZED event to the hash-chained audit log
  4. Create a seal over: sha256(signed PDF), audit head hash, chargesheet content hash
        |
        v
final/ChargeSheet_vN_final.pdf   +   ChargeSheet_vN_final.seal.json
        |
        v   (anyone)
GET  /verify/{case}                            public HTML page
GET  /api/v1/cases/{case}/verification         checks the stored PDF
POST /api/v1/cases/{case}/verification/upload  checks any copy you were given
```

### 7.1 Hash-chained audit log

- **Files:** `review/audit_chain.py`, `review/review_models.py`, `review/review_service.py`
- Each `ReviewEvent` now has `prev_hash` and `event_hash`. `event_hash` is the SHA-256 of the event's canonical JSON (excluding the hash itself), which includes `prev_hash`. The first event links to `"GENESIS"`.
- `verify_chain` recomputes every link and reports the first altered event.
- **Why:** review history was plain JSON on disk, so anyone with file access could rewrite who approved what. Now an edit is detectable. Fields are optional, so old state files still load (but report "no hash; cannot be verified").

### 7.2 Signing identity

- **File:** `signing/identity.py`
- On first use, an RSA-2048 key and a self-signed X.509 certificate (with digital-signature and non-repudiation key usage) are created in `<storage root>/_signing/`. RSA is used for compatibility with PDF readers.
- The certificate is clearly labelled "Self-signed demo certificate (not a licensed DSC)".

### 7.3 Embedded PDF signature

- **File:** `signing/pades.py`
- pyHanko appends an incremental signature (field `OfficerApprovalSignature`, SHA-256) with a visible stamp: signer, date and reason.
- **Layout:** the renderer places an empty `SignatureSlot` flowable next to the QR code. After layout it records the page number and absolute coordinates, and pyHanko uses exactly those. The stamp therefore never overlaps content, whatever the page count.
- `validate_embedded` validates the signature using this system's certificate as the only trust root and reports: present, intact, trusted, covers the entire file.

### 7.4 The seal

- **File:** `signing/seal.py`
- A JSON document containing the case, version, `pdf_sha256` (of the signed file), `chargesheet_content_hash`, `audit_head_hash`, timestamp and signer, signed with RSA-SHA256, plus the certificate. It is stored beside the PDF.
- The seal binds three things together: the exact bytes of the PDF, the approved chargesheet content, and the audit history up to finalisation. Rewriting history cannot be hidden because the head hash is signed.

### 7.5 Verification checks

| Check | Fails when |
|---|---|
| Document integrity | The PDF bytes differ from the signed ones |
| Signature | The seal signature is invalid |
| Trusted signer | The seal was signed by a different key |
| Embedded PDF signature | Missing, altered, partial coverage, or untrusted |
| Audit trail | Any event or link was edited |
| Audit trail matches seal | The history differs from what was signed |
| Content binding | The approved chargesheet differs from the signed content |

Tests show that one flipped byte fails document integrity and the embedded signature only, that a rewritten history fails the audit trail, and that a seal produced with another key is not trusted.

### 7.6 QR code and public page

The final PDF carries a QR code (ReportLab, no extra dependency) to `PUBLIC_BASE_URL/verify/{case}` (default `http://127.0.0.1:8000`). The self-contained page shows the checks for the stored document and lets a user upload any PDF to check it. It is built with DOM `textContent` only, so case data cannot inject markup.

Implementation note: pyHanko validation uses asyncio internally, so the upload endpoint runs it through `run_in_threadpool` to avoid a "running event loop" error.

---

## 8. Demo data seeding

- **File:** `backend/scripts/seed_demo_cases.py` (run with `python scripts/seed_demo_cases.py [--storage-root PATH] [--public-base-url URL]`)
- Creates two cases through the real nine-stage pipeline. Only document **parsing** is scripted (`ScriptedParserClient` returns authored structured data in place of Gemini), so the demo works offline and is identical on every run. The source documents are real generated PDFs, so OCR, boxes and click-to-source all work.

| Case | Content |
|---|---|
| `DEMO_COMPLETED_KarolBagh_Robbery` | 10 documents. Corrections add the final opinion and signature; the case is approved and finalised, signed and QR-verifiable. No contradictions; sections 115, 117, 118, 303, 309, 317 and 351 supported |
| `DEMO_DRAFT_Dwarka_HitAndRun` | 6 documents. Planted: time mismatch, accused name mismatch, witness statement dated before the incident, vehicle number mismatch, location mismatch. Missing court (a critical blocker), no final opinion; Section 106 shows "insufficient evidence" because the victim survived |

Re-running deletes and recreates only these two IDs. To make the QR scannable from a phone, pass `--public-base-url http://<laptop-ip>:8000` and start the API with `--host 0.0.0.0`.

---

## 9. API additions

| Method and path | Purpose |
|---|---|
| `GET /api/v1/cases/{case}/sources/{doc}` | Source document info |
| `GET /api/v1/cases/{case}/sources/{doc}/pages/{n}/image` | Rendered page |
| `GET /api/v1/cases/{case}/sources/{doc}/locate` | Locate text on pages |
| `GET /api/v1/cases/{case}/verification` | Verify the stored final PDF |
| `POST /api/v1/cases/{case}/verification/upload` | Verify an uploaded copy (25 MB limit) |
| `GET /verify/{case}` | Public verification page |

Existing review responses now also carry `contradictions`, and each legal finding carries `court_readiness`, `evidence_gaps`, `punishment`, `cognizable`, `bailable`, `triable_by`, plus per-ingredient `confidence` and `evidence_quote`.

## 10. Dependencies

Added to `backend/requirements.txt`: `pymupdf` (PDF text, boxes, page images; note its AGPL licence), `rapidfuzz` (fuzzy matching), `pyhanko` (PAdES signing and validation). `cryptography` was already present and is used for the identity and seal.

## 11. Testing

The suite grew from 187 to 224 passing tests (2 skipped as before). New test files:

| File | Covers |
|---|---|
| `test_trust_fixes.py` | No mock fallback, Unicode names, prompt delimiters, PDF boxes, scanned-PDF fallback |
| `test_source_tracing.py` | Locator accuracy (including Devanagari), endpoints, pipeline traceability |
| `test_legal_section_suggestion.py` | Matching, negation, candidate selection, IPC crosswalk, readiness and gaps |
| `test_contradiction_detector.py` | Every contradiction type, plus false-positive guards |
| `test_signed_verifiable_pdf.py` | Hash chain, seal, tamper detection, embedded signature, endpoints |

Five existing tests were changed because they asserted the old behaviour: the end-to-end fixture now correctly lands in `review_required` (it lacks FIR number, station and timeline); the phase-1 parser-failure test now expects a failed core document to stop the case; the information-preservation fixture gained a police station; the Delhi regression allows Section 106 to be absent while still forbidding it from being "supported"; the RAG test still forbids retrieval alone from establishing an ingredient; and the failed-job test now simulates a provider outage instead of relying on an accidental crash.

## 12. Known limitations and honest caveats

- **Legal data is unverified.** The 30 new sections were written from general knowledge and flagged `verified: false`. Punishments, cognizability and bailability need expert review before any real use. The legal reasoner suggests sections for an officer to decide; it does not decide.
- **Scripted parsing in the demo.** Real Gemini parsing was not run in this work. Mock-mode parsing produces poor narrative text, so section suggestion needs real parsing to show its full value on uploaded documents.
- **Self-signed certificate.** Signatures verify against this system's own authority. Adobe Acrobat will show the signature as intact but the signer as untrusted unless the certificate is added to its trust list. A production system would use a licensed DSC or an eSign service and keep the private key in an HSM.
- **Contradictions are heuristic.** They are precise rather than exhaustive: for example, a time in a sentence with no incident cue is ignored, and place comparison depends on distinctive words.
- **Candidate selection is keyword-based.** A relevant offence whose keywords never appear will not be proposed.
- **Click-to-source depends on box quality.** Boxes from a digital text layer are exact; boxes from Gemini OCR on messy scans can be imprecise.
- **Not changed:** no authentication, no database, in-memory job tracking, no PII redaction. These were out of scope for the MVP.

## 13. Where things live

```
backend/src/
  text_normalization.py            Unicode-aware matching helpers
  extraction/pdf_extractor.py      PyMuPDF text and line boxes
  tracing/locator.py               text -> page boxes
  legal/ingredient_matcher.py      negation-aware ingredient matching
  legal/legal_reasoner.py          candidate selection, readiness, gaps
  legal/legal_stage.py             narrative evidence for the reasoner
  contradictions/                  models.py, detector.py
  review/audit_chain.py            hash-chained events
  signing/                         identity.py, pades.py, seal.py
  api/services/source_service.py   page images and locate
  api/services/verification_service.py
  api/routers/sources.py, verification.py
backend/references/legal/bns_sections.json
backend/scripts/seed_demo_cases.py
```
