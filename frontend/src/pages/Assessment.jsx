import { useEffect, useMemo, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { api } from '../api/client';
import { useAuth } from '../api/AuthContext';

const SECTION_LABELS = {
  likert: 'Section A · Agree or Disagree',
  forced_choice: 'Section B · Pick One',
  scenario: 'Section C · Scenarios',
  situational: 'Section D · Workplace Situations',
  ranking: 'Section E · Rank Your Preferences',
};

const LIKERT_SCALE = [
  { value: 1, label: 'Strongly Disagree' },
  { value: 2, label: 'Disagree' },
  { value: 3, label: 'Neutral' },
  { value: 4, label: 'Agree' },
  { value: 5, label: 'Strongly Agree' },
];

function LikertQuestion({ question, onAnswer, onSkip }) {
  return (
    <div className="card" style={{ padding: 28 }}>
      <h2 style={{ fontSize: 20 }}>{question.text}</h2>
      <div style={{ display: 'flex', gap: 8, marginTop: 20, flexWrap: 'wrap' }}>
        {LIKERT_SCALE.map((opt) => (
          <button
            key={opt.value}
            className="btn btn-outline"
            style={{ flex: '1 1 auto', minWidth: 100, flexDirection: 'column', padding: '14px 10px' }}
            onClick={() => onAnswer(opt.value)}
          >
            <span style={{ fontSize: 20, fontWeight: 700 }}>{opt.value}</span>
            <span style={{ fontSize: 11, color: 'var(--ink-soft)' }}>{opt.label}</span>
          </button>
        ))}
      </div>
      <button className="btn btn-outline" style={{ marginTop: 16 }} onClick={onSkip}>
        Skip this question
      </button>
    </div>
  );
}

function ChoiceQuestion({ question, onAnswer, onSkip }) {
  return (
    <div className="card" style={{ padding: 28 }}>
      <h2 style={{ fontSize: 20 }}>{question.text}</h2>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 12, marginTop: 20 }}>
        {question.options.map((opt) => (
          <button
            key={opt.key}
            className="btn btn-outline"
            style={{ justifyContent: 'flex-start', textAlign: 'left', fontWeight: 400, padding: '16px 18px' }}
            onClick={() => onAnswer(opt.key)}
          >
            <span style={{ fontWeight: 700, marginRight: 10 }}>{opt.key}.</span>
            {opt.text}
          </button>
        ))}
      </div>
      <button className="btn btn-outline" style={{ marginTop: 16 }} onClick={onSkip}>
        Skip this question
      </button>
    </div>
  );
}

function RankingQuestion({ question, onAnswer, onSkip }) {
  const [order, setOrder] = useState([]);
  const remaining = question.items.filter((item) => !order.includes(item.key));

  function pick(itemKey) {
    const updated = [...order, itemKey];
    setOrder(updated);
    if (updated.length === question.items.length) {
      onAnswer(updated);
    }
  }

  function reset() {
    setOrder([]);
  }

  return (
    <div className="card" style={{ padding: 28 }}>
      <h2 style={{ fontSize: 20 }}>{question.text}</h2>
      <p style={{ fontSize: 13 }}>Click items in order, most appealing first.</p>

      {order.length > 0 && (
        <ol style={{ paddingLeft: 20, marginBottom: 16 }}>
          {order.map((key) => (
            <li key={key} style={{ marginBottom: 4, fontWeight: 600 }}>
              {question.items.find((i) => i.key === key)?.text}
            </li>
          ))}
        </ol>
      )}

      <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
        {remaining.map((item) => (
          <button
            key={item.key}
            className="btn btn-outline"
            style={{ justifyContent: 'flex-start', textAlign: 'left', fontWeight: 400, padding: '16px 18px' }}
            onClick={() => pick(item.key)}
          >
            {item.text}
          </button>
        ))}
      </div>

      <div style={{ display: 'flex', gap: 8, marginTop: 16 }}>
        {order.length > 0 && (
          <button className="btn btn-outline" onClick={reset}>
            Start over
          </button>
        )}
        <button className="btn btn-outline" onClick={onSkip}>
          Skip this question
        </button>
      </div>
    </div>
  );
}

