import { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { api } from '../api/client';
import { useAuth } from '../api/AuthContext';

function ResultSummary({ result }) {
  const rankedScores = Object.entries(result.scores).sort((a, b) => b[1] - a[1]);
  const date = new Date(result.created_at).toLocaleDateString(undefined, {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  });

  return (
    <div className="card" style={{ padding: 24, marginBottom: 20 }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
        <p className="pill">Track {result.track} · {date}</p>
        <Link to={`/results/${result.id}`} style={{ fontSize: 13 }}>
          View full page →
        </Link>
      </div>

      {result.close_call && (
        <p style={{ fontSize: 13, color: 'var(--accent-dark)', marginTop: 10 }}>{result.close_call_message}</p>
      )}

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16, marginTop: 16 }}>
        <div>
          <p style={{ fontSize: 12, fontWeight: 700, textTransform: 'uppercase', letterSpacing: 0.5, color: 'var(--accent-dark)' }}>
            Primary
          </p>
          <h3 style={{ marginTop: 4 }}>{result.primary.name}</h3>
          <p style={{ fontSize: 13 }}>{result.primary.focus}</p>
        </div>
        <div>
          <p style={{ fontSize: 12, fontWeight: 700, textTransform: 'uppercase', letterSpacing: 0.5, color: 'var(--accent-dark)' }}>
            Secondary
          </p>
          <h3 style={{ marginTop: 4 }}>{result.secondary.name}</h3>
          <p style={{ fontSize: 13 }}>{result.secondary.focus}</p>
        </div>
      </div>

      <p style={{ fontSize: 12, fontWeight: 700, textTransform: 'uppercase', letterSpacing: 0.5, color: 'var(--accent-dark)', marginTop: 20 }}>
        Your Strengths (all categories, ranked)
      </p>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8, marginTop: 8 }}>
        {rankedScores.map(([key, score]) => (
          <span key={key} className="pill" style={{ background: 'var(--milk-panel)', color: 'var(--ink)' }}>
            {key}: {score}
          </span>
        ))}
      </div>

      {[result.primary, result.secondary].map(
        (category) =>
          category.curriculum && (
            <div key={category.key} style={{ marginTop: 20 }}>
              <p style={{ fontWeight: 700, fontSize: 13, textTransform: 'uppercase', letterSpacing: 0.5, color: 'var(--accent-dark)' }}>
                {category.name} — Course Outline
              </p>
              <ul style={{ paddingLeft: 18 }}>
                {category.curriculum.map((step) => (
                  <li key={step} style={{ marginBottom: 4, fontSize: 14 }}>
                    {step}
                  </li>
                ))}
              </ul>
            </div>
          )
      )}
    </div>
  );
}

export default function Dashboard() {
  const { user, loading: authLoading } = useAuth();
  const navigate = useNavigate();
  const [results, setResults] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    if (authLoading) return;
    if (!user) {
      navigate('/login');
      return;
    }
    api
      .getDashboardResults()
      .then(setResults)
      .catch(() => setError('Could not load your results.'));
  }, [authLoading, user, navigate]);

  if (authLoading || (!results && !error)) {
    return (
      <div className="container" style={{ paddingTop: 60, textAlign: 'center' }}>
        <p>Loading your dashboard…</p>
      </div>
    );
  }

  return (
    <div className="container" style={{ paddingTop: 48, paddingBottom: 40, maxWidth: 720 }}>
      <p className="pill">Your Dashboard</p>
      <h1 style={{ fontSize: 30, marginTop: 12 }}>Welcome back, {user.name.split(' ')[0]}</h1>
      <p>Every assessment you take is saved here with full strengths and course outline — no charge.</p>

      <button className="btn btn-primary" onClick={() => navigate('/assessment')} style={{ marginBottom: 24 }}>
        Take a new assessment →
      </button>

      {error && <p style={{ color: 'var(--danger)' }}>{error}</p>}

      {results && results.length === 0 && (
        <div className="card" style={{ padding: 24, textAlign: 'center' }}>
          <p>You haven't taken an assessment yet.</p>
        </div>
      )}

      {results && results.map((result) => <ResultSummary key={result.id} result={result} />)}
    </div>
  );
}
