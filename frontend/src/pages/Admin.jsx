import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { api } from '../api/client';
import { useAuth } from '../api/AuthContext';

export default function Admin() {
  const { user, loading: authLoading } = useAuth();
  const navigate = useNavigate();
  const [leads, setLeads] = useState(null);
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
      .getAdminLeads()
      .then(setLeads)
      .catch(() => setError('Could not load respondents.'));
  }, [authLoading, user, navigate]);

  if (authLoading || (!leads && !error)) {
    return (
      <div className="container" style={{ paddingTop: 60, textAlign: 'center' }}>
        <p>Loading…</p>
      </div>
    );
  }

  return (
    <div className="container" style={{ paddingTop: 48, paddingBottom: 40, maxWidth: 800 }}>
      <p className="pill">Admin</p>
      <h1 style={{ fontSize: 28, marginTop: 12 }}>Respondents</h1>
      <p>{leads ? `${leads.length} ${leads.length === 1 ? 'person has' : 'people have'} taken the assessment.` : ''}</p>

      {error && <p style={{ color: 'var(--danger)' }}>{error}</p>}

      {leads && (
        <div className="card" style={{ overflow: 'hidden', marginTop: 16 }}>
          <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 14 }}>
            <thead>
              <tr style={{ background: 'var(--milk-panel-alt)', textAlign: 'left' }}>
                <th style={{ padding: '12px 16px' }}>Name</th>
                <th style={{ padding: '12px 16px' }}>Email</th>
                <th style={{ padding: '12px 16px' }}>Date</th>
              </tr>
            </thead>
            <tbody>
              {leads.map((lead) => (
                <tr key={lead.id} style={{ borderTop: '1px solid var(--milk-border)' }}>
                  <td style={{ padding: '12px 16px' }}>{lead.name}</td>
                  <td style={{ padding: '12px 16px' }}>{lead.email}</td>
                  <td style={{ padding: '12px 16px' }}>
                    {new Date(lead.created_at).toLocaleDateString(undefined, {
                      year: 'numeric',
                      month: 'short',
                      day: 'numeric',
                    })}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