export default function Assessment() {
  const navigate = useNavigate();
  const { user, loading: authLoading } = useAuth();
  const [lead, setLead] = useState(null);
  const [questionSet, setQuestionSet] = useState(null);
  const [index, setIndex] = useState(0);
  const [answers, setAnswers] = useState({
    likert: {},
    forced_choice: {},
    scenario: {},
    situational: {},
    ranking: {},
  });
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

  const steps = useMemo(() => {
    if (!questionSet) return [];
    const flat = [];
    for (const q of questionSet.likert) flat.push({ section: 'likert', question: q });
    for (const q of questionSet.forced_choice) flat.push({ section: 'forced_choice', question: q });
    for (const q of questionSet.scenario) flat.push({ section: 'scenario', question: q });
    for (const q of questionSet.situational) flat.push({ section: 'situational', question: q });
    for (const q of questionSet.ranking) flat.push({ section: 'ranking', question: q });
    return flat;
  }, [questionSet]);

  const answeredCount = Object.values(answers).reduce((sum, section) => sum + Object.keys(section).length, 0);

  async function submitNow(finalAnswers) {
    setSubmitting(true);
    setError('');
    try {
      const result = await api.submitAssessment({ lead_id: lead.id, answers: finalAnswers });
      sessionStorage.removeItem('lead');
      navigate(`/results/${result.id}`);
    } catch (err) {
      setError(err.message || 'Something went wrong submitting your assessment. Please try again.');
      setSubmitting(false);
    }
  }

  function recordAnswer(section, questionId, value) {
    const updated = { ...answers, [section]: { ...answers[section], [questionId]: value } };
    setAnswers(updated);
    advance(updated);
  }

  function skipCurrent() {
    advance(answers);
  }

  function advance(currentAnswers) {
    if (index + 1 >= steps.length) {
      submitNow(currentAnswers);
      return;
    }
    setIndex(index + 1);
  }

  function goBack() {
    if (index > 0) setIndex(index - 1);
  }

  function finishNow() {
    submitNow(answers);
  }

  if (loading || submitting) {
    return (
      <div className="container" style={{ paddingTop: 80, textAlign: 'center' }}>
        <p>{submitting ? 'Scoring your results…' : 'Loading…'}</p>
      </div>
    );
  }

  if (error && !steps.length) {
    return (
      <div className="container" style={{ paddingTop: 80, textAlign: 'center' }}>
        <p style={{ color: 'var(--danger)' }}>{error}</p>
      </div>
    );
  }

  const current = steps[index];
  if (!current) return null;

  const progressPct = Math.round(((index + 1) / steps.length) * 100);

  return (
    <div className="container" style={{ paddingTop: 40, paddingBottom: 40, maxWidth: 600 }}>
      <div style={{ marginBottom: 20 }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline' }}>
          <p style={{ fontSize: 12, color: 'var(--ink-soft)', margin: 0 }}>{SECTION_LABELS[current.section]}</p>
          <p style={{ fontSize: 12, color: 'var(--ink-soft)', margin: 0 }}>
            {index + 1} / {steps.length}
          </p>
        </div>
        <div
          style={{
            height: 8,
            borderRadius: 999,
            background: 'var(--milk-panel-alt)',
            overflow: 'hidden',
            marginTop: 8,
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
      </div>

      {current.section === 'likert' && (
        <LikertQuestion
          question={current.question}
          onAnswer={(val) => recordAnswer('likert', current.question.id, val)}
          onSkip={skipCurrent}
        />
      )}
      {(current.section === 'forced_choice' || current.section === 'scenario' || current.section === 'situational') && (
        <ChoiceQuestion
          question={current.question}
          onAnswer={(val) => recordAnswer(current.section, current.question.id, val)}
          onSkip={skipCurrent}
        />
      )}
      {current.section === 'ranking' && (
        <RankingQuestion
          question={current.question}
          onAnswer={(val) => recordAnswer('ranking', current.question.id, val)}
          onSkip={skipCurrent}
        />
      )}

      {error && <p style={{ color: 'var(--danger)', marginTop: 12 }}>{error}</p>}

      <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: 16 }}>
        <div>{index > 0 && <button className="btn btn-outline" onClick={goBack}>← Back</button>}</div>
        {answeredCount > 0 && (
          <button className="btn btn-accent" onClick={finishNow}>
            Finish now & see my results →
          </button>
        )}
      </div>
    </div>
  );
}
