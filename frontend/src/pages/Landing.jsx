import { useNavigate } from 'react-router-dom';

const SAMPLE_CAREERS = [
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

  return (
    <div className="container" style={{ paddingTop: 56, paddingBottom: 40 }}>
      <div style={{ textAlign: 'center', maxWidth: 640, margin: '0 auto' }}>
        <p className="pill">Free · No signup required · ~20 minutes</p>
        <h1 style={{ fontSize: 40, marginTop: 16 }}>
          Wherever you are, find your digital career path
        </h1>
        <p style={{ fontSize: 17 }}>
          A psychometric assessment across 24 traits maps your real strengths onto 69 digital careers —
          with the reasons behind every recommendation, not just a label.
        </p>
        <button className="btn btn-primary" style={{ marginTop: 20 }} onClick={() => navigate('/start')}>
          Start Free Assessment →
        </button>
        <p style={{ fontSize: 13, marginTop: 14 }}>
          Get your top 2 matches free. Create a free account (or unlock for $1) to see your top 4 —
          each with the reasons why and a full course outline.
        </p>
      </div>

      <div className="card" style={{ padding: 28, marginTop: 48 }}>
        <p className="pill">69 careers, 5 question types</p>
        <h3 style={{ marginTop: 10 }}>A real psychometric assessment, not a quiz</h3>
        <p>
          88 questions across five formats — agree/disagree statements, forced choices, workplace scenarios,
          situational judgment, and preference ranking — measuring 24 underlying traits like Systems Thinking,
          Creativity, and Business Thinking. You don't have to answer every question; finish whenever you're ready.
        </p>
        <ul style={{ paddingLeft: 18, color: 'var(--ink-soft)', fontSize: 14, columns: 2 }}>
          {SAMPLE_CAREERS.map((t) => (
            <li key={t}>{t}</li>
          ))}
          <li>…and 61 more</li>
        </ul>
      </div>

      <div className="card" style={{ padding: 28, marginTop: 24, textAlign: 'center' }}>
        <h3>Every recommendation comes with a reason and a course outline</h3>
        <p>
          No black-box scoring — see exactly which of your strengths drove each match, plus a real 4-phase
          curriculum and hand-picked resources to get started.
        </p>
        <button className="btn btn-accent" onClick={() => navigate('/start')}>
          Take the Assessment →
        </button>
      </div>
    </div>
  );
}
