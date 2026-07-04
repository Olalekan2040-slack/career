const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

let authToken = null;

export function setAuthToken(token) {
  authToken = token;
}

async function request(path, options = {}) {
  const headers = { 'Content-Type': 'application/json' };
  if (authToken) headers.Authorization = `Bearer ${authToken}`;

  const res = await fetch(`${API_URL}${path}`, {
    headers,
    ...options,
  });
  if (!res.ok) {
    let message = `Request to ${path} failed with ${res.status}`;
    try {
      const body = await res.json();
      message = body.detail || message;
    } catch {
      // ignore non-JSON error bodies
    }
    throw new Error(message);
  }
  return res.json();
}

export const api = {
  // Best-effort keep-alive ping — swallows errors, never surfaces to the UI.
  ping: () => fetch(`${API_URL}/api/health`).catch(() => {}),
  signup: (payload) => request('/api/auth/signup', { method: 'POST', body: JSON.stringify(payload) }),
  login: (payload) => request('/api/auth/login', { method: 'POST', body: JSON.stringify(payload) }),
  me: () => request('/api/auth/me'),
  getMeta: () => request('/api/meta'),
  getAdminUsers: () => request('/api/admin/users'),
  getAdminLeads: () => request('/api/admin/leads'),
  createLead: (payload) => request('/api/leads', { method: 'POST', body: JSON.stringify(payload) }),
  getQuestions: () => request('/api/questions'),
  getIntakeSchema: () => request('/api/assessment/intake-schema'),
  getNextQuestion: (payload) => request('/api/assessment/next', { method: 'POST', body: JSON.stringify(payload) }),
  submitAssessment: (payload) => request('/api/submit', { method: 'POST', body: JSON.stringify(payload) }),
  getResult: (resultId) => request(`/api/result/${resultId}`),
  bookConsultation: (payload) => request('/api/consultation', { method: 'POST', body: JSON.stringify(payload) }),
};
