/**
 * Click-to-source tracing: source document info, text location and rendered pages.
 */

import { apiClient } from "./apiClient.js";

function base(caseId, documentId) {
  if (!caseId || !documentId) throw new Error("caseId and documentId are required");
  return `/api/v1/cases/${encodeURIComponent(caseId)}/sources/${encodeURIComponent(documentId)}`;
}

export const sourceService = {
  getInfo(caseId, documentId) {
    return apiClient.get(base(caseId, documentId));
  },

  async locate(caseId, documentId, text, page = null) {
    const params = new URLSearchParams({ text: String(text).slice(0, 2000) });
    if (page) params.set("page", String(page));
    const data = await apiClient.get(`${base(caseId, documentId)}/locate?${params}`);
    return data?.matches || [];
  },

  async getPageImageUrl(caseId, documentId, pageNumber) {
    const { blob } = await apiClient.downloadBlob(`${base(caseId, documentId)}/pages/${pageNumber}/image`);
    return URL.createObjectURL(blob);
  },
};
