import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { api } from '../api/client';

export default function LeadCapture() {
  const navigate = useNavigate();
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [consent, setConsent] = useState(true);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e) {
    e.preventDefault();
    setError('');
    if (!name.trim() || !email.trim()) {
      setError('Please fill in your name and email.');
      return;
    }
    setLoading(true);
    try {
      const lead = await api.createLead({ name: name.trim(), email: email.trim(), consent_given: consent });
      sessionStorage.setItem('lead', JSON.stringify(lead));
      navigate('/assessment');
    } catch {
      setError('Something went wrong creating your session. Please try again.');
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="container" style={{ paddingTop: 56, paddingBottom: 40, maxWidth: 480 }}>
      <p className="pill">Step 1 of 2</p>
      <h1 style={{ fontSize: 28, marginTop: 12 }}>Let's get you started</h1>
      <p>Just your name and email — your full result will be sent there when you're done.</p>

      <form onSubmit={handleSubmit} className="card" style={{ padding: 24, marginTop: 20 }}>
        <label htmlFor="name">Full Name</label>
        <input
          id="name"
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Ada Lovelace"
          style={{ marginBottom: 16 }}
        />
        <label htmlFor="email">Email</label>
        <input
          id="email"
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="you@example.com"
          style={{ marginBottom: 16 }}
        />
        <label style={{ display: 'flex', alignItems: 'flex-start', gap: 8, fontWeight: 400, fontSize: 13 }}>
          <input
            type="checkbox"
            checked={consent}
            onChange={(e) => setConsent(e.target.checked)}
            style={{ width: 'auto', marginTop: 2 }}
          />
          I agree to receive my result and occasional career-path emails. No spam, unsubscribe anytime.
        </label>
        {error && <p style={{ color: 'var(--danger)', marginTop: 12 }}>{error}</p>}
        <button className="btn btn-primary btn-block" type="submit" disabled={loading} style={{ marginTop: 20 }}>
          {loading ? 'Starting…' : 'Continue to Assessment →'}
        </button>
      </form>
    </div>
  );
}
