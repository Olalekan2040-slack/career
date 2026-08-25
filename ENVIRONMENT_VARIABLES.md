# Production Environment Variables Checklist

## Quick Reference - All Environment Variables Needed for Render Deployment

Copy and customize this for your Render environment variable setup:

```env
# === PRODUCTION CONFIGURATION ===
ENVIRONMENT=production
SECRET_KEY=[GENERATE NEW - see below]

# === FRONTEND & CORS ===
FRONTEND_URL=https://career-assessment-frontend.onrender.com

# === DATABASE (PostgreSQL on Render) ===
DATABASE_URL=[PASTE INTERNAL DATABASE URL FROM RENDER POSTGRES SERVICE]
# Format: postgresql://username:password@host:5432/dbname
# Example: postgresql://assessment_user:pass123@dpg-abc123.renders.com:5432/assessment

# === ADMIN ACCESS ===
ADMIN_EMAILS=olalekanquadri58@gmail.com
# Add more admins: email1@example.com,email2@example.com

# === EMAIL CONFIGURATION (Brevo API) ===
BREVO_API_KEY=[YOUR BREVO API KEY]
# Get from: https://app.brevo.com/settings/keys/api
EMAIL_FROM_ADDRESS=olalekanquadri58@gmail.com
EMAIL_FROM_NAME=Global Digital Skills Assessment

# === PAYMENT CONFIGURATION (Optional - set to false to disable) ===
PAYMENTS_ENABLED=false

# === STRIPE (Optional - only if PAYMENTS_ENABLED=true) ===
STRIPE_SECRET_KEY=sk_test_YOUR_KEY_HERE_OR_sk_live_FOR_PRODUCTION
STRIPE_WEBHOOK_SECRET=whsec_YOUR_SECRET_HERE
STRIPE_PRICE_USD_CENTS=100

# === PAYSTACK (Optional - only if PAYMENTS_ENABLED=true) ===
PAYSTACK_SECRET_KEY=sk_test_YOUR_KEY_HERE_OR_sk_live_FOR_PRODUCTION
PAYSTACK_PUBLIC_KEY=pk_test_YOUR_KEY_HERE_OR_pk_live_FOR_PRODUCTION
PAYSTACK_AMOUNT_KOBO=150000

# === CONSULTATION & PORTFOLIO ===
CONSULTATION_BOOKING_URL=https://calendly.com/your-handle/consultation
PORTFOLIO_URL=https://quaddev.onrender.com/
```

---

## Step-by-Step: Setting These in Render Dashboard

### 1. Generate SECRET_KEY

Run locally:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Example output:
```
a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6
```

### 2. Get PostgreSQL Internal Database URL

1. In Render Dashboard, click on your PostgreSQL service
2. Go to "Internal Database URL"
3. Copy the full URL (format: `postgresql://username:password@host:5432/dbname`)

### 3. Add Variables to Backend Service

1. In Render Dashboard, select backend service
2. Click "Environment" 
3. Add each variable from the checklist above
4. Click "Save Changes"
5. Backend will auto-redeploy with new variables

---

## Environment Variables by Purpose

### 🔒 Security (REQUIRED - Production)

| Variable | Value | Generate/Get From |
|----------|-------|-------------------|
| `SECRET_KEY` | Random hex string | `python -c "import secrets; print(secrets.token_hex(32))"` |
| `ENVIRONMENT` | `production` | Fixed value |
| `ADMIN_EMAILS` | Your admin emails | Your email address |

### 📡 Connectivity (REQUIRED)

| Variable | Value | Notes |
|----------|-------|-------|
| `FRONTEND_URL` | Frontend service URL | `https://career-assessment-frontend.onrender.com` |
| `DATABASE_URL` | PostgreSQL URL | From Render PostgreSQL service |

### 📧 Email (REQUIRED for emails to work)

| Variable | Value | Get From |
|----------|-------|----------|
| `BREVO_API_KEY` | Brevo API key | https://app.brevo.com/settings/keys/api |
| `EMAIL_FROM_ADDRESS` | Sender email | Must match Brevo verified sender |
| `EMAIL_FROM_NAME` | Display name | Any company/app name |

### 💳 Payments (OPTIONAL)

| Variable | Value | Get From | Required If |
|----------|-------|----------|-------------|
| `PAYMENTS_ENABLED` | `true`/`false` | Set in env | Enabling payments |
| `STRIPE_SECRET_KEY` | Secret key | https://dashboard.stripe.com/apikeys | Using Stripe |
| `STRIPE_WEBHOOK_SECRET` | Webhook secret | https://dashboard.stripe.com/webhooks | Using Stripe |
| `PAYSTACK_SECRET_KEY` | Secret key | https://dashboard.paystack.com/settings/developer | Using Paystack |
| `PAYSTACK_PUBLIC_KEY` | Public key | https://dashboard.paystack.com/settings/developer | Using Paystack |

### 🎯 Customization (OPTIONAL)

