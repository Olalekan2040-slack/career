import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../api/AuthContext';

export default function Signup() {
  const { signup } = useAuth();
  const navigate = useNavigate();
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e) {
    e.preventDefault();
    setError('');
    if (password.length < 8) {
      setError('Password must be at least 8 characters.');
      return;
    }
    setLoading(true);
    try {
      await signup(name.trim(), email.trim(), password);
      navigate('/assessment');
    } catch (err) {
      setError(err.message || 'Could not create your account.');
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="container" style={{ paddingTop: 56, paddingBottom: 40, maxWidth: 440 }}>
      <p className="pill">Free account</p>
      <h1 style={{ fontSize: 28, marginTop: 12 }}>Create your account</h1>
      <p>
        Save every assessment you take, with full strengths and course outline in your dashboard — no $1
        charge required.
      </p>

      <form onSubmit={handleSubmit} className="card" style={{ padding: 24, marginTop: 20 }}>
        <label htmlFor="name">Full Name</label>
        <input id="name" type="text" value={name} onChange={(e) => setName(e.target.value)} style={{ marginBottom: 16 }} />
        <label htmlFor="email">Email</label>
        <input id="email" type="email" value={email} onChange={(e) => setEmail(e.target.value)} style={{ marginBottom: 16 }} />
        <label htmlFor="password">Password</label>
        <input
          id="password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="At least 8 characters"
          style={{ marginBottom: 16 }}
        />
        {error && <p style={{ color: 'var(--danger)', marginBottom: 12 }}>{error}</p>}
        <button className="btn btn-primary btn-block" type="submit" disabled={loading}>
          {loading ? 'Creating account…' : 'Create free account →'}
        </button>
      </form>

      <p style={{ marginTop: 16, fontSize: 14 }}>
        Already have an account? <Link to="/login">Log in</Link>
      </p>
    </div>
  );
}
