import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { api } from '../api/client';
import { useAuth } from '../api/AuthContext';

const SECTION_LABELS = {
  likert: 'Agree or Disagree',
  forced_choice: 'Pick One',
  scenario: 'Scenario',
  situational: 'Workplace Situation',
  ranking: 'Rank Your Preferences',
};

const LIKERT_SCALE = [
  { value: 1, label: 'Strongly Disagree' },
  { value: 2, label: 'Disagree' },
  { value: 3, label: 'Neutral' },
  { value: 4, label: 'Agree' },
  { value: 5, label: 'Strongly Agree' },
];

const TIME_TARGET_SECONDS = 300; // 5 minutes

function IntakeForm({ schema, values, onChange, onContinue, error }) {
  const allRequiredAnswered = schema.every((field) => !field.required || values[field.key]);

  return (
    <div className="container" style={{ paddingTop: 48, paddingBottom: 40, maxWidth: 560 }}>
      <p className="pill">Before we start</p>
      <h1 style={{ fontSize: 26, marginTop: 12 }}>Tell us a bit about yourself</h1>
      <p>
        This helps us ask the right questions for your background and give you a more accurate result —
        it doesn't judge you, and most fields take one tap.
      </p>

      <div className="card" style={{ padding: 24, marginTop: 16 }}>
        {schema.map((field) => (
          <div key={field.key} style={{ marginBottom: 22 }}>
            <label style={{ marginBottom: 10 }}>
              {field.label}
              {!field.required && <span style={{ fontWeight: 400 }}> (optional)</span>}
            </label>
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8 }}>
              {field.options.map((opt) => {
                const selected = values[field.key] === opt.key;
                return (
                  <button
                    key={opt.key}
                    type="button"
                    className={selected ? 'btn btn-primary' : 'btn btn-outline'}
                    style={{ padding: '10px 16px', fontWeight: 400, fontSize: 14 }}
                    onClick={() => onChange(field.key, opt.key)}
                  >
                    {opt.label}
                  </button>
                );
              })}
            </div>
          </div>
        ))}

        {error && <p style={{ color: 'var(--danger)' }}>{error}</p>}
        <button className="btn btn-primary btn-block" disabled={!allRequiredAnswered} onClick={onContinue}>
          Continue to Assessment →
        </button>
      </div>
    </div>
  );
}

function LikertQuestion({ question, selectedValue, onAnswer, onSkip }) {
  return (
    <div className="card" style={{ padding: 28 }}>
      <h2 style={{ fontSize: 20 }}>{question.text}</h2>
      <div style={{ display: 'flex', gap: 8, marginTop: 20, flexWrap: 'wrap' }}>
        {LIKERT_SCALE.map((opt) => {
          const selected = selectedValue === opt.value;
          return (
            <button
              key={opt.value}
              className={selected ? 'btn btn-primary' : 'btn btn-outline'}
              style={{ flex: '1 1 auto', minWidth: 100, flexDirection: 'column', padding: '14px 10px' }}
              onClick={() => onAnswer(opt.value)}
            >
              <span style={{ fontSize: 20, fontWeight: 700 }}>{opt.value}</span>
              <span style={{ fontSize: 11, color: selected ? 'inherit' : 'var(--ink-soft)' }}>{opt.label}</span>
            </button>
          );
        })}
      </div>
      <button className="btn btn-outline" style={{ marginTop: 16 }} onClick={onSkip}>
        Skip this question
      </button>
    </div>
  );
}

function ChoiceQuestion({ question, selectedKey, onAnswer, onSkip }) {
  return (
    <div className="card" style={{ padding: 28 }}>
      <h2 style={{ fontSize: 20 }}>{question.text}</h2>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 12, marginTop: 20 }}>
        {question.options.map((opt) => {
          const selected = selectedKey === opt.key;
          return (
            <div key={opt.key}>
              <button
                className={selected ? 'btn btn-primary' : 'btn btn-outline'}
                style={{ justifyContent: 'flex-start', textAlign: 'left', fontWeight: 400, padding: '16px 18px', width: '100%' }}
                onClick={() => onAnswer(opt.key)}
              >
                <span style={{ fontWeight: 700, marginRight: 10 }}>{opt.key}.</span>
                {opt.text}
              </button>
              {opt.hint && (
                <p style={{ fontSize: 12, color: 'var(--ink-soft)', fontStyle: 'italic', margin: '4px 0 0 4px' }}>
                  💡 {opt.hint}
                </p>
              )}
            </div>
          );
        })}
      </div>
      <button className="btn btn-outline" style={{ marginTop: 16 }} onClick={onSkip}>
        Skip this question
      </button>
    </div>
  );
}

