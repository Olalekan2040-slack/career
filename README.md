# Global Digital Skills Career Assessment Platform

A career assessment purpose-built for people who are new to tech and don't
yet know their own aptitude — not a quiz for people who've already decided
what they want. A short background intake (age range, education, field of
study, prior tech exposure, and broader interests) branches an **adaptive**
question flow drawn from an 88-item, 5-format psychometric bank (Likert
agreement, forced-choice, scenario-based, situational judgment, and
preference ranking), scoring 24 underlying competencies. The number of
questions asked isn't fixed — the engine keeps asking, picking whichever
next question best separates the current leading candidates, until it's
confident or ~5 minutes have passed. No account or password — just a name
and email — before the top 4 recommended careers (from a curated 28-career
shortlist) appear on-screen and are emailed in full detail, each with a
plain-language reason, a full course outline, and — for careers that
usually assume prior technical exposure — a caveat pointing to an easier
starting point if the respondent flagged none. Built per
`Tech_Career_Assessment_PRD_v2.md` and the
`Comprehensive_Question_Bank_Psychometric.docx`.

## Stack

- **Backend**: FastAPI (Python) + SQLAlchemy (SQLite locally, Postgres in production)
- **Frontend**: React (Vite) + React Router
- **Auth**: Email + password login exists only for the hidden admin view (`/login` → `/admin`) — regular respondents never see it, see "Accounts, admin, and payments" below
- **Payments**: Stripe + Paystack integration exists in the backend but is deactivated platform-wide (`PAYMENTS_ENABLED=false`)
- **Email**: Gmail SMTP (App Password, port 465/SSL), styled HTML templates in a milky/cream theme

## The assessment engine

- **Background intake** (`backend/app/data/intake.py`): age range, education
  level, field of study, prior tech exposure, and a broad interest area
  (technology, business, arts, people, science, or hands-on work) — collected
  before any competency question. Age/education/gender are for context and
  reporting only; field of study, tech exposure, and interest area actively
  drive question selection and result caveats.
- **24 competencies** measured (Logical Reasoning, Creativity, Systems Thinking, Business Thinking, etc. — see `backend/app/data/competencies.py`)
- **88-question bank**, 5 section types (`backend/app/data/questions_v3.py`):
  Likert (35), forced-choice (20), scenario-based (15), situational judgment
  (10), preference ranking (8) — see the module docstring for the full
  breakdown.
