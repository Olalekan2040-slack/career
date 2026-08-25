# Deployment Guide - Tech Career Assessment Platform

## Overview

This guide explains how to deploy the Tech Career Assessment platform to **Render** using **PostgreSQL** as the production database.

### Architecture
- **Frontend**: Static site (Vite/React) on Render
- **Backend**: FastAPI on Render  
- **Database**: PostgreSQL on Render
- **Email**: Brevo API (no SMTP ports needed)

---

## Database Configuration

### Development (SQLite)
```
DATABASE_URL=sqlite:///./assessment.db
```
- Stores data in local `assessment.db` file
- Suitable for local development and testing
- No password or connection string needed

### Production (PostgreSQL)
```
DATABASE_URL=postgresql://username:password@host:5432/dbname
```
- Uses Render's managed PostgreSQL service
- Persistent data across server restarts
- Accessible only from other Render services (Internal Database URL)

### Verify Current Configuration
The application automatically detects the database type:
- If `DATABASE_URL` starts with `postgresql://` → uses PostgreSQL
- Otherwise → uses SQLite

Check config with:
```python
from app.config import settings
print(f"Using PostgreSQL: {settings.is_postgres}")
print(f"Production mode: {settings.is_production}")
```

---

## Step-by-Step Render Deployment

### Step 1: Create PostgreSQL Database Service

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **"New +"** → **"PostgreSQL"**
3. Configure:
   - **Name**: `career-assessment-db`
   - **Database**: `assessment`
   - **User**: `assessment_user` (auto-generated)
   - **Region**: Choose closest to your users
   - **Plan**: Free (for testing) or Starter (production)
4. Click **Create Database**
5. **Copy the Internal Database URL** (format: `postgresql://...`)
   - You'll use this for the backend service
   - Only accessible from other Render services

**Important**: Save the Internal Database URL for Step 3!

### Step 2: Set Up Backend Service

1. Connect your GitHub repository to Render
2. Click **"New +"** → **"Web Service"**
3. Configure:
   - **Name**: `career-assessment-backend`
   - **Runtime**: `Python 3.13`
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

### Step 3: Add Environment Variables for Backend

In the backend service settings, add these environment variables:

| Variable | Value | Notes |
|----------|-------|-------|
| `ENVIRONMENT` | `production` | Enables production mode |
| `DATABASE_URL` | `postgresql://...` | Paste the Internal Database URL from Step 1 |
| `SECRET_KEY` | [generate below] | Must be random and unique |
| `ADMIN_EMAILS` | `olalekanquadri58@gmail.com` | Can be comma-separated |
| `FRONTEND_URL` | `https://career-assessment-frontend.onrender.com` | Will be updated after frontend deploy |
| `BREVO_API_KEY` | [your API key] | Get from brevo.com/settings/keys/api |
| `EMAIL_FROM_ADDRESS` | `olalekanquadri58@gmail.com` | Must match Brevo sender |
| `EMAIL_FROM_NAME` | `Global Digital Skills Assessment` | Display name for emails |
| `STRIPE_SECRET_KEY` | [test or live key] | Optional - only if payments enabled |
| `STRIPE_WEBHOOK_SECRET` | [webhook secret] | Optional - only if payments enabled |
| `PAYSTACK_SECRET_KEY` | [test or live key] | Optional - only if payments enabled |
| `PAYSTACK_PUBLIC_KEY` | [public key] | Optional - only if payments enabled |
| `PAYMENTS_ENABLED` | `false` | Set to true to enable payments |

#### Generate SECRET_KEY

Run this command locally:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Output example:
```
a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6
```

Copy the output and paste into Render dashboard.

### Step 4: Set Up Frontend Service

1. Click **"New +"** → **"Static Site"**
2. Configure:
   - **Name**: `career-assessment-frontend`
   - **Root Directory**: `frontend`
   - **Build Command**: `npm install && npm run build`
   - **Publish Directory**: `dist`

