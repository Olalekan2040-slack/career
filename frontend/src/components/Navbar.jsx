import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../api/AuthContext';

export default function Navbar() {
  const { user, logout, loading } = useAuth();
  const navigate = useNavigate();

  function handleLogout() {
    logout();
    navigate('/');
  }

  return (
    <header
      style={{
        borderBottom: '1px solid var(--milk-border)',
        background: 'var(--milk-bg)',
        position: 'sticky',
        top: 0,
        zIndex: 10,
      }}
    >
      <div
        className="container"
        style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', height: 64 }}
      >
        <Link to="/" style={{ fontWeight: 700, fontSize: 16, color: 'var(--ink)', textDecoration: 'none' }}>
          Digital Skills Assessment
        </Link>
        {/* No public sign up/log in — everyone just takes the assessment via name+email.
            This nav slot only ever shows anything for an already-logged-in admin session. */}
        {!loading && user && user.is_admin && (
          <nav style={{ display: 'flex', alignItems: 'center', gap: 16, fontSize: 14 }}>
            <Link to="/admin" style={{ color: 'var(--ink)', textDecoration: 'none', fontWeight: 600 }}>
              Admin
            </Link>
            <button className="btn btn-outline" onClick={handleLogout} style={{ padding: '8px 16px' }}>
              Log out
            </button>
          </nav>
        )}
      </div>
    </header>
  );
}
