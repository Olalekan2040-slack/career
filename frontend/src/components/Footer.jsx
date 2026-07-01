import profilePhoto from '../assets/profile.jpg';

export default function Footer() {
  return (
    <footer
      style={{
        background: 'var(--milk-panel)',
        borderTop: '1px solid var(--milk-border)',
        padding: '32px 20px',
        marginTop: 48,
      }}
    >
      <div className="container" style={{ textAlign: 'center' }}>
        <img
          src={profilePhoto}
          alt="Sharafdeen Quadri Olalekan"
          style={{
            width: 72,
            height: 72,
            borderRadius: '50%',
            objectFit: 'cover',
            border: '2px solid var(--milk-border)',
            marginBottom: 10,
          }}
        />
        <p style={{ margin: 0, fontSize: 13, color: 'var(--ink-soft)' }}>Built with care by</p>
        <p style={{ margin: '4px 0', fontSize: 16, fontWeight: 700, color: 'var(--ink)' }}>
          Sharafdeen Quadri Olalekan
        </p>
        <p style={{ margin: 0, fontSize: 13 }}>
          <a href="https://quaddev.onrender.com/" target="_blank" rel="noreferrer">
            quaddev.onrender.com
          </a>
        </p>
        <p style={{ margin: '16px 0 0 0', fontSize: 12, color: 'var(--ink-soft)' }}>
          © {new Date().getFullYear()} Global Digital Skills Career Assessment. All rights reserved.
        </p>
      </div>
    </footer>
  );
}
