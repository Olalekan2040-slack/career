# Global Digital Skills Career Assessment Platform

A free career assessment — no signup required to take it — that matches users
to one of 24 digital career paths (11 code-based, 13 non-coding). Anyone can
try the test anonymously and see a basic result; creating a free account
unlocks the full strengths breakdown and course outline in a personal
dashboard (and by email), no payment required. A $1 Stripe/Paystack unlock
remains available as an alternative for anonymous users who don't want to
sign up. Built per `Tech_Career_Assessment_PRD_v2.md` and
`Tech_Assessment_QuestionBank_v2.docx`.

## Stack

- **Backend**: FastAPI (Python) + SQLAlchemy + SQLite
- **Frontend**: React (Vite) + React Router
- **Auth**: Email + password, signed expiring tokens (no external JWT library)
- **Payments**: Stripe Checkout (international) + Paystack Checkout (Nigeria), test-mode by default — optional alternative to signing up
- **Email**: Gmail SMTP (App Password, port 465/SSL), styled HTML templates in a milky/cream theme

## Project layout

```
backend/            FastAPI app
  app/
    data/            question bank + category/curriculum content
    routers/         API endpoints (auth, dashboard, leads, questions, submit, result, checkout, webhooks, consultation, waitlist)
    main.py           app entrypoint
    auth.py           password hashing + signed token auth
    scoring.py        orientation routing + category scoring logic
    email_service.py  HTML email templates + SMTP sending
    payments.py        Stripe + Paystack integration
frontend/            React (Vite) app
  src/
    pages/            Landing, LeadCapture, Assessment, Results, Signup, Login, Dashboard
    components/        Navbar, Footer, ConsultationCTA
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
| `PAYSTACK_SECRET_KEY` | Paystack test/live secret key |
| `CONSULTATION_BOOKING_URL` | Calendly/Cal.com link shown after unlock |
| `PORTFOLIO_URL` | Shown in the footer and emails |
| `FRONTEND_URL` | Used to build Stripe/Paystack redirect + webhook links |

The repo ships with `SMTP_USER`/`SMTP_APP_PASSWORD` already filled in `backend/.env`
and **verified working** (SMTP over port 465/SSL — port 587/STARTTLS was blocked
in the build sandbox but 465 is not; both should work on a normal host). Stripe
and Paystack keys are placeholders — replace `sk_test_replace_me` with real
test (or live) keys before going live; no code changes are needed.

## How the free vs. account vs. $1 tiers work

- **Anonymous (no account)**: takes the assessment via name+email only, sees a
  basic result (primary shown, secondary locked, no curriculum) — this is the
  "recent version of their result," not saved anywhere they can log back into.
- **Signed up (free account)**: full strengths breakdown (all 24 category
  scores, ranked) and full 4-phase course outline for both primary and
  secondary appear immediately on the results page, in their **Dashboard**
  (`/dashboard`, lists every assessment they've taken), and in a detailed
  email sent right after submitting. No payment involved.
- **$1 unlock (Stripe/Paystack)**: still available for anonymous users who'd
  rather pay once than create an account — unchanged from the original flow.

## What's implemented (Phase 1 per PRD Section 9)

- Full assessment engine scoring all 24 categories from day one (Orientation
  8 questions → routes to Track A or B → 12/13-question deep-dive → primary +
  secondary recommendation, with the "close call" consultation nudge)
- Full curriculum + resources for the 8 Phase-1 categories: Frontend Dev,
  Backend Dev, UI/UX Design, Graphic Design, Digital Marketing, Virtual
  Assistance, Video Editing, Cybersecurity
- "Coming soon" waitlist capture for the other 16 categories
- Email + password signup/login, dashboard listing full assessment history
- $1 unlock via Stripe or Paystack (manual + locale-based provider toggle),
  webhook-driven unlock + confirmation polling — optional alternative to signup
- Free-tier and detailed HTML emails, milky-themed, with footer/portfolio link
- Consultation booking CTA available on every result screen
- Desktop shortcut (`start_app.bat` + Desktop `.lnk`) to launch both servers
  without a terminal
- SQLite storage via SQLAlchemy — swap `DATABASE_URL` to Postgres later with
  no code changes (per PRD Section 8.2)

## Not implemented / needs your input before launch

- Real Stripe/Paystack API keys (currently placeholders — payments will
  error until you add live/test keys)
- Hosting/deployment (PRD recommends Vercel/Netlify for frontend, Render/Railway
  for backend)
- Calendly/Cal.com embed — currently a plain link (`CONSULTATION_BOOKING_URL`)
  rather than a live scheduler; the in-app "Book a consultation" form logs the
  request to the database instead of syncing with an external calendar
- Password reset / email verification for accounts — not built yet
- Retroactively "claiming" an anonymous result after signing up — not built;
  signing up affects assessments taken from that point forward