| Variable | Default | Example |
|----------|---------|---------|
| `CONSULTATION_BOOKING_URL` | `https://calendly.com/...` | Your Calendly link |
| `PORTFOLIO_URL` | `https://quaddev.onrender.com/` | Your website |
| `STRIPE_PRICE_USD_CENTS` | `100` | `9999` for $99.99 |
| `PAYSTACK_AMOUNT_KOBO` | `150000` | `100000` for 1000 ₦ |

---

## Database URL Format

### PostgreSQL (Production on Render)

```
postgresql://username:password@host:port/dbname
```

**Example from Render:**
```
postgresql://assessment_user_xyz:abc123def456@dpg-abcdef123456.renders.com:5432/assessment_abc123
```

**How to get:**
1. Create PostgreSQL service on Render
2. Click on service name
3. Go to "Internal Database URL" section
4. Copy the entire URL

**Important**: Use **Internal Database URL** (not External) for backend service

---

## Complete Copy-Paste Template for Render

Here's the exact format to enter in Render "Environment Variables" section:

```
ENVIRONMENT=production
SECRET_KEY=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6
DATABASE_URL=postgresql://assessment_user:password123@dpg-abc123.renders.com:5432/assessment
FRONTEND_URL=https://career-assessment-frontend.onrender.com
ADMIN_EMAILS=olalekanquadri58@gmail.com
BREVO_API_KEY=xxxxxxxxxxxxxxxxxxx
EMAIL_FROM_ADDRESS=olalekanquadri58@gmail.com
EMAIL_FROM_NAME=Global Digital Skills Assessment
PAYMENTS_ENABLED=false
CONSULTATION_BOOKING_URL=https://calendly.com/your-handle/consultation
PORTFOLIO_URL=https://quaddev.onrender.com/
```

---

## Pre-Deployment Checklist

- [ ] PostgreSQL service created on Render
- [ ] Internal Database URL copied
- [ ] `SECRET_KEY` generated and copied
- [ ] `BREVO_API_KEY` obtained from brevo.com
- [ ] Frontend URL determined (or temporary)
- [ ] Backend "Environment" section has all variables
- [ ] All required variables filled (no empty ones)
- [ ] Values verified for typos
- [ ] Sensitive keys kept private (never in Git)
- [ ] `render.yaml` checked for correct URLs
- [ ] Backend service deployed successfully
- [ ] Frontend service deployed successfully
- [ ] Test endpoints accessible from browser
- [ ] Admin login works with admin email

---

## Quick Verification After Deployment

### Check Backend Health
```bash
curl https://career-assessment-backend.onrender.com/api/health
# Response: {"status": "ok", "service": "digital-skills-assessment-api"}
```

### Check Database Connection
```bash
# In backend service logs, look for:
# "Application startup complete"
# If you see database connection errors, check DATABASE_URL
```

### Test Login
1. Go to frontend: https://career-assessment-frontend.onrender.com/login
2. Click Sign Up
3. Use email: olalekanquadri58@gmail.com (your admin email)
4. You should get admin privileges automatically
5. You should see "Admin" link in navbar

### Test Admin Dashboard
1. Go to /admin
2. Should see assessment results table
3. CSV/PDF export buttons should work

---

## Troubleshooting Variables

### Backend won't start
```
Check logs:
1. DATABASE_URL format: postgresql://user:pass@host:port/dbname
2. SECRET_KEY: Should be set (not empty)
3. ENVIRONMENT: Should be "production"
```

### CORS errors in browser
```
Check:
1. FRONTEND_URL matches your frontend service URL exactly
2. Backend service was restarted after FRONTEND_URL change
```

### Emails not sending
```
Check:
1. BREVO_API_KEY is set (not empty)
2. EMAIL_FROM_ADDRESS matches Brevo verified sender
3. Backend logs for API errors
```

### Admin access denied
```
Check:
1. ADMIN_EMAILS contains your email exactly
2. Case doesn't matter but spelling must match
3. Sign up with exact email from ADMIN_EMAILS
4. Clear browser cache after sign up
```

---

## Security Best Practices

✅ **DO:**
- Keep SECRET_KEY secret and random
- Use PostgreSQL (not SQLite) in production
- Rotate API keys regularly
- Use test keys for testing, live keys for production
- Store credentials in Render environment variables (not Git)

❌ **DON'T:**
- Commit .env file to Git
- Use same SECRET_KEY across environments
- Hardcode API keys in code
- Share SECRET_KEY or database credentials
- Use weak/simple SECRET_KEY values

---

## File Locations in Deploy

When deployed to Render, the structure is:

```
/opt/render/project/src/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py      ← Reads env variables here
│   │   ├── database.py
│   │   └── ...
│   ├── requirements.txt
│   └── .env               ← NOT uploaded (Render provides via dashboard)
├── frontend/
│   ├── src/
│   ├── package.json
│   └── .env.local         ← Generated from VITE_API_URL
└── render.yaml            ← Service configuration
```

Environment variables are injected by Render at runtime, not from .env files.

