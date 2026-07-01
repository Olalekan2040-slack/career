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
  getDashboardResults: () => request('/api/dashboard/results'),
  createLead: (payload) => request('/api/leads', { method: 'POST', body: JSON.stringify(payload) }),
  getQuestions: () => request('/api/questions'),
  routeTrack: (orientationAnswers) => request('/api/questions/route', { method: 'POST', body: JSON.stringify(orientationAnswers) }),
  submitAssessment: (payload) => request('/api/submit', { method: 'POST', body: JSON.stringify(payload) }),
  getResult: (resultId) => request(`/api/result/${resultId}`),
  checkoutStripe: (resultId) => request('/api/checkout/stripe', { method: 'POST', body: JSON.stringify({ result_id: resultId }) }),
  checkoutPaystack: (resultId) => request('/api/checkout/paystack', { method: 'POST', body: JSON.stringify({ result_id: resultId }) }),
  bookConsultation: (payload) => request('/api/consultation', { method: 'POST', body: JSON.stringify(payload) }),
  joinWaitlist: (payload) => request('/api/waitlist', { method: 'POST', body: JSON.stringify(payload) }),
};
