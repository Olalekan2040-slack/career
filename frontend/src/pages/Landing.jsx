import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { api } from '../api/client';
import { useAuth } from '../api/AuthContext';

const DIFFERENTIATORS = [
  {
    title: 'A real psychometric instrument',
    body: 'Not a personality quiz. We measure stable underlying traits first, then map them onto careers — the standard approach used in professional aptitude testing.',
  },
  {
    title: 'Transparent, not a black box',
    body: 'Every recommendation names the exact strengths that drove it, so you can see the reasoning behind your result, not just trust it.',
  },
  {
    title: 'Built for the whole industry',
    body: 'Engineering, data, design, marketing, product, and operations — spanning technical and non-technical paths alike.',
  },
];

export default function Landing() {
  const navigate = useNavigate();
  const { user } = useAuth();
  const [meta, setMeta] = useState(null);

  useEffect(() => {
    api.getMeta().then(setMeta).catch(() => {});
  }, []);

  const careerCount = meta?.career_count ?? 69;
  const competencyCount = meta?.competency_count ?? 24;

  function handleStart() {
    navigate(user ? '/assessment' : '/signup');
  }

  return (
    <div className="container" style={{ paddingTop: 64, paddingBottom: 56 }}>
      {/* Hero */}
      <div style={{ textAlign: 'center', maxWidth: 640, margin: '0 auto' }}>
        <p className="pill">Global · Evidence-Based Career Assessment</p>
        <h1 style={{ fontSize: 44, marginTop: 16, lineHeight: 1.15 }}>
          Discover the digital career built for your strengths
        </h1>
        <p style={{ fontSize: 18 }}>
          A professional psychometric assessment that maps your real strengths onto {careerCount} digital
          careers — with the reasoning behind every recommendation, and a full course outline to start.
        </p>
        <button className="btn btn-primary" style={{ marginTop: 20, padding: '16px 32px', fontSize: 16 }} onClick={handleStart}>
          Get Started Free →
        </button>
        <p style={{ fontSize: 13, marginTop: 14 }}>Free account required · Takes about 10 minutes</p>
      </div>

      {/* Stat bar */}
      <div
        className="card"
        style={{
          display: 'flex',
          justifyContent: 'center',
          gap: 40,
          padding: '24px 32px',
          marginTop: 40,
          flexWrap: 'wrap',
          textAlign: 'center',
        }}
      >
        {[
          { value: careerCount, label: 'Careers Mapped' },
          { value: competencyCount, label: 'Competencies Measured' },
          { value: '5', label: 'Question Formats' },
        ].map((stat) => (
          <div key={stat.label}>
            <p style={{ margin: 0, fontSize: 28, fontWeight: 700, color: 'var(--accent-dark)' }}>{stat.value}</p>
            <p style={{ margin: 0, fontSize: 13, color: 'var(--ink-soft)' }}>{stat.label}</p>
          </div>
        ))}
      </div>

      {/* How it works */}
      <div className="grid-responsive-3" style={{ marginTop: 24 }}>
        {[
          { step: '01', title: 'Create your free account', body: 'One minute — name, email, and password. Your results are saved to your personal dashboard.' },
          { step: '02', title: 'Take the assessment', body: 'A focused, randomised set of questions. Skip anything that doesn’t apply, finish whenever you’re ready.' },
          { step: '03', title: 'See your ranked matches', body: 'Your top career matches, each with the reasons why and a full course outline to get started.' },
        ].map((item) => (
          <div key={item.step} className="card" style={{ padding: 24 }}>
            <p style={{ fontSize: 13, fontWeight: 700, color: 'var(--accent)', letterSpacing: 1 }}>{item.step}</p>
            <h3 style={{ marginTop: 8, fontSize: 18 }}>{item.title}</h3>
            <p style={{ fontSize: 14 }}>{item.body}</p>
          </div>
        ))}
      </div>

      {/* Why it's different */}
      <div className="grid-responsive-3" style={{ marginTop: 24 }}>
        {DIFFERENTIATORS.map((item) => (
          <div key={item.title} className="card" style={{ padding: 24 }}>
            <h3 style={{ fontSize: 17 }}>{item.title}</h3>
            <p style={{ fontSize: 14 }}>{item.body}</p>
          </div>
        ))}
      </div>

      {/* Final CTA */}
      <div className="card" style={{ padding: 32, marginTop: 24, textAlign: 'center' }}>
        <h2 style={{ fontSize: 24 }}>Make your next career move an evidence-based one</h2>
        <button className="btn btn-accent" style={{ marginTop: 12, padding: '16px 32px', fontSize: 16 }} onClick={handleStart}>
          Get Started Free →
        </button>
      </div>
    </div>
  );
}
