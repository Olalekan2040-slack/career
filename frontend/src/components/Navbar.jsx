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
        <nav style={{ display: 'flex', alignItems: 'center', gap: 16, fontSize: 14 }}>
          {!loading && user && (
            <>
              <Link to="/dashboard" style={{ color: 'var(--ink)', textDecoration: 'none', fontWeight: 600 }}>
                Dashboard
              </Link>
              {user.is_admin && (
                <Link to="/admin" style={{ color: 'var(--ink)', textDecoration: 'none', fontWeight: 600 }}>
                  Admin
                </Link>
              )}
              <span style={{ color: 'var(--ink-soft)' }}>Hi, {user.name.split(' ')[0]}</span>
              <button className="btn btn-outline" onClick={handleLogout} style={{ padding: '8px 16px' }}>
                Log out
              </button>
            </>
          )}
          {!loading && !user && (
            <>
              <Link to="/login" style={{ color: 'var(--ink)', textDecoration: 'none', fontWeight: 600 }}>
                Log in
              </Link>
              <Link to="/signup" className="btn btn-primary" style={{ padding: '8px 16px', textDecoration: 'none' }}>
                Sign up free
              </Link>
            </>
          )}
        </nav>
      </div>
    </header>
  );
}
