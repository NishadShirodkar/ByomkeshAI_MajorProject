/**
 * Authenticity verification of finalized charge sheets (digital seal + audit trail).
 */

import { apiClient } from "./apiClient.js";

export const verificationService = {
  verify(caseId) {
    if (!caseId) throw new Error("caseId is required");
    return apiClient.get(`/api/v1/cases/${encodeURIComponent(caseId)}/verification`);
  },

  verifyCopy(caseId, file) {
    if (!caseId || !file) throw new Error("caseId and file are required");
    const form = new FormData();
    form.append("file", file);
    return apiClient.post(`/api/v1/cases/${encodeURIComponent(caseId)}/verification/upload`, form);
  },

  publicPageUrl(caseId) {
    if (!caseId) throw new Error("caseId is required");
    return `${apiClient.getBaseUrl()}/verify/${encodeURIComponent(caseId)}`;
  },
};
