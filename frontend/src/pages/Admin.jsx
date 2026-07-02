import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { api } from '../api/client';
import { useAuth } from '../api/AuthContext';

export default function Admin() {
  const { user, loading: authLoading } = useAuth();
  const navigate = useNavigate();
  const [users, setUsers] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    if (authLoading) return;
    if (!user) {
      navigate('/login');
      return;
    }
    if (!user.is_admin) {
      navigate('/');
      return;
    }
    api
      .getAdminUsers()
      .then(setUsers)
      .catch(() => setError('Could not load registered users.'));
  }, [authLoading, user, navigate]);

  if (authLoading || (!users && !error)) {
    return (
      <div className="container" style={{ paddingTop: 60, textAlign: 'center' }}>
        <p>Loading…</p>
      </div>
    );
  }

  return (
    <div className="container" style={{ paddingTop: 48, paddingBottom: 40, maxWidth: 800 }}>
      <p className="pill">Admin</p>
      <h1 style={{ fontSize: 28, marginTop: 12 }}>Registered users</h1>
      <p>{users ? `${users.length} account${users.length === 1 ? '' : 's'} registered.` : ''}</p>

      {error && <p style={{ color: 'var(--danger)' }}>{error}</p>}

      {users && (
        <div className="card" style={{ overflow: 'hidden', marginTop: 16 }}>
          <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 14 }}>
            <thead>
              <tr style={{ background: 'var(--milk-panel-alt)', textAlign: 'left' }}>
                <th style={{ padding: '12px 16px' }}>Name</th>
                <th style={{ padding: '12px 16px' }}>Email</th>
                <th style={{ padding: '12px 16px' }}>Joined</th>
                <th style={{ padding: '12px 16px' }}>Role</th>
              </tr>
            </thead>
            <tbody>
              {users.map((u) => (
                <tr key={u.id} style={{ borderTop: '1px solid var(--milk-border)' }}>
                  <td style={{ padding: '12px 16px' }}>{u.name}</td>
                  <td style={{ padding: '12px 16px' }}>{u.email}</td>
                  <td style={{ padding: '12px 16px' }}>
                    {new Date(u.created_at).toLocaleDateString(undefined, {
                      year: 'numeric',
                      month: 'short',
                      day: 'numeric',
                    })}
                  </td>
                  <td style={{ padding: '12px 16px' }}>{u.is_admin ? 'Admin' : 'User'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