3. Add Environment Variable:
   - **VITE_API_URL**: `https://career-assessment-backend.onrender.com`
   - (Replace with your actual backend URL once deployed)

### Step 5: Update FRONTEND_URL in Backend

Once the frontend is deployed, go back to the backend service and update:
- **FRONTEND_URL**: `https://career-assessment-frontend.onrender.com`

This is needed for CORS configuration.

---

## Environment Variables Summary

### Required for Production

```env
ENVIRONMENT=production
DATABASE_URL=postgresql://username:password@host:5432/dbname
SECRET_KEY=[generated random value]
ADMIN_EMAILS=olalekanquadri58@gmail.com
FRONTEND_URL=https://your-frontend-url.onrender.com
EMAIL_FROM_ADDRESS=your-email@example.com
EMAIL_FROM_NAME=Your Company Name
```

### Optional (Email/Payments)

```env
BREVO_API_KEY=your-api-key        # For transactional emails
STRIPE_SECRET_KEY=sk_test_...     # If using Stripe
STRIPE_WEBHOOK_SECRET=whsec_...   # If using Stripe
PAYSTACK_SECRET_KEY=sk_test_...   # If using Paystack
PAYSTACK_PUBLIC_KEY=pk_test_...   # If using Paystack
PAYMENTS_ENABLED=false             # Set true to enable
```

### All Variables with Descriptions

| Variable | Default | Description |
|----------|---------|-------------|
| `ENVIRONMENT` | `development` | `development`, `staging`, or `production` |
| `FRONTEND_URL` | `http://localhost:5173` | Frontend URL for CORS |
| `SECRET_KEY` | `dev-secret-...` | Auth token signing key (must be random in production) |
| `DATABASE_URL` | `sqlite:///./assessment.db` | SQLite (dev) or PostgreSQL (prod) connection string |
| `ADMIN_EMAILS` | `olalekanquadri58@gmail.com` | Comma-separated list of admin user emails |
| `BREVO_API_KEY` | (empty) | Brevo transactional email API key |
| `EMAIL_FROM_ADDRESS` | `olalekanquadri58@gmail.com` | Sender email address |
| `EMAIL_FROM_NAME` | `Global Digital Skills Assessment` | Sender display name |
| `PAYMENTS_ENABLED` | `false` | Enable payment checkout |
| `STRIPE_SECRET_KEY` | (empty) | Stripe API secret key |
| `STRIPE_WEBHOOK_SECRET` | (empty) | Stripe webhook signing secret |
| `STRIPE_PRICE_USD_CENTS` | `100` | Price for unlock ($1.00) |
| `PAYSTACK_SECRET_KEY` | (empty) | Paystack API secret key |
| `PAYSTACK_PUBLIC_KEY` | (empty) | Paystack API public key |
| `PAYSTACK_AMOUNT_KOBO` | `150000` | Price in Kobo (1500 ₦) |
| `CONSULTATION_BOOKING_URL` | `https://calendly.com/...` | Consultation booking link |
| `PORTFOLIO_URL` | `https://quaddev.onrender.com/` | Portfolio/company website |

---

## Getting API Keys

