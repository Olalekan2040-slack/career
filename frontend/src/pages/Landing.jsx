import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { api } from '../api/client';

const QUESTION_FORMATS = [
  {
    key: 'likert',
    name: 'Likert Agreement',
    description: 'Rate statements about your habits and preferences on a 1-5 agreement scale.',
  },
  {
    key: 'forced_choice',
    name: 'Forced Choice',
    description: 'Pick between two contrasting activities to reveal genuine preference, not social desirability.',
  },
  {
    key: 'scenario',
    name: 'Scenario-Based',
    description: 'React to realistic workplace situations the way you naturally would.',
  },
  {
    key: 'situational',
    name: 'Situational Judgment',
    description: 'Choose your instinct in workplace dilemmas — every option is descriptive, not right or wrong.',
  },
  {
    key: 'ranking',
    name: 'Preference Ranking',
    description: 'Order competing priorities from most to least appealing to reveal relative strength of preference.',
  },
];

const SESSION_LENGTH = 20;

const FALLBACK_CAREERS = [
  'Frontend Web Development',
  'Data Science',
  'UI/UX Design',
  'Cybersecurity',
  'Digital Marketing',
  'Product Management',
  'AI Agent Development',
  'Video Editing',
];

export default function Landing() {
  const navigate = useNavigate();
  const [meta, setMeta] = useState(null);

  useEffect(() => {
    api.getMeta().then(setMeta).catch(() => {});
  }, []);

  const careerCount = meta?.career_count ?? 69;
  const competencyCount = meta?.competency_count ?? 24;
  const totalQuestions = meta?.question_counts?.total ?? 88;
  const sampleCareers = (meta?.careers ?? FALLBACK_CAREERS).slice(0, 8);
  const extraCareerCount = careerCount - sampleCareers.length;

  return (
    <div className="container" style={{ paddingTop: 56, paddingBottom: 56 }}>
      {/* Hero */}
      <div style={{ textAlign: 'center', maxWidth: 700, margin: '0 auto' }}>
        <p className="pill">Global · Evidence-Based Career Assessment</p>
        <h1 style={{ fontSize: 42, marginTop: 16, lineHeight: 1.15 }}>
          Discover the digital career built for your strengths
        </h1>
        <p style={{ fontSize: 18 }}>
          A professional-grade psychometric instrument — a validated {totalQuestions}-item bank across five formats,
          measuring {competencyCount} underlying competencies — mapped onto {careerCount} digital careers spanning
          engineering, data, design, marketing, product, and operations. Each session draws a focused set of around
          {' '}{SESSION_LENGTH} questions, randomised so every attempt stays fresh. Used by career switchers and
          professionals worldwide to make an evidence-based next move, not a guess.
        </p>
        <button className="btn btn-primary" style={{ marginTop: 20, padding: '16px 32px', fontSize: 16 }} onClick={() => navigate('/start')}>
          Start Free Assessment →
        </button>
        <p style={{ fontSize: 13, marginTop: 14 }}>
          No signup required to begin · Get your top 2 matches free · Create a free account or unlock for $1 to see your top 4
        </p>
      </div>

      {/* How it works */}
      <div className="grid-responsive-3" style={{ marginTop: 56 }}>
        {[
          { step: '01', title: 'Answer at your pace', body: `Work through a focused, randomised session of around ${SESSION_LENGTH} questions. Skip anything that doesn't apply — finish whenever you're ready.` },
          { step: '02', title: 'Get scored across 24 competencies', body: 'Your responses are normalized into a competency profile, not a single arbitrary score.' },
          { step: '03', title: 'See ranked matches with reasons', body: `Your profile is matched against all ${careerCount} careers. Every recommendation names exactly which strengths drove it.` },
        ].map((item) => (
          <div key={item.step} className="card" style={{ padding: 24 }}>
            <p style={{ fontSize: 13, fontWeight: 700, color: 'var(--accent)', letterSpacing: 1 }}>{item.step}</p>
            <h3 style={{ marginTop: 8, fontSize: 18 }}>{item.title}</h3>
            <p style={{ fontSize: 14 }}>{item.body}</p>
          </div>
        ))}
      </div>

      {/* Methodology */}
      <div className="card" style={{ padding: 32, marginTop: 24 }}>
        <p className="pill">The Methodology</p>
        <h2 style={{ marginTop: 12, fontSize: 26 }}>A real psychometric instrument, not a personality quiz</h2>
        <p style={{ fontSize: 15, maxWidth: 760 }}>
          Most "career quizzes" score a handful of questions directly against a job title. This assessment
          follows the standard psychometric approach used in professional aptitude testing: measure a person's
          stable underlying traits first, independent of any specific career, then map those traits onto the wider
          career space afterward. That separation is what makes the result defensible — your competency profile
          would look the same regardless of which careers happen to be in the taxonomy this year.
        </p>

        <p style={{ fontWeight: 700, fontSize: 13, textTransform: 'uppercase', letterSpacing: 0.5, color: 'var(--accent-dark)', marginTop: 24 }}>
          Five question formats, {totalQuestions} items in the full bank
        </p>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 16, marginTop: 12 }}>
          {QUESTION_FORMATS.map((format) => (
            <div key={format.key} style={{ padding: 16, background: 'var(--milk-panel)', borderRadius: 10 }}>
              <p style={{ margin: 0, fontWeight: 700, fontSize: 14 }}>
                {format.name}
                {meta?.question_counts && (
                  <span style={{ color: 'var(--accent-dark)', fontWeight: 400 }}> · {meta.question_counts[format.key]} items</span>
                )}
              </p>
              <p style={{ margin: '6px 0 0 0', fontSize: 13, color: 'var(--ink-soft)' }}>{format.description}</p>
            </div>
          ))}
        </div>

        <p style={{ fontWeight: 700, fontSize: 13, textTransform: 'uppercase', letterSpacing: 0.5, color: 'var(--accent-dark)', marginTop: 24 }}>
          {competencyCount} competencies measured
        </p>
        <p style={{ fontSize: 14 }}>
          Including Logical Reasoning, Systems Thinking, Creativity, Business Thinking, Empathy, Risk Tolerance,
          Communication, and Leadership — each scored from multiple independent questions across different formats,
          so no single answer can distort your profile.
        </p>

        <p style={{ fontWeight: 700, fontSize: 13, textTransform: 'uppercase', letterSpacing: 0.5, color: 'var(--accent-dark)', marginTop: 24 }}>
          Transparent scoring, not a black box
        </p>
        <p style={{ fontSize: 14 }}>
          Every recommendation you receive names the specific competencies that drove it — "Your strengths in
          Systems Thinking and Technical Curiosity closely match this career" — so you can see the reasoning,
          not just trust it.
        </p>
      </div>

      {/* Careers */}
      <div className="card" style={{ padding: 32, marginTop: 24 }}>
        <p className="pill">{careerCount} Career Paths</p>
        <h2 style={{ marginTop: 12, fontSize: 26 }}>Every digital discipline, not just "developer"</h2>
        <p style={{ fontSize: 15 }}>
          From engineering and data to design, marketing, product, and operations — spanning both technical and
          non-technical paths, so the result fits people who love writing code and people who never want to.
        </p>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8, marginTop: 16 }}>
          {sampleCareers.map((c) => (
            <span key={c} className="pill" style={{ background: 'var(--milk-panel-alt)' }}>
              {c}
            </span>
          ))}
          {extraCareerCount > 0 && (
            <span className="pill" style={{ background: 'var(--milk-panel-alt)' }}>+{extraCareerCount} more</span>
          )}
        </div>
      </div>

      {/* Tiers */}
      <div className="grid-responsive-2" style={{ marginTop: 24 }}>
        <div className="card" style={{ padding: 24 }}>
          <p className="pill">Free</p>
          <h3 style={{ marginTop: 10 }}>Top 2 matches</h3>
          <p>Complete the assessment with no signup and get your top 2 recommended careers, each with its full
            reasoning and a complete course outline.</p>
        </div>
        <div className="card" style={{ padding: 24 }}>
          <p className="pill">Free account or $1</p>
          <h3 style={{ marginTop: 10 }}>Top 4 matches</h3>
          <p>Create a free account to unlock your top 4 matches and a personal dashboard — or unlock the same top
            4 for $1 without signing up.</p>
        </div>
      </div>

      {/* Final CTA */}
      <div className="card" style={{ padding: 32, marginTop: 24, textAlign: 'center' }}>
        <h2 style={{ fontSize: 24 }}>Make your next career move an evidence-based one</h2>
        <p style={{ fontSize: 15, maxWidth: 560, margin: '0 auto' }}>
          ~{SESSION_LENGTH} questions per session. {competencyCount} competencies. {careerCount} careers. One clear,
          reasoned recommendation.
        </p>
        <button className="btn btn-accent" style={{ marginTop: 12, padding: '16px 32px', fontSize: 16 }} onClick={() => navigate('/start')}>
          Take the Assessment →
        </button>
      </div>
    </div>
  );
}
