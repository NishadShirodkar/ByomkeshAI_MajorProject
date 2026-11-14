import React, { useEffect, useMemo, useState } from "react";
import { sourceService } from "../services/sourceService.js";

/**
 * Shows the original document page behind a charge-sheet field, with the
 * supporting text highlighted. References come from the field's provenance.
 */
export default function SourceViewer({ caseId, references, fieldText, title, onClose }) {
  const documents = useMemo(() => {
    const seen = new Map();
    for (const ref of references || []) {
      if (!seen.has(ref.document_id)) seen.set(ref.document_id, ref);
    }
    return [...seen.values()];
  }, [references]);

  const [activeIndex, setActiveIndex] = useState(0);
  const [info, setInfo] = useState(null);
  const [match, setMatch] = useState(null);
  const [page, setPage] = useState(1);
  const [imageUrl, setImageUrl] = useState(null);
  const [status, setStatus] = useState("loading");
  const [error, setError] = useState(null);

  const active = documents[activeIndex];

  useEffect(() => {
    if (!active) return undefined;
    let cancelled = false;
    setStatus("loading");
    setError(null);
    setMatch(null);
    setInfo(null);

    (async () => {
      try {
        const docInfo = await sourceService.getInfo(caseId, active.document_id);
        const hintPage = active.location?.page_number || null;
        const queries = [active.excerpt, fieldText].filter((q) => q && q.trim().length >= 3);
        let best = null;
        for (const query of queries) {
          const matches = await sourceService.locate(caseId, active.document_id, query, hintPage);
          if (matches.length) {
            best = matches[0];
            break;
          }
        }
        if (cancelled) return;
        setInfo(docInfo);
        setMatch(best);
        setPage(best?.page_number || hintPage || 1);
        setStatus("ready");
      } catch (err) {
        if (cancelled) return;
        setError(err.message || "Could not load source document.");
        setStatus("error");
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [caseId, active?.document_id, active?.excerpt, active?.location?.page_number, fieldText]);

  useEffect(() => {
    if (!active || status !== "ready") return undefined;
    let cancelled = false;
    let createdUrl = null;
    setImageUrl(null);
    sourceService
      .getPageImageUrl(caseId, active.document_id, page)
      .then((url) => {
        createdUrl = url;
        if (cancelled) URL.revokeObjectURL(url);
        else setImageUrl(url);
      })
      .catch((err) => {
        if (!cancelled) setError(err.message || "This source cannot be shown as a page image.");
      });
    return () => {
      cancelled = true;
      if (createdUrl) URL.revokeObjectURL(createdUrl);
    };
  }, [caseId, active?.document_id, page, status]);

  const boxes = match && match.page_number === page ? match.boxes : [];
  const pageCount = info?.page_count || 1;
  const exact = match && match.score >= 90;

  return (
    <div className="modal-overlay" onClick={onClose} id="source-viewer-overlay">
      <div className="modal-content" style={{ maxWidth: "980px" }} onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <div>
            <div style={{ fontWeight: 700, fontSize: "14px" }}>Source evidence{title ? `: ${title}` : ""}</div>
            {info && (
              <div style={{ fontSize: "11px", color: "var(--text-muted)", marginTop: "2px" }}>
                {info.filename || "Document"}
                {info.document_type ? ` • ${String(info.document_type).replace(/_/g, " ")}` : ""}
                {info.ocr_provider ? ` • read by ${info.ocr_provider}` : ""}
                {typeof info.ocr_confidence === "number" ? ` • OCR confidence ${(info.ocr_confidence * 100).toFixed(0)}%` : ""}
              </div>
            )}
          </div>
          <button className="btn btn-outline btn-sm" onClick={onClose} id="source-viewer-close">✕</button>
        </div>

        <div className="modal-body" style={{ display: "flex", flexDirection: "column", gap: "12px" }}>
          {documents.length > 1 && (
            <div style={{ display: "flex", gap: "8px", flexWrap: "wrap" }}>
              {documents.map((doc, idx) => (
                <button
                  key={doc.document_id}
                  className={`btn btn-sm ${idx === activeIndex ? "btn-primary" : "btn-outline"}`}
                  onClick={() => setActiveIndex(idx)}
                >
                  Source {idx + 1}
                </button>
              ))}
            </div>
          )}

          {status === "loading" && <div style={{ color: "var(--text-muted)", fontSize: "13px" }}>Locating evidence in the original document…</div>}
          {status === "error" && <div className="alert alert-danger" style={{ margin: 0 }}>✕ {error}</div>}

          {status === "ready" && (
            <>
              <div style={{ display: "flex", alignItems: "center", gap: "10px", flexWrap: "wrap", fontSize: "12px" }}>
                {match ? (
                  <span className={`badge ${exact ? "badge-extracted" : "badge-review-required"}`}>
                    {exact ? "EXACT TEXT MATCH" : `APPROXIMATE MATCH ${match.score}%`}
                  </span>
                ) : (
                  <span className="badge badge-review-required">TEXT NOT LOCATED, SHOWING PAGE</span>
                )}
                {match && <span style={{ color: "var(--text-secondary)" }}>“{match.matched_text.slice(0, 140)}”</span>}
              </div>

              <div style={{ display: "flex", alignItems: "center", gap: "8px" }}>
                <button className="btn btn-outline btn-sm" disabled={page <= 1} onClick={() => setPage(page - 1)}>◀</button>
                <span style={{ fontSize: "12px" }}>Page {page} of {pageCount}</span>
                <button className="btn btn-outline btn-sm" disabled={page >= pageCount} onClick={() => setPage(page + 1)}>▶</button>
              </div>

              <div style={{ position: "relative", alignSelf: "center", maxWidth: "100%", background: "#fff", border: "1px solid var(--border-strong)" }}>
                {imageUrl ? (
                  <>
                    <img src={imageUrl} alt={`Source page ${page}`} style={{ display: "block", maxWidth: "100%", maxHeight: "62vh" }} id="source-page-image" />
                    {boxes.map((box, idx) => (
                      <div
                        key={idx}
                        className="source-highlight"
                        style={{
                          position: "absolute",
                          left: `${box[0] * 100}%`,
                          top: `${box[1] * 100}%`,
                          width: `${(box[2] - box[0]) * 100}%`,
                          height: `${(box[3] - box[1]) * 100}%`,
                          background: "rgba(245, 158, 11, 0.35)",
                          outline: "2px solid #f59e0b",
                          pointerEvents: "none",
                        }}
                      />
                    ))}
                  </>
                ) : (
                  !error && <div style={{ padding: "40px", color: "#64748b", fontSize: "13px" }}>Rendering page…</div>
                )}
              </div>
              {error && <div className="alert alert-warning" style={{ margin: 0 }}>{error}</div>}
            </>
          )}
        </div>
      </div>
    </div>
  );
}
