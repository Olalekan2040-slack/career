# Global Digital Skills Career Assessment Platform

A free career assessment — no signup required to take it — that maps a
person's real strengths onto 69 digital careers using a genuine psychometric
instrument: 88 questions across 5 formats (Likert agreement, forced-choice,
scenario-based, situational judgment, and preference ranking), scoring 24
underlying competencies which are then projected onto the career space.
Anyone can answer as few or as many questions as they like and get their top
2 matches for free, each with a plain-language reason and a full course
outline; creating a free account (or paying $1) unlocks the top 4 matches
instead. Built per `Tech_Career_Assessment_PRD_v2.md` and the
`Comprehensive_Question_Bank_Psychometric.docx`.

## Stack

- **Backend**: FastAPI (Python) + SQLAlchemy (SQLite locally, Postgres in production)
- **Frontend**: React (Vite) + React Router
- **Auth**: Email + password, signed expiring tokens (no external JWT library)
- **Payments**: Stripe Checkout (international) + Paystack Checkout (Nigeria), test-mode by default — optional alternative to signing up
- **Email**: Gmail SMTP (App Password, port 465/SSL), styled HTML templates in a milky/cream theme

## The assessment engine

- **24 competencies** measured (Logical Reasoning, Creativity, Systems Thinking, Business Thinking, etc. — see `backend/app/data/competencies.py`)
- **88 questions**, 5 section types (`backend/app/data/questions_v3.py`):
  - Section A — 35 Likert (1-5 agreement) statements
  - Section B — 20 forced-choice (pick one of two)
  - Section C — 15 scenario-based (pick one of four reactions)
  - Section D — 10 situational judgment (pick one of four, no "correct" answer)
  - Section E — 8 preference-ranking (order 4 items most→least appealing)
- **69 careers** with full curricula (`backend/app/data/careers.py`) — the source document's Career Legend header says "70" but only 69 are actually enumerated
- **Derived competency→career matrix** (`backend/app/data/career_matrix.py`): the source document explicitly calls a 24×69 mapping matrix a separate "required artefact" it doesn't provide. Rather than inventing arbitrary weights, this matrix is *derived* from data already in the question bank — every question/option/ranking-item lists both its competency weights and the careers it signals ("careers_influenced"), so summing those signals per career and normalizing produces a fully-traceable matrix without a second hand-authored input. 5 careers (Mobile App Dev, Desktop App Dev, Game Dev, Blockchain Dev, Web3 Dev) are never referenced by any question and got small hand-authored fallback profiles instead.
- **Scoring** (`backend/app/scoring_v3.py`): partial completion is fully supported — every competency is normalized against the maximum achievable score from only the questions actually answered, so skipping questions doesn't unfairly zero out a trait. Final career scores come from a dot product against the derived matrix; the top-ranked careers become recommendations, each with a plain-language "why this fits" reason drawn from its highest-contributing competencies.

## Project layout

```
backend/            FastAPI app
  app/
    data/            competencies, 88-question bank, career matrix, career curricula
    routers/         API endpoints (auth, dashboard, leads, questions, submit, result, checkout, webhooks, consultation)
    main.py           app entrypoint
    auth.py           password hashing + signed token auth
    scoring_v3.py      competency scoring + career ranking + reason generation
    email_service.py  HTML email templates + SMTP sending
    payments.py        Stripe + Paystack integration
frontend/            React (Vite) app
  src/
    pages/            Landing, LeadCapture, Assessment, Results, Signup, Login, Dashboard
    components/        Navbar, Footer (with profile photo), ConsultationCTA
    api/client.js       API client, AuthContext.jsx auth state
```

## Running locally

**Easiest**: double-click the **"Start Career Assessment App"** shortcut on the Desktop
(or run `start_app.bat` in this folder). It opens the backend and frontend each
in their own window and launches your browser automatically.

### Manual — Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
copy .env.example .env       # then fill in real values (see below)
uvicorn app.main:app --reload --port 8000
```

### Manual — Frontend

```bash
cd frontend
npm install
copy .env.example .env       # set VITE_API_URL to match your backend port
npm run dev
```

Open the printed local URL (default `http://localhost:5173`).

## Environment variables (`backend/.env`)