### Brevo (Email)
1. Go to [Brevo](https://app.brevo.com)
2. Sign up or log in
3. Settings → API Keys
4. Copy API Key v3
5. Paste into Render environment variables

### Stripe (Optional)
1. Go to [Stripe Dashboard](https://dashboard.stripe.com)
2. Use test keys for development, live keys for production
3. API Keys → Copy Secret Key and Webhook Secret

### Paystack (Optional)
1. Go to [Paystack Dashboard](https://dashboard.paystack.com)
2. Settings → Developer
3. Copy secret and public keys

---

## Deployment Checklist

- [ ] PostgreSQL database created on Render
- [ ] Internal Database URL copied
- [ ] Backend service created on Render
- [ ] All environment variables set in backend service
- [ ] Frontend service created on Render
- [ ] `VITE_API_URL` set to backend service URL
- [ ] Backend `FRONTEND_URL` updated to frontend service URL
- [ ] Backend service deployed successfully
- [ ] Frontend service deployed successfully
- [ ] Test login at `/login`
- [ ] Test admin dashboard at `/admin` (with admin email)
- [ ] Test assessment workflow end-to-end
- [ ] Verify emails are being sent (if BREVO_API_KEY configured)

---

## Troubleshooting

### Database Connection Errors

**Error**: `no such table: users`
- **Cause**: SQLite database doesn't exist in production
- **Solution**: Ensure `DATABASE_URL` is set to PostgreSQL URL, not SQLite

**Error**: `could not connect to server: Connection refused`
- **Cause**: PostgreSQL service not running or wrong URL
- **Solution**: 
  1. Check Render PostgreSQL service is "Available"
  2. Verify Internal Database URL is correct
  3. Ensure it's the Internal URL (for Render-to-Render access)

### Email Not Sending

**Symptom**: No emails received but no error in logs
- **Cause**: `BREVO_API_KEY` not set or empty
- **Solution**: 
  1. Get API key from brevo.com
  2. Set `BREVO_API_KEY` in environment variables
  3. Restart backend service

### CORS Errors in Browser

**Error**: `Access to XMLHttpRequest blocked by CORS policy`
- **Cause**: Frontend URL not matching `FRONTEND_URL` in backend
- **Solution**:
  1. Check browser console for exact frontend URL
  2. Update `FRONTEND_URL` in backend environment variables
  3. Restart backend service

### Admin Dashboard Not Accessible

**Error**: Redirected to home page after login
- **Cause**: User email not in `ADMIN_EMAILS`
- **Solution**:
  1. Create account with email in `ADMIN_EMAILS`
  2. Or update `ADMIN_EMAILS` to include your email
  3. Re-login to sync admin flag

---

## Local Development

### Using SQLite (Default)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Switching to PostgreSQL Locally
```bash
# Install PostgreSQL locally, create database
createdb assessment

# Set connection string
export DATABASE_URL="postgresql://postgres:password@localhost/assessment"

# Or add to .env:
# DATABASE_URL=postgresql://postgres:password@localhost/assessment

# Run
uvicorn app.main:app --reload
```

---

## Performance & Scaling

### Database Indexing
PostgreSQL automatically indexes primary keys and foreign keys. For better query performance, consider adding indexes:

```sql
CREATE INDEX idx_assessment_responses_lead_id ON assessment_responses(lead_id);
CREATE INDEX idx_assessment_responses_submitted_at ON assessment_responses(submitted_at DESC);
CREATE INDEX idx_results_created_at ON results(created_at DESC);
```

### Connection Pooling
For high-traffic deployments, consider using SQLAlchemy with a connection pool:

```python
# In database.py
from sqlalchemy.pool import NullPool

engine = create_engine(
    settings.database_url,
    poolclass=NullPool if settings.is_production else None,
)
```

### Free Tier Limitations
Render's free PostgreSQL includes:
- 256 MB storage
- ~1000 rows typical capacity
- Auto-suspend after 7 days of inactivity

Upgrade to Starter plan for production workloads.

---

## Monitoring & Maintenance

### View Logs
```bash
# In Render dashboard, select backend service → Logs
# View real-time application output
```

### Database Backups
Render PostgreSQL includes automatic daily backups for paid plans.
For free tier, manually export:

```bash
pg_dump -U assessment_user -h host assessment > backup.sql
```

### Monitor Resources
Check Render dashboard for:
- CPU usage
- Memory usage
- Network I/O
- Disk space

---

## Additional Resources

- [Render Documentation](https://render.com/docs)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [FastAPI Production Guide](https://fastapi.tiangolo.com/deployment/)
- [SQLAlchemy PostgreSQL](https://docs.sqlalchemy.org/en/20/dialects/postgresql.html)

