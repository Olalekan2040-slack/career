import { useEffect, useMemo, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { api } from '../api/client';
import { useAuth } from '../api/AuthContext';

const STAGE_ORIENTATION = 'orientation';
const STAGE_DEEP_DIVE = 'deep_dive';

export default function Assessment() {
  const navigate = useNavigate();
  const { user, loading: authLoading } = useAuth();
  const [lead, setLead] = useState(null);
  const [questionSet, setQuestionSet] = useState(null);
  const [stage, setStage] = useState(STAGE_ORIENTATION);
  const [track, setTrack] = useState(null);
  const [index, setIndex] = useState(0);
  const [orientationAnswers, setOrientationAnswers] = useState({});
  const [deepDiveAnswers, setDeepDiveAnswers] = useState({});
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    if (authLoading) return;

    async function initLead() {
      const storedLead = sessionStorage.getItem('lead');
      if (storedLead) {
        setLead(JSON.parse(storedLead));
        return true;
      }
      if (user) {
        // Signed-in users skip the lead-capture form — use their account details.
        const newLead = await api.createLead({ name: user.name, email: user.email, consent_given: true });
        sessionStorage.setItem('lead', JSON.stringify(newLead));
        setLead(newLead);
        return true;
      }
      navigate('/start');
      return false;
    }

    initLead().then((ready) => {
      if (!ready) return;
      api
        .getQuestions()
        .then(setQuestionSet)
        .catch(() => setError('Could not load the assessment. Please refresh the page.'))
        .finally(() => setLoading(false));
    });
  }, [navigate, user, authLoading]);

  const activeQuestions = useMemo(() => {
    if (!questionSet) return [];
    if (stage === STAGE_ORIENTATION) return questionSet.orientation;
    return track === 'A' ? questionSet.track_a_deep_dive : questionSet.track_b_deep_dive;
  }, [questionSet, stage, track]);

  const currentQuestion = activeQuestions[index];
  const orientationCount = questionSet?.orientation.length ?? 8;
  const deepDiveCount =
    stage === STAGE_DEEP_DIVE
      ? activeQuestions.length
      : ((questionSet?.track_a_deep_dive.length ?? 12) + (questionSet?.track_b_deep_dive.length ?? 13)) / 2;
  const totalSteps = stage === STAGE_ORIENTATION ? orientationCount : activeQuestions.length;
  const overallTotal = orientationCount + deepDiveCount;
  const overallDone = stage === STAGE_ORIENTATION ? index : orientationCount + index;

  async function handleAnswer(optionKey) {
    if (stage === STAGE_ORIENTATION) {
      const updated = { ...orientationAnswers, [currentQuestion.id]: optionKey };
      setOrientationAnswers(updated);

      if (index + 1 < activeQuestions.length) {
        setIndex(index + 1);
        return;
      }

      // Orientation complete — determine track
      setLoading(true);
      try {
        const { track: resolvedTrack } = await api.routeTrack(updated);
        setTrack(resolvedTrack);
        setStage(STAGE_DEEP_DIVE);
        setIndex(0);
      } catch {
        setError('Could not determine your track. Please try again.');
      } finally {
        setLoading(false);
      }
      return;
    }

    // Deep-dive stage
    const updated = { ...deepDiveAnswers, [currentQuestion.id]: optionKey };
    setDeepDiveAnswers(updated);

    if (index + 1 < activeQuestions.length) {
      setIndex(index + 1);
      return;
    }

    // Final question answered — submit
    setSubmitting(true);
    try {
      const result = await api.submitAssessment({
        lead_id: lead.id,
        orientation_answers: orientationAnswers,
        deep_dive_answers: updated,
      });
      navigate(`/results/${result.id}`);
    } catch {
      setError('Something went wrong submitting your assessment. Please try again.');
      setSubmitting(false);
    }
  }

  function handleBack() {
    if (index > 0) {
      setIndex(index - 1);
    }
  }

  if (loading || submitting) {
    return (
      <div className="container" style={{ paddingTop: 80, textAlign: 'center' }}>
        <p>{submitting ? 'Scoring your results…' : 'Loading…'}</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="container" style={{ paddingTop: 80, textAlign: 'center' }}>
        <p style={{ color: 'var(--danger)' }}>{error}</p>
      </div>
    );
  }

  if (!currentQuestion) {
    return null;
  }

  const progressPct = Math.round((overallDone / (overallTotal || 1)) * 100);

  return (
    <div className="container" style={{ paddingTop: 48, paddingBottom: 40, maxWidth: 560 }}>
      <div style={{ marginBottom: 24 }}>
        <div
          style={{
            height: 8,
            borderRadius: 999,
            background: 'var(--milk-panel-alt)',
            overflow: 'hidden',
          }}
        >
          <div
            style={{
              height: '100%',
              width: `${progressPct}%`,
              background: 'var(--accent)',
              transition: 'width 0.3s ease',
            }}
          />
        </div>
        <p style={{ fontSize: 12, marginTop: 8, color: 'var(--ink-soft)' }}>
          {stage === STAGE_ORIENTATION ? 'Orientation' : 'Deep-Dive'} · Question {index + 1} of {totalSteps}
        </p>
      </div>

      <div className="card" style={{ padding: 28 }}>
        <h2 style={{ fontSize: 22 }}>{currentQuestion.text}</h2>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 12, marginTop: 20 }}>
          {currentQuestion.options.map((opt) => (
            <button
              key={opt.key}
              className="btn btn-outline"
              style={{ justifyContent: 'flex-start', textAlign: 'left', fontWeight: 400, padding: '16px 18px' }}
              onClick={() => handleAnswer(opt.key)}
            >
              <span style={{ fontWeight: 700, marginRight: 10 }}>{opt.key}.</span>
              {opt.text}
            </button>
          ))}
        </div>
      </div>

      {index > 0 && (
        <button className="btn btn-outline" style={{ marginTop: 16 }} onClick={handleBack}>
          ← Back
        </button>
      )}
    </div>
  );
}