| Variable | Purpose |
|---|---|
| `SECRET_KEY` | Random secret signing auth tokens — generate your own for production (`python -c "import secrets; print(secrets.token_hex(32))"`) |
| `SMTP_USER` / `SMTP_APP_PASSWORD` | Gmail address + [App Password](https://myaccount.google.com/apppasswords) used to send result emails |
| `STRIPE_SECRET_KEY` / `STRIPE_WEBHOOK_SECRET` | Stripe test/live keys — get from the Stripe Dashboard |
| `PAYSTACK_SECRET_KEY` / `PAYSTACK_PUBLIC_KEY` | Paystack test/live keys |
| `CONSULTATION_BOOKING_URL` | Calendly/Cal.com link shown after unlock |
| `PORTFOLIO_URL` | Shown in the footer and emails |
| `FRONTEND_URL` | Used to build Stripe/Paystack redirect + webhook links |

The repo ships with `SMTP_USER`/`SMTP_APP_PASSWORD` already filled in `backend/.env`
and **verified working** (SMTP over port 465/SSL). Paystack test keys are also
filled in and verified working end-to-end. Stripe keys are still placeholders —
replace `sk_test_replace_me` with real test (or live) keys before going live;
no code changes are needed.

## How the free vs. account vs. $1 tiers work

- **Anonymous (no account)**: takes the assessment via name+email only, sees
  their **top 2** recommended careers — each with the reason it matched and a
  full course outline. This is a one-off view, not saved anywhere they can log
  back into.
- **Signed up (free account)**: sees their **top 4** recommended careers
  immediately, saved to a personal **Dashboard** (`/dashboard`, lists every
  assessment taken), and emailed in full detail right after submitting. No
  payment involved — this is the primary way to unlock the top 4.
- **$1 unlock (Stripe/Paystack)**: still available for anonymous users who'd
  rather pay once than create an account, to see the same top 4 without
  signing up.

## Deploying to Render

The repo includes a `render.yaml` Blueprint that provisions both services in one go:

1. Push this repo to GitHub (already done: `github.com/Olalekan2040-slack/career`).
2. In the [Render Dashboard](https://dashboard.render.com/), click **New +** → **Blueprint**, and connect the `career` repo.
3. Render reads `render.yaml` and creates two services:
   - `career-assessment-backend` — FastAPI, free web service
   - `career-assessment-frontend` — static site (Vite build), free
4. Render will prompt you to fill in the env vars marked `sync: false` (secrets it won't
   auto-generate): `SMTP_USER`, `SMTP_APP_PASSWORD`, `STRIPE_SECRET_KEY`,
   `STRIPE_WEBHOOK_SECRET`, `PAYSTACK_SECRET_KEY`, `PAYSTACK_PUBLIC_KEY`,
   `CONSULTATION_BOOKING_URL`, and `DATABASE_URL` (see below).
5. After the first deploy, confirm the actual URLs Render assigned (it may append a
   suffix if the exact name is taken — this happened on first deploy; the backend
   is actually at `career-assessment-backend-a0xc.onrender.com`). If either differs
   from what's in `render.yaml`, update `FRONTEND_URL` (backend service) and
   `VITE_API_URL` (frontend service) env vars to match, then redeploy — the
   frontend needs a full rebuild since Vite bakes env vars in at build time.
6. Once you have real Stripe/Paystack keys, add your backend's webhook URLs in each
   provider's dashboard:
   - Stripe: `https://<your-backend-url>/api/webhooks/stripe`
   - Paystack: `https://<your-backend-url>/api/webhooks/paystack`

### Database: Postgres, not SQLite, in production

Render's free web services use an ephemeral filesystem — a SQLite file would be wiped
on every deploy or restart. The app already uses SQLAlchemy, so switching databases is
just a `DATABASE_URL` change:

1. Create a Render Postgres instance (or use one you already have).
2. Copy its **Internal Database URL** from the Render dashboard (only reachable from
   other Render services, not from your own machine — that's expected).
3. Paste it into the backend service's `DATABASE_URL` env var in the Render dashboard.
4. Redeploy the backend. `Base.metadata.create_all()` runs on startup and creates the
   tables automatically on first boot against the new database.

Locally, `DATABASE_URL` is unset and the app falls back to SQLite (`backend/.env` /
`.env.example`) — no need to touch anything for local dev.

**Known limitations of this setup** (accepted for now, revisit before real launch):
- Render's free web services spin down after ~5 minutes of inactivity and cold-start
  slowly on the next request. Two mitigations are already in place: the frontend
  pings `/api/health` every 4 minutes while a visitor has the site open
  (`frontend/src/api/useKeepAlive.js`), and a GitHub Actions workflow
  (`.github/workflows/keep-alive.yml`) pings it every 5 minutes independent of
  traffic. For a stronger guarantee, a dedicated uptime service (e.g. UptimeRobot)
  is more reliable than GitHub's best-effort scheduler.

## What's implemented

- Full 88-question, 5-format psychometric assessment scoring 24 competencies
  and ranking all 69 careers from day one, with partial-completion support
- Derived competency→career mapping matrix, fully traceable to the source
  question bank (see "The assessment engine" above)
- Full curriculum + resources for all 69 careers (4-phase outline + 3
  resources each)
- Plain-language "why this fits" reason generated per recommendation
- Free tier (top 2, anonymous) vs. account/paid tier (top 4) recommendation
  counts, matching the requested "signed in = 4, anonymous = 2" behaviour
- Email + password signup/login, dashboard listing full assessment history
- $1 unlock via Stripe or Paystack (manual + locale-based provider toggle),
  webhook-driven unlock + confirmation polling — optional alternative to signup
- Result emails (2- and 4-recommendation tiers), milky-themed, with reasons
  and full curricula included, footer/portfolio link, and a profile photo
- Consultation booking CTA available on every result screen
- Desktop shortcut (`start_app.bat` + Desktop `.lnk`) to launch both servers
  without a terminal
- Backend keep-alive (frontend heartbeat + GitHub Actions cron) to reduce
  Render free-tier cold starts
- Postgres in production (Render), SQLite for local dev — same SQLAlchemy
  models, just a `DATABASE_URL` env var difference

## Not implemented / needs your input before launch

- Real Stripe API keys (Paystack test keys are filled in and verified; Stripe
  is still a placeholder — payments via Stripe will error until you add keys)
- Calendly/Cal.com embed — currently a plain link (`CONSULTATION_BOOKING_URL`)
  rather than a live scheduler; the in-app "Book a consultation" form logs the
  request to the database instead of syncing with an external calendar
- Password reset / email verification for accounts — not built yet
- Retroactively "claiming" an anonymous result after signing up — not built;
  signing up affects assessments taken from that point forward
- The 5 careers with no question-bank signal (Mobile App Dev, Desktop App
  Dev, Game Dev, Blockchain Dev, Web3 Dev) use hand-authored fallback
  competency profiles rather than derived ones — reasonable but worth
  reviewing if those careers start showing up as recommendations often
