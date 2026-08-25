import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { api } from '../api/client';
import { useAuth } from '../api/AuthContext';
import { jsPDF } from 'jspdf';
import 'jspdf-autotable';

export default function Admin() {
  const { user, loading: authLoading } = useAuth();
  const navigate = useNavigate();
  const [results, setResults] = useState(null);
  const [leads, setLeads] = useState(null);
  const [error, setError] = useState('');
  const [activeTab, setActiveTab] = useState('results');
  const [exporting, setExporting] = useState(false);

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
    
    // Load assessment results
    api
      .getAdminAssessmentResults()
      .then(setResults)
      .catch(() => setError('Could not load assessment results.'));
    
    // Load leads
    api
      .getAdminLeads()
      .then(setLeads)
      .catch(() => {});
  }, [authLoading, user, navigate]);

  const exportToCSV = () => {
    if (!results || results.length === 0) {
      alert('No data to export');
      return;
    }

    setExporting(true);
    try {
      // Prepare CSV data
      const headers = ['Name', 'Email', 'Submitted Date', 'Top Recommendation', 'Score', 'Second Recommendation', 'Score'];
      const rows = results.map(item => {
        const top1 = item.recommendations[0];
        const top2 = item.recommendations[1];
        return [
          item.lead_name,
          item.lead_email,
          new Date(item.submitted_at).toLocaleDateString(),
          top1 ? top1.career.name : 'N/A',
          top1 ? top1.score.toFixed(2) : 'N/A',
          top2 ? top2.career.name : 'N/A',
          top2 ? top2.score.toFixed(2) : 'N/A',
        ];
      });

      // Create CSV content
      const csvContent = [
        headers.join(','),
        ...rows.map(row => row.map(cell => `"${cell}"`).join(',')),
      ].join('\n');

      // Download CSV
      const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
      const link = document.createElement('a');
      const url = URL.createObjectURL(blob);
      link.setAttribute('href', url);
      link.setAttribute('download', `assessment-results-${new Date().toISOString().split('T')[0]}.csv`);
      link.style.visibility = 'hidden';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    } catch (err) {
      alert('Error exporting CSV: ' + err.message);
    } finally {
      setExporting(false);
    }
  };

  const exportToPDF = () => {
    if (!results || results.length === 0) {
      alert('No data to export');
      return;
    }

    setExporting(true);
    try {
      const doc = new jsPDF();
      const pageWidth = doc.internal.pageSize.getWidth();
      const pageHeight = doc.internal.pageSize.getHeight();

      // Title
      doc.setFontSize(20);
      doc.text('Assessment Results Report', pageWidth / 2, 20, { align: 'center' });

      // Generated date
      doc.setFontSize(10);
      doc.setTextColor(100);
      doc.text(`Generated: ${new Date().toLocaleDateString()}`, pageWidth / 2, 27, { align: 'center' });

      // Reset text color
      doc.setTextColor(0);

      // Prepare table data
      const tableData = results.map(item => {
        const top1 = item.recommendations[0];
        const top2 = item.recommendations[1];
        return [
          item.lead_name,
          item.lead_email,
          new Date(item.submitted_at).toLocaleDateString(),
          top1 ? top1.career.name : 'N/A',
          top1 ? top1.score.toFixed(2) : 'N/A',
          top2 ? top2.career.name : 'N/A',
          top2 ? top2.score.toFixed(2) : 'N/A',
        ];
      });

      doc.autoTable({
        startY: 35,
        head: [['Name', 'Email', 'Date', 'Top Recommendation', 'Score', '2nd Recommendation', 'Score']],
        body: tableData,
        margin: { top: 35, right: 10, bottom: 10, left: 10 },
        styles: {
          fontSize: 9,
          cellPadding: 3,
        },
        headStyles: {
          backgroundColor: [41, 128, 185],
          textColor: 255,
          fontStyle: 'bold',
        },
        alternateRowStyles: {
          backgroundColor: [245, 245, 245],
        },
      });

      // Add summary
      const yPosition = doc.lastAutoTable.finalY + 15;
      doc.setFontSize(12);
      doc.text(`Total Respondents: ${results.length}`, 15, yPosition);

      // Save PDF
      doc.save(`assessment-results-${new Date().toISOString().split('T')[0]}.pdf`);
    } catch (err) {
      alert('Error exporting PDF: ' + err.message);
    } finally {
      setExporting(false);
    }
  };

  if (authLoading || (!results && !leads && !error)) {
    return (
      <div className="container" style={{ paddingTop: 60, textAlign: 'center' }}>
        <p>Loading…</p>
      </div>
    );
  }

  return (
    <div className="container" style={{ paddingTop: 48, paddingBottom: 40, maxWidth: 1200 }}>
      <p className="pill">Admin</p>
      <h1 style={{ fontSize: 28, marginTop: 12 }}>Admin Dashboard</h1>

      {error && <p style={{ color: 'var(--danger)' }}>{error}</p>}

      {/* Tab Navigation */}
      <div style={{ display: 'flex', gap: 16, marginTop: 24, marginBottom: 24, borderBottom: '1px solid var(--milk-border)' }}>
        <button
          onClick={() => setActiveTab('results')}
          style={{
            padding: '12px 0',
            border: 'none',
            background: 'none',
            cursor: 'pointer',
            fontSize: 16,
            fontWeight: activeTab === 'results' ? 600 : 400,
            color: activeTab === 'results' ? 'var(--brand)' : 'var(--text-secondary)',
            borderBottom: activeTab === 'results' ? '3px solid var(--brand)' : 'none',
          }}
        >
          Assessment Results
        </button>
        <button
          onClick={() => setActiveTab('leads')}
          style={{
            padding: '12px 0',
            border: 'none',
            background: 'none',
            cursor: 'pointer',
            fontSize: 16,
            fontWeight: activeTab === 'leads' ? 600 : 400,
            color: activeTab === 'leads' ? 'var(--brand)' : 'var(--text-secondary)',
            borderBottom: activeTab === 'leads' ? '3px solid var(--brand)' : 'none',
          }}
        >
          All Respondents
        </button>
      </div>

      {/* Assessment Results Tab */}
      {activeTab === 'results' && (
        <>
          <div style={{ display: 'flex', gap: 12, marginBottom: 20, alignItems: 'center' }}>
            <p>{results ? `${results.length} ${results.length === 1 ? 'person has' : 'people have'} submitted their assessment.` : 'Loading...'}</p>
            {results && results.length > 0 && (
              <>
                <button
                  onClick={exportToCSV}
                  disabled={exporting}
                  style={{
                    padding: '8px 16px',
                    background: 'var(--brand)',
                    color: 'white',
                    border: 'none',
                    borderRadius: 4,
                    cursor: exporting ? 'not-allowed' : 'pointer',
                    fontSize: 14,
                    fontWeight: 600,
                    opacity: exporting ? 0.6 : 1,
                  }}
                >
                  📥 Export CSV
                </button>
                <button
                  onClick={exportToPDF}
                  disabled={exporting}
                  style={{
                    padding: '8px 16px',
                    background: 'var(--success)',
                    color: 'white',
                    border: 'none',
                    borderRadius: 4,
                    cursor: exporting ? 'not-allowed' : 'pointer',
                    fontSize: 14,
                    fontWeight: 600,
                    opacity: exporting ? 0.6 : 1,
                  }}
                >
                  📄 Export PDF
                </button>
              </>
            )}
          </div>

          {results && (
            <div className="card" style={{ overflow: 'hidden' }}>
              <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 14 }}>
                <thead>
                  <tr style={{ background: 'var(--milk-panel-alt)', textAlign: 'left' }}>
                    <th style={{ padding: '12px 16px' }}>Name</th>
                    <th style={{ padding: '12px 16px' }}>Email</th>
                    <th style={{ padding: '12px 16px' }}>Submitted</th>
                    <th style={{ padding: '12px 16px' }}>Top Recommendation</th>
                    <th style={{ padding: '12px 16px' }}>Score</th>
                    <th style={{ padding: '12px 16px' }}>2nd Recommendation</th>
                  </tr>
                </thead>
                <tbody>
                  {results.map((item) => (
                    <tr key={item.result_id} style={{ borderTop: '1px solid var(--milk-border)' }}>
                      <td style={{ padding: '12px 16px' }}>{item.lead_name}</td>
                      <td style={{ padding: '12px 16px' }}>{item.lead_email}</td>
                      <td style={{ padding: '12px 16px' }}>
                        {new Date(item.submitted_at).toLocaleDateString(undefined, {
                          year: 'numeric',
                          month: 'short',
                          day: 'numeric',
                        })}
                      </td>
                      <td style={{ padding: '12px 16px' }}>
                        {item.recommendations[0] ? (
                          <>
                            <strong>{item.recommendations[0].career.name}</strong>
                            <br />
                            <small style={{ color: 'var(--text-secondary)' }}>
                              {item.recommendations[0].career.duration}
                            </small>
                          </>
                        ) : (
                          'N/A'
                        )}
                      </td>
                      <td style={{ padding: '12px 16px' }}>
                        {item.recommendations[0] ? item.recommendations[0].score.toFixed(2) : 'N/A'}
                      </td>
                      <td style={{ padding: '12px 16px' }}>
                        {item.recommendations[1] ? (
                          <>
                            <strong>{item.recommendations[1].career.name}</strong>
                            <br />
                            <small style={{ color: 'var(--text-secondary)' }}>
                              {item.recommendations[1].career.duration}
                            </small>
                          </>
                        ) : (
                          'N/A'
                        )}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </>
      )}

      {/* Respondents Tab */}
      {activeTab === 'leads' && (
        <>
          <p>{leads ? `${leads.length} ${leads.length === 1 ? 'person has' : 'people have'} registered.` : ''}</p>
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
        </>
      )}
    </div>
  );
}