function RankingQuestion({ question, selectedOrder, onAnswer, onSkip }) {
  const [order, setOrder] = useState(selectedOrder || []);
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
          <div key={item.key}>
            <button
              className="btn btn-outline"
              style={{ justifyContent: 'flex-start', textAlign: 'left', fontWeight: 400, padding: '16px 18px', width: '100%' }}
              onClick={() => pick(item.key)}
            >
              {item.text}
            </button>
            {item.hint && (
              <p style={{ fontSize: 12, color: 'var(--ink-soft)', fontStyle: 'italic', margin: '4px 0 0 4px' }}>
                💡 {item.hint}
              </p>
            )}
          </div>
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

function answerValue(section, entry) {
  if (!entry || entry.skipped) return undefined;
  return entry.value;
}

function buildAnswersFromHistory(history) {
  const answers = { likert: {}, forced_choice: {}, scenario: {}, situational: {}, ranking: {} };
  for (const entry of history) {
    if (entry.skipped) continue;
    answers[entry.section][entry.question.id] = entry.value;
  }
  return answers;
}

function buildSkippedIdsFromHistory(history) {
  return history.filter((e) => e.skipped).map((e) => e.question.id);
}

export default function Assessment() {
  const navigate = useNavigate();
  const { user, loading: authLoading } = useAuth();
  const [lead, setLead] = useState(null);
  const [intakeSchema, setIntakeSchema] = useState(null);
  const [intakeValues, setIntakeValues] = useState({});
  const [intakeError, setIntakeError] = useState('');
  const [stage, setStage] = useState('loading'); // loading | intake | questions | submitting
  const [history, setHistory] = useState([]);
  const [pointer, setPointer] = useState(0);
  const [fetching, setFetching] = useState(false);
  const [startTime, setStartTime] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    if (authLoading) return;

    async function init() {
      if (!user) {
        sessionStorage.removeItem('lead');
        navigate('/signup');
        return;
      }
      const storedLead = sessionStorage.getItem('lead');
      let currentLead;
      if (storedLead) {
        currentLead = JSON.parse(storedLead);
      } else {
        currentLead = await api.createLead({ name: user.name, email: user.email, consent_given: true });
        sessionStorage.setItem('lead', JSON.stringify(currentLead));
      }
      setLead(currentLead);

      const schema = await api.getIntakeSchema();
      setIntakeSchema(schema);
      setStage('intake');
    }

    init().catch(() => setError('Could not load the assessment. Please refresh the page.'));
  }, [navigate, user, authLoading]);

  function handleIntakeChange(key, value) {
    setIntakeValues((prev) => ({ ...prev, [key]: value }));
  }

  async function handleIntakeContinue() {
    setIntakeError('');
    setFetching(true);
    setStartTime(Date.now());
    try {
      const next = await api.getNextQuestion({ intake: intakeValues, answers: {}, skipped_ids: [], elapsed_seconds: 0 });
      if (next.done || !next.next) {
        setIntakeError('Could not start the assessment. Please try again.');
        return;
      }
      setHistory([{ section: next.next.section, question: next.next.question, value: null, skipped: false }]);
      setPointer(0);
      setStage('questions');
    } catch (err) {
      setIntakeError(err.message || 'Could not start the assessment.');
    } finally {
      setFetching(false);
    }
  }

  async function advance(updatedHistory, newPointer) {
    if (newPointer < updatedHistory.length) {
      // Already-fetched question — just move the pointer, no network call.
      setPointer(newPointer);
      return;
    }

    setFetching(true);
    try {
      const elapsedSeconds = (Date.now() - startTime) / 1000;
      const answers = buildAnswersFromHistory(updatedHistory);
      const skipped_ids = buildSkippedIdsFromHistory(updatedHistory);
      const next = await api.getNextQuestion({ intake: intakeValues, answers, skipped_ids, elapsed_seconds });

      if (next.done || !next.next) {
        await finalizeSubmission(answers);
        return;
      }
      setHistory([...updatedHistory, { section: next.next.section, question: next.next.question, value: null, skipped: false }]);
      setPointer(newPointer);
    } catch (err) {
      setError(err.message || 'Something went wrong. Please try again.');
    } finally {
      setFetching(false);
    }
  }

  function recordAnswer(value) {
    const updated = history.map((entry, i) => (i === pointer ? { ...entry, value, skipped: false } : entry));
    setHistory(updated);
    advance(updated, pointer + 1);
  }

  function skipCurrent() {
    const updated = history.map((entry, i) => (i === pointer ? { ...entry, value: null, skipped: true } : entry));
    setHistory(updated);
    advance(updated, pointer + 1);
  }

  function goBack() {
    if (pointer > 0) setPointer(pointer - 1);
  }

  async function finalizeSubmission(answers) {
    setStage('submitting');
    setError('');
    try {
      const result = await api.submitAssessment({ lead_id: lead.id, intake: intakeValues, answers });
      sessionStorage.removeItem('lead');
      navigate(`/results/${result.id}`);
    } catch (err) {
      setError(err.message || 'Something went wrong submitting your assessment. Please try again.');
      setStage('questions');
    }
  }

  function finishNow() {
    finalizeSubmission(buildAnswersFromHistory(history));
  }

  if (stage === 'loading' || (stage === 'intake' && !intakeSchema)) {
    return (
      <div className="container" style={{ paddingTop: 80, textAlign: 'center' }}>
        <p>Loading…</p>
      </div>
    );
  }

  if (error && stage !== 'questions') {
    return (
      <div className="container" style={{ paddingTop: 80, textAlign: 'center' }}>
        <p style={{ color: 'var(--danger)' }}>{error}</p>
      </div>
    );
  }

  if (stage === 'intake') {
    return (
      <IntakeForm
        schema={intakeSchema}
        values={intakeValues}
        onChange={handleIntakeChange}
        onContinue={handleIntakeContinue}
        error={intakeError}
      />
    );
  }

  if (stage === 'submitting' || fetching && history.length === 0) {
    return (
      <div className="container" style={{ paddingTop: 80, textAlign: 'center' }}>
        <p>{stage === 'submitting' ? 'Scoring your results…' : 'Loading…'}</p>
      </div>
    );
  }

  const current = history[pointer];
  if (!current) return null;

  const answeredCount = history.filter((e) => !e.skipped && e.value !== null).length;
  const elapsedSeconds = startTime ? (Date.now() - startTime) / 1000 : 0;
  const progressPct = Math.min(100, Math.round((elapsedSeconds / TIME_TARGET_SECONDS) * 100));

  return (
    <div className="container" style={{ paddingTop: 40, paddingBottom: 40, maxWidth: 600 }}>
      <div style={{ marginBottom: 20 }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline' }}>
          <p style={{ fontSize: 12, color: 'var(--ink-soft)', margin: 0 }}>{SECTION_LABELS[current.section]}</p>
          <p style={{ fontSize: 12, color: 'var(--ink-soft)', margin: 0 }}>Question {pointer + 1} · ~5 min total</p>
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

      {fetching && (
        <div className="card" style={{ padding: 28, textAlign: 'center' }}>
          <p>Loading next question…</p>
        </div>
      )}

      {!fetching && current.section === 'likert' && (
        <LikertQuestion
          key={current.question.id}
          question={current.question}
          selectedValue={answerValue(current.section, current)}
          onAnswer={recordAnswer}
          onSkip={skipCurrent}
        />
      )}
      {!fetching && (current.section === 'forced_choice' || current.section === 'scenario' || current.section === 'situational') && (
        <ChoiceQuestion
          key={current.question.id}
          question={current.question}
          selectedKey={answerValue(current.section, current)}
          onAnswer={recordAnswer}
          onSkip={skipCurrent}
        />
      )}
      {!fetching && current.section === 'ranking' && (
        <RankingQuestion
          key={current.question.id}
          question={current.question}
          selectedOrder={current.skipped ? null : current.value}
          onAnswer={recordAnswer}
          onSkip={skipCurrent}
        />
      )}

      {error && <p style={{ color: 'var(--danger)', marginTop: 12 }}>{error}</p>}

      <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: 16 }}>
        <div>{pointer > 0 && <button className="btn btn-outline" onClick={goBack}>← Back</button>}</div>
        {answeredCount > 0 && (
          <button className="btn btn-accent" onClick={finishNow}>
            Finish now & see my results →
          </button>
        )}
      </div>
    </div>
  );
}
