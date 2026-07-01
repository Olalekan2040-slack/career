import { useNavigate } from 'react-router-dom';

const TRACK_A_SAMPLE = ['Frontend Development', 'Backend Development', 'Cybersecurity', 'AI / Machine Learning', 'Mobile App Dev'];
const TRACK_B_SAMPLE = ['UI/UX Design', 'Digital Marketing', 'Virtual Assistance', 'Graphic Design', 'Video Editing'];

export default function Landing() {
  const navigate = useNavigate();

  return (
    <div className="container" style={{ paddingTop: 56, paddingBottom: 40 }}>
      <div style={{ textAlign: 'center', maxWidth: 640, margin: '0 auto' }}>
        <p className="pill">Free · No signup · 10 minutes</p>
        <h1 style={{ fontSize: 40, marginTop: 16 }}>
          Wherever you are, find your digital career path
        </h1>
        <p style={{ fontSize: 17 }}>
          Take a quick assessment and instantly get matched to the digital career that fits your real
          strengths — whether that means writing code, or not.
        </p>
        <button className="btn btn-primary" style={{ marginTop: 20 }} onClick={() => navigate('/start')}>
          Start Free Assessment →
        </button>
        <p style={{ fontSize: 13, marginTop: 14 }}>
          Your top match is free. Unlock your full curriculum + resources for both matches for just{' '}
          <strong style={{ color: 'var(--ink)' }}>$1 USD</strong>.
        </p>
      </div>

      <div
        style={{
          display: 'grid',
          gridTemplateColumns: '1fr 1fr',
          gap: 20,
          marginTop: 48,
        }}
      >
        <div className="card" style={{ padding: 24 }}>
          <p className="pill">Track A</p>
          <h3 style={{ marginTop: 10 }}>Code-Based Paths</h3>
          <p>For people who want to build with logic and code — 11 categories.</p>
          <ul style={{ paddingLeft: 18, color: 'var(--ink-soft)', fontSize: 14 }}>
            {TRACK_A_SAMPLE.map((t) => (
              <li key={t}>{t}</li>
            ))}
            <li>…and 6 more</li>
          </ul>
        </div>
        <div className="card" style={{ padding: 24 }}>
          <p className="pill">Track B</p>
          <h3 style={{ marginTop: 10 }}>Non-Coding Digital Paths</h3>
          <p>For people who'd rather build with people, visuals, or words — 13 categories.</p>
          <ul style={{ paddingLeft: 18, color: 'var(--ink-soft)', fontSize: 14 }}>
            {TRACK_B_SAMPLE.map((t) => (
              <li key={t}>{t}</li>
            ))}
            <li>…and 8 more</li>
          </ul>
        </div>
      </div>

      <div className="card" style={{ padding: 28, marginTop: 24, textAlign: 'center' }}>
        <h3>Whether you love code or not, there's a path for you</h3>
        <p>
          24 digital career categories, one 10-minute assessment, and a real 4-phase curriculum with
          hand-picked resources to get you started.
        </p>
        <button className="btn btn-accent" onClick={() => navigate('/start')}>
          Take the Assessment →
        </button>
      </div>
    </div>
  );
}