- **Adaptive selection, not a fixed set** (`backend/app/adaptive.py`): the
  first ~8 questions are weighted toward competencies related to the
  respondent's stated interest area (branching on their background from
  question 1, not sampling randomly). After that, each new question is
  chosen based on which competency would most separate the current top-5
  candidate careers — an honest, practical approximation of adaptive testing
  (not full Item Response Theory, which needs item parameters calibrated
  from response data this platform doesn't have yet). The test stops when a
  confidence gap opens up between the leading and 5th-ranked career (minimum
  12 questions), a hard cap of 30 questions is hit, or ~4.5 minutes have
  elapsed — whichever comes first.
- **28-career shortlist** (`backend/app/data/shortlist.py`): recommendations
  are drawn only from a curated subset of the full 69-career taxonomy —
  Full-Stack/Frontend/Backend Dev, AI, ML, UI/UX, Graphic Design, Video
  Editing, Content Writing, Social Media Management, Virtual Assistance,
  Data Analysis, Data Science, Cloud Computing, Cybersecurity, Mobile Dev,
  QA, Animation, Data Engineering, Digital Marketing, SEO, Technical
  Writing, Product/Project Management, DevOps, IT Support, Motion Graphics,
  and Copywriting — chosen for a beginner audience that needs a short,
  confident list rather than an exhaustive catalogue.
- **Entry-level caveats**: 10 of those 28 (Full-Stack, Backend, AI, ML, Data
  Science, Cloud Computing, Cybersecurity, Mobile Dev, Data Engineering,
  DevOps) are flagged as usually needing prior programming/technical
  exposure. If a respondent who flagged no tech exposure still matches one
  strongly, it's still shown (not hidden), but with a note naming an easier
  starting point (e.g. Cybersecurity → IT Support first).
- **Derived competency→career matrix** (`backend/app/data/career_matrix.py`): the source document explicitly calls a 24×69 mapping matrix a separate "required artefact" it doesn't provide. Rather than inventing arbitrary weights, this matrix is *derived* from data already in the question bank — every question/option/ranking-item lists both its competency weights and the careers it signals ("careers_influenced"), so summing those signals per career and normalizing produces a fully-traceable matrix without a second hand-authored input. 5 careers (Mobile App Dev, Desktop App Dev, Game Dev, Blockchain Dev, Web3 Dev) are never referenced by any question and got small hand-authored fallback profiles instead.
- **Scoring** (`backend/app/scoring_v3.py`): partial completion is fully supported — every competency is normalized against the maximum achievable score from only the questions actually answered, so skipping questions doesn't unfairly zero out a trait. Final career scores come from a dot product against the derived matrix (restricted to the 28-career shortlist); the top-ranked careers become recommendations, each with a plain-language "why this fits" reason drawn from its highest-contributing competencies.

**On accuracy — an honest limit.** No short self-report questionnaire, adaptive
or not, can reliably surface traits a person is genuinely blind to (that's
what projective testing or long behavioral observation is for). What this
engine does to get meaningfully closer: indirect scenario/forced-choice items
(which reveal more than direct self-rating), and a competency profile that's
independent of self-reported tech interest — so a gap between what someone
says excites them and what their answers show can surface as a genuine
insight rather than just confirming what they already believed about themselves.

## Project layout

```
backend/            FastAPI app
  app/
    data/            competencies, 88-question bank, career matrix, curricula, shortlist, intake schema
    routers/         API endpoints (auth, admin, assessment, leads, questions, submit, result, checkout, webhooks, consultation)
    main.py           app entrypoint
    auth.py           password hashing + signed token auth + admin flag sync
    adaptive.py        question selection + stopping logic
    scoring_v3.py      competency scoring + career ranking + reason generation
    email_service.py  HTML email templates + SMTP sending
    payments.py        Stripe + Paystack integration (deactivated by default)
frontend/            React (Vite) app
  src/
    pages/            Landing, LeadCapture, Assessment, Results, Login (admin), Admin
    components/        Navbar, Footer (with profile photo), ConsultationCTA
    api/client.js       API client, AuthContext.jsx auth state (admin session only)
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
| `ADMIN_EMAILS` | Comma-separated emails auto-granted admin access (`/admin` user list) on signup/login |
| `SMTP_USER` / `SMTP_APP_PASSWORD` | Gmail address + [App Password](https://myaccount.google.com/apppasswords) used to send result emails |
| `PAYMENTS_ENABLED` | `false` by default — set to `true` to re-enable the Stripe/Paystack checkout endpoints |
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

## Accounts, admin, and payments

- **No signup, no password, no login** for respondents. `/start` collects
  just a name and email (`POST /api/leads`), which flows straight into the
  assessment. `POST /api/leads` and `POST /api/submit` are both fully public
  — no auth token involved anywhere in the respondent-facing flow.
- Everyone who finishes sees their **top 4** recommended careers on-screen
  immediately, and gets them emailed in full detail (background task, so the
  results page doesn't wait on the SMTP round trip).
- **Admin access** is the *only* thing behind a login, and it's not linked
  from the public nav — it's a plain email+password account (`/login`,
  reusing the same auth system) whose email is listed in the `ADMIN_EMAILS`
  env var (comma-separated; defaults to `olalekanquadri58@gmail.com`),
  auto-flagged `is_admin` on signup/login. Logged-in admins see an **Admin**
  link leading to `/admin`, listing every respondent's name, email, and
  submission date (`GET /api/admin/leads`, 403 for non-admins). There's no
  public "Sign up" page — the admin account is created once via
  `POST /api/auth/signup` directly (not through any UI).
- **Payments (Stripe/Paystack)**: deactivated platform-wide via
  `PAYMENTS_ENABLED=false` (default) — `POST /api/checkout/stripe` and
  `/paystack` both return `503` immediately without calling either provider.
  The integration itself (`backend/app/payments.py`, `routers/checkout.py`,
  `routers/webhooks.py`) is untouched and can be re-enabled by flipping that
  one setting if a paid tier is wanted again later.

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
- `Base.metadata.create_all()` only creates *missing* tables — it never alters
  an existing table to add new columns. If you add columns to a model in the
  future, either run an `ALTER TABLE` against the live database or drop/recreate
  the affected table (only safe if it doesn't hold real data you need). The
  production Postgres database was fully wiped (all tables dropped) as part of
  this change specifically to pick up the intake columns cleanly — expect an
  empty `leads`/`results` table on first login to `/admin` after this deploy.

## What's implemented

- Background intake (age, education, field of study, tech exposure, broad
  interest area) collected before the assessment, driving both question
  selection and result caveats
- Adaptive question selection — no fixed question count; the engine picks
  each next question based on the respondent's background and answers so
  far, and stops on a confidence signal or a ~5-minute time cap (12-30
  questions in practice), not a hard-coded number
- Recommendations drawn from a curated 28-career shortlist (not the full 69),
  chosen for a beginner audience
- Entry-level caveats on 10 "advanced" careers, naming an easier starting
  point when a respondent with no prior tech exposure still matches strongly
- Derived competency→career mapping matrix, fully traceable to the source
  question bank (see "The assessment engine" above)
- Full curriculum + resources for all 69 careers in the underlying taxonomy
  (4-phase outline + 3 resources each), 28 of which are ever recommended
- Plain-language "why this fits" reason generated per recommendation
- No signup or login for respondents — just name + email before the
  assessment; results shown on-screen and emailed, no account required
- Admin page (`/admin`, gated by a hidden `/login` and `ADMIN_EMAILS`)
  listing every respondent's name, email, and submission date
- Payments (Stripe/Paystack) deactivated via `PAYMENTS_ENABLED=false` —
  checkout endpoints return 503 immediately, no live provider calls
- Result emails, milky-themed, with reasons, entry-level caveats, and full
  curricula included, footer/portfolio link, and a profile photo — sent via a
  background task so the results page loads immediately instead of waiting
  on the SMTP round trip
- Going back to a previously answered question highlights your previous
  choice so you can review and change it, without breaking the adaptive flow
  going forward
- Consultation booking CTA available on every result screen
- Desktop shortcut (`start_app.bat` + Desktop `.lnk`) to launch both servers
  without a terminal
- Backend keep-alive (frontend heartbeat + GitHub Actions cron) to reduce
  Render free-tier cold starts
- Postgres in production (Render), SQLite for local dev — same SQLAlchemy
  models, just a `DATABASE_URL` env var difference

## Not implemented / needs your input before launch

- Calendly/Cal.com embed — currently a plain link (`CONSULTATION_BOOKING_URL`)
  rather than a live scheduler; the in-app "Book a consultation" form logs the
  request to the database instead of syncing with an external calendar
- Password reset / email verification for accounts — not built yet
- The adaptive engine is a practical heuristic, not calibrated Item Response
  Theory — there's no prior response data yet to calibrate item difficulty
  against, so "confidence" is measured by score separation between candidate
  careers rather than a formally validated statistic
- The 5 careers with no question-bank signal (Mobile App Dev, Desktop App
  Dev, Game Dev, Blockchain Dev, Web3 Dev) use hand-authored fallback
  competency profiles rather than derived ones — reasonable but worth
  reviewing if those careers start showing up as recommendations often
