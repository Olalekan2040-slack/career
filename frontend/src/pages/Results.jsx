import { useCallback, useEffect, useRef, useState } from 'react';
import { Link, useNavigate, useParams, useSearchParams } from 'react-router-dom';
import { api } from '../api/client';
import { useAuth } from '../api/AuthContext';
import ConsultationCTA from '../components/ConsultationCTA';

function likelyNigerian() {
  try {
    return (navigator.language || '').toLowerCase().includes('-ng');
  } catch {
    return false;
  }
}

function RecommendationCard({ recommendation }) {
  const { career, reason, rank } = recommendation;
  return (
    <div className="card" style={{ padding: 24, marginBottom: 16 }}>
      <p className="pill">Recommendation #{rank}</p>
      <h3 style={{ marginTop: 10 }}>{career.name}</h3>
      <p>{career.focus}</p>
      <p style={{ fontSize: 13, color: 'var(--ink-soft)' }}>Typical duration: {career.duration}</p>
      <p style={{ fontSize: 14, color: 'var(--accent-dark)', fontStyle: 'italic', marginTop: 10 }}>
        Why this fits: {reason}
      </p>
      <p style={{ fontWeight: 700, fontSize: 13, textTransform: 'uppercase', letterSpacing: 0.5, color: 'var(--accent-dark)', marginTop: 16 }}>
        Curriculum Path
      </p>
      <ul style={{ paddingLeft: 18 }}>
        {career.curriculum.map((step) => (
          <li key={step} style={{ marginBottom: 6 }}>
            {step}
          </li>
        ))}
      </ul>
      <p style={{ fontWeight: 700, fontSize: 13, textTransform: 'uppercase', letterSpacing: 0.5, color: 'var(--accent-dark)', marginTop: 16 }}>
        Recommended Resources
      </p>
      <ul style={{ paddingLeft: 18 }}>
        {career.resources.map((res) => (
          <li key={res} style={{ marginBottom: 6 }}>
            {res}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default function Results() {
  const { resultId } = useParams();
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();
  const { user } = useAuth();
  const [result, setResult] = useState(null);
  const [lead, setLead] = useState(null);
  const [error, setError] = useState('');
  const [paying, setPaying] = useState(false);
  const [confirming, setConfirming] = useState(searchParams.get('payment') === 'confirming' || searchParams.get('payment') === 'success');
  const [provider, setProvider] = useState(likelyNigerian() ? 'paystack' : 'stripe');
  const pollRef = useRef(null);

  const fetchResult = useCallback(async () => {
    try {
      const data = await api.getResult(resultId);
      setResult(data);
      return data;
    } catch {
      setError('We could not find this result.');
      return null;
    }
  }, [resultId]);

  useEffect(() => {
    const storedLead = sessionStorage.getItem('lead');
    if (storedLead) setLead(JSON.parse(storedLead));
    fetchResult();
  }, [fetchResult]);

  useEffect(() => {
    if (!confirming) return;
    pollRef.current = setInterval(async () => {
      const data = await fetchResult();
      if (data?.unlocked) {
        setConfirming(false);
        clearInterval(pollRef.current);
      }
    }, 2500);
    return () => clearInterval(pollRef.current);
  }, [confirming, fetchResult]);

  async function handleUnlock() {
    setPaying(true);
    try {
      const session =
        provider === 'paystack' ? await api.checkoutPaystack(resultId) : await api.checkoutStripe(resultId);
      window.location.href = session.checkout_url;
    } catch {
      setError('Could not start checkout. Please try again.');
      setPaying(false);
    }
  }

  if (error) {
    return (
      <div className="container" style={{ paddingTop: 60, textAlign: 'center' }}>
        <p style={{ color: 'var(--danger)' }}>{error}</p>
        <button className="btn btn-outline" onClick={() => navigate('/')}>
          Back to home
        </button>
      </div>
    );
  }

  if (!result) {
    return (
      <div className="container" style={{ paddingTop: 60, textAlign: 'center' }}>
        <p>Loading your result…</p>
      </div>
    );
  }

  return (
    <div className="container" style={{ paddingTop: 48, paddingBottom: 40, maxWidth: 640 }}>
      <p className="pill">
        {result.unlocked ? 'Full Result — Top 4 Matches' : 'Your Top 2 Matches'}
      </p>
      <h1 style={{ fontSize: 30, marginTop: 12 }}>
        {result.unlocked ? 'Here are your top 4 recommended careers' : 'Here are your top 2 recommended careers'}
      </h1>

      {result.close_call && (
        <div className="card" style={{ padding: 18, background: 'var(--milk-panel-alt)', marginBottom: 20 }}>
          <p style={{ margin: 0 }}>{result.close_call_message}</p>
        </div>
      )}

      {result.recommendations.map((rec) => (
        <RecommendationCard key={rec.career.key} recommendation={rec} />
      ))}

      {!result.unlocked && (
        <div className="card" style={{ padding: 26, marginTop: 8, textAlign: 'center' }}>
          {!user && (
            <>
              <h3>Create a free account to see your top 4 matches</h3>
              <p>
                Get 2 more recommendations, with the same full curriculum and reasons — saved to your
                dashboard, free forever.
              </p>
              <Link to="/signup" className="btn btn-primary btn-block" style={{ textDecoration: 'none', marginBottom: 20 }}>
                Sign up free →
              </Link>
              <p style={{ fontSize: 13, color: 'var(--ink-soft)', margin: '0 0 12px 0' }}>
                — or unlock your top 4 for $1 without an account —
              </p>
            </>
          )}

          <div style={{ display: 'flex', justifyContent: 'center', gap: 8, marginBottom: 18 }}>
            <button
              className={provider === 'stripe' ? 'btn btn-primary' : 'btn btn-outline'}
              onClick={() => setProvider('stripe')}
              type="button"
            >
              Pay with card (international)
            </button>
            <button
              className={provider === 'paystack' ? 'btn btn-primary' : 'btn btn-outline'}
              onClick={() => setProvider('paystack')}
              type="button"
            >
              Pay with Nigerian card/bank
            </button>
          </div>

          <p style={{ fontSize: 13, marginBottom: 16 }}>
            {provider === 'stripe' ? '$1.00 USD' : '$1 USD (~₦1,500)'}
          </p>

          <button className="btn btn-outline btn-block" onClick={handleUnlock} disabled={paying || confirming}>
            {confirming ? 'Confirming payment…' : paying ? 'Redirecting…' : 'Unlock Top 4 Matches — $1'}
          </button>
        </div>
      )}

      {lead && <ConsultationCTA leadId={lead.id} />}
    </div>
  );
}
