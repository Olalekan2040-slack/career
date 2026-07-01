import { useEffect } from 'react';
import { api } from './client';

const PING_INTERVAL_MS = 4 * 60 * 1000; // 4 minutes — under Render's ~5 minute idle timeout

/**
 * Pings the backend periodically while this tab is open, so Render's free-tier
 * instance doesn't spin down between requests during an active visit.
 * This only helps while someone has the site open — it does not keep the
 * backend warm when there are no visitors at all (see the GitHub Actions
 * cron ping for that).
 */
export function useKeepAlive() {
  useEffect(() => {
    api.ping();
    const interval = setInterval(() => {
      api.ping();
    }, PING_INTERVAL_MS);
    return () => clearInterval(interval);
  }, []);
}
