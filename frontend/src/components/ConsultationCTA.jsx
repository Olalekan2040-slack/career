import { useState } from 'react';
import { api } from '../api/client';

export default function ConsultationCTA({ leadId }) {
  const [open, setOpen] = useState(false);
  const [preferredTime, setPreferredTime] = useState('');
  const [note, setNote] = useState('');
  const [status, setStatus] = useState('idle'); // idle | sending | sent | error

  async function handleSubmit(e) {
    e.preventDefault();
    setStatus('sending');
    try {
      await api.bookConsultation({ lead_id: leadId, preferred_time: preferredTime, note });
      setStatus('sent');
    } catch {
      setStatus('error');
    }
  }

  return (
    <div className="card" style={{ padding: 24, marginTop: 24 }}>
      <p className="pill">Free, no strings attached</p>
      <h3 style={{ marginTop: 10 }}>Book a free consultation with Sharafdeen</h3>
      <p>
        Whether you unlocked your full result or not, you can always book a short call to talk through
        your path and next steps.
      </p>
      {!open && status !== 'sent' && (
        <button className="btn btn-outline" onClick={() => setOpen(true)}>
          Book a consultation
        </button>
      )}
      {open && status !== 'sent' && (
        <form onSubmit={handleSubmit} style={{ marginTop: 16 }}>
          <label htmlFor="preferred_time">Preferred time (optional)</label>
          <input
            id="preferred_time"
            type="text"
            placeholder="e.g. Weekday evenings, GMT+1"
            value={preferredTime}
            onChange={(e) => setPreferredTime(e.target.value)}
            style={{ marginBottom: 12 }}
          />
          <label htmlFor="note">What would you like to talk about? (optional)</label>
          <textarea
            id="note"
            rows={3}
            value={note}
            onChange={(e) => setNote(e.target.value)}
            style={{ marginBottom: 12 }}
          />
          <button className="btn btn-primary" type="submit" disabled={status === 'sending'}>
            {status === 'sending' ? 'Submitting…' : 'Request consultation'}
          </button>
          {status === 'error' && (
            <p style={{ color: 'var(--danger)', marginTop: 8 }}>
              Something went wrong — please try again.
            </p>
          )}
        </form>
      )}
      {status === 'sent' && (
        <p style={{ color: 'var(--success)', fontWeight: 600 }}>
          Thanks! Sharafdeen will reach out to schedule your call.
        </p>
      )}
    </div>
  );
}
