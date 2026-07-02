import { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { api } from '../api/client';
import ConsultationCTA from '../components/ConsultationCTA';

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
  const navigate = useNavigate();
  const [result, setResult] = useState(null);
  const [lead, setLead] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    const storedLead = sessionStorage.getItem('lead');
    if (storedLead) setLead(JSON.parse(storedLead));

    api
      .getResult(resultId)
      .then(setResult)
      .catch(() => setError('We could not find this result.'));
  }, [resultId]);

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
      <p className="pill">Your Top {result.recommendations.length} Matches</p>
      <h1 style={{ fontSize: 30, marginTop: 12 }}>
        Here are your top {result.recommendations.length} recommended careers
      </h1>

      {result.close_call && (
        <div className="card" style={{ padding: 18, background: 'var(--milk-panel-alt)', marginBottom: 20 }}>
          <p style={{ margin: 0 }}>{result.close_call_message}</p>
        </div>
      )}

      {result.recommendations.map((rec) => (
        <RecommendationCard key={rec.career.key} recommendation={rec} />
      ))}

      {lead && <ConsultationCTA leadId={lead.id} />}
    </div>
  );
}
