import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../api/AuthContext';

export default function Login() {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e) {
    e.preventDefault();
    setError('');
    setLoading(true);
    try {
      await login(email.trim(), password);
      navigate('/dashboard');
    } catch (err) {
      setError(err.message || 'Could not log in.');
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="container" style={{ paddingTop: 56, paddingBottom: 40, maxWidth: 440 }}>
      <p className="pill">Welcome back</p>
      <h1 style={{ fontSize: 28, marginTop: 12 }}>Log in</h1>

      <form onSubmit={handleSubmit} className="card" style={{ padding: 24, marginTop: 20 }}>
        <label htmlFor="email">Email</label>
        <input id="email" type="email" value={email} onChange={(e) => setEmail(e.target.value)} style={{ marginBottom: 16 }} />
        <label htmlFor="password">Password</label>
        <input
          id="password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          style={{ marginBottom: 16 }}
        />
        {error && <p style={{ color: 'var(--danger)', marginBottom: 12 }}>{error}</p>}
        <button className="btn btn-primary btn-block" type="submit" disabled={loading}>
          {loading ? 'Logging in…' : 'Log in →'}
        </button>
      </form>

      <p style={{ marginTop: 16, fontSize: 14 }}>
        Don't have an account? <Link to="/signup">Sign up free</Link>
      </p>
    </div>
  );
}
