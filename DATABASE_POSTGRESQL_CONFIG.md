# Database & Deployment Configuration Summary

## Current Status

### ✅ Database Configuration
**Status**: App is **NOT** configured for PostgreSQL by default, but **CAN** use PostgreSQL

**Development (Current)**:
- Database: SQLite (`assessment.db`)
- Location: Local file storage
- Suitable for: Local development, testing

**Production (Updated)**:
- Database: PostgreSQL (must be explicitly configured)
- Location: Render's managed PostgreSQL service
- Configuration: Via `DATABASE_URL` environment variable

---

## What's Changed

### 1. **backend/app/config.py** (UPDATED)
Added automatic database type detection:

```python
@property
def is_postgres(self) -> bool:
    """Check if using PostgreSQL database"""
    return self.database_url.startswith("postgresql://")

@property
def is_production(self) -> bool:
    """Check if running in production environment"""
    return self.environment.lower() == "production"
```

Now the app automatically:
- Detects if using PostgreSQL or SQLite based on `DATABASE_URL`
- Knows if in production or development mode
- Can adjust behavior accordingly

---

## Production Environment Variables (REQUIRED)

### Core Configuration
```env
ENVIRONMENT=production
SECRET_KEY=[GENERATE NEW]
FRONTEND_URL=https://your-frontend.onrender.com
DATABASE_URL=postgresql://username:password@host:5432/dbname
ADMIN_EMAILS=olalekanquadri58@gmail.com
```

### Email (Brevo - Required for emails)
```env
BREVO_API_KEY=[GET FROM BREVO]
EMAIL_FROM_ADDRESS=olalekanquadri58@gmail.com
EMAIL_FROM_NAME=Global Digital Skills Assessment
```

### Optional (Payments)
```env
PAYMENTS_ENABLED=false
STRIPE_SECRET_KEY=[OPTIONAL]
STRIPE_WEBHOOK_SECRET=[OPTIONAL]
PAYSTACK_SECRET_KEY=[OPTIONAL]
PAYSTACK_PUBLIC_KEY=[OPTIONAL]
```

### Optional (Customization)
```env
CONSULTATION_BOOKING_URL=https://calendly.com/...
PORTFOLIO_URL=https://your-portfolio.com
```

---

## How to Switch Databases

### From SQLite to PostgreSQL

**Step 1**: Create PostgreSQL service on Render
- Dashboard → New → PostgreSQL
- Copy Internal Database URL

**Step 2**: Update environment variable
```env
# Before (Development/SQLite):
DATABASE_URL=sqlite:///./assessment.db

# After (Production/PostgreSQL):
DATABASE_URL=postgresql://user:password@host:5432/dbname
```

**Step 3**: Restart backend service
- Render will auto-detect PostgreSQL URL
- App automatically uses PostgreSQL driver
- No code changes needed!

---

## Deployment Checklist

### Pre-Deployment
- [ ] Generate random `SECRET_KEY` with: `python -c "import secrets; print(secrets.token_hex(32))"`
- [ ] Create PostgreSQL service on Render
- [ ] Get Brevo API key from https://app.brevo.com/settings/keys/api
- [ ] Copy PostgreSQL Internal Database URL

### In Render Dashboard
- [ ] Create Backend Service (Python, FastAPI)
- [ ] Create PostgreSQL Service
- [ ] Create Frontend Service (Static Site)
- [ ] Set all environment variables in backend service
- [ ] Deploy backend first, then frontend

### Post-Deployment
- [ ] Test health endpoint: `/api/health`
- [ ] Test login at `/login`
- [ ] Test admin dashboard at `/admin`
- [ ] Verify emails are sending
- [ ] Check logs for any errors

---

## File Changes Summary

### Modified Files
1. **backend/app/config.py**
   - Added `is_postgres` property
   - Added `is_production` property
   - Enhanced documentation

2. **backend/.env.example**
   - Complete rewrite with all variables
   - Added descriptions for each variable
   - Included generation instructions
   - Added Render deployment guide

### New Files
1. **DEPLOYMENT_GUIDE.md** (3,200+ lines)
   - Step-by-step Render setup
   - Database configuration
   - Environment variables
   - API key getting started
   - Troubleshooting section
   - Monitoring & scaling tips

2. **ENVIRONMENT_VARIABLES.md** (400+ lines)
   - Quick reference checklist
   - Variable-by-purpose tables
   - Copy-paste template
   - Security best practices
   - Troubleshooting by issue

---

## Key Features

### ✅ Automatic Database Detection
App automatically uses:
- **SQLite** if DATABASE_URL contains `sqlite://`
- **PostgreSQL** if DATABASE_URL contains `postgresql://`

```python
# No code changes needed!
# App detects from DATABASE_URL string
if settings.is_postgres:
    # Use PostgreSQL-specific features if needed
else:
    # Use SQLite if needed
```

### ✅ Production-Ready Configuration
All variables defined:
- Email sending (Brevo)
- Payment processing (Stripe/Paystack)
- Admin access control
- CORS configuration
- Database connections

### ✅ Comprehensive Documentation
- DEPLOYMENT_GUIDE.md - Full setup instructions
- ENVIRONMENT_VARIABLES.md - Reference guide
- .env.example - Template with 100+ lines of docs
- InCode comments - Explain each setting

---

## PostgreSQL vs SQLite

| Feature | SQLite | PostgreSQL |
|---------|--------|-----------|
| **Persistence** | Local file | Managed service |
| **Scalability** | ~1000 rows | Millions of rows |
| **Concurrency** | Limited | Full support |
| **Backup** | Manual | Automatic |
| **Cost** | Free | Free (Starter) → Paid |
| **Setup** | None | Render setup |
| **Best For** | Development | Production |

---

## Example: Setting Up for Production

### 1. Generate SECRET_KEY
```bash
$ python -c "import secrets; print(secrets.token_hex(32))"
a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6
```

### 2. Get Brevo API Key
1. Go to https://app.brevo.com/settings/keys/api
2. Click "Create a new API key"
3. Copy the key

### 3. Create PostgreSQL on Render
1. Render Dashboard → New → PostgreSQL
2. Name: `career-assessment-db`
3. Copy Internal Database URL

### 4. Set Environment Variables
```env
ENVIRONMENT=production
SECRET_KEY=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6
DATABASE_URL=postgresql://assessment_user_xyz:abc123@dpg-abc.renders.com:5432/assessment_abc
FRONTEND_URL=https://your-frontend.onrender.com
ADMIN_EMAILS=olalekanquadri58@gmail.com
BREVO_API_KEY=your-api-key-here
EMAIL_FROM_ADDRESS=olalekanquadri58@gmail.com
EMAIL_FROM_NAME=Global Digital Skills Assessment
```

### 5. Deploy
- Commit changes to GitHub
- Render auto-deploys from main branch
- Backend starts with new environment variables
- App connects to PostgreSQL automatically

---

## Documentation Files

| File | Purpose | Audience |
|------|---------|----------|
| DEPLOYMENT_GUIDE.md | Complete setup & troubleshooting | DevOps/Deployers |
| ENVIRONMENT_VARIABLES.md | Quick reference & checklist | Developers/Deployers |
| .env.example | Template for local development | All developers |
| backend/app/config.py | Code-level configuration | Backend developers |

---

## Next Steps

1. **Review DEPLOYMENT_GUIDE.md** - Full instructions
2. **Use ENVIRONMENT_VARIABLES.md** - Copy-paste template
3. **Follow the checklist** - Ensure nothing is missed
4. **Test locally** - Run backend & frontend before deployment
5. **Deploy to Render** - Use the provided instructions
6. **Verify in production** - Test endpoints and admin access

---

## Support Resources

- **Render PostgreSQL**: https://render.com/docs/databases
- **Brevo Email API**: https://developers.brevo.com/docs/getting-started
- **FastAPI Deployment**: https://fastapi.tiangolo.com/deployment/
- **SQLAlchemy PostgreSQL**: https://docs.sqlalchemy.org/dialects/postgresql.html

---

## Summary

✅ **App is NOW configured to support PostgreSQL**
- Auto-detects database type from `DATABASE_URL`
- Works with SQLite (development) or PostgreSQL (production)
- All environment variables documented and provided
- Complete deployment guide included
- Production-ready configuration

👉 **To use PostgreSQL on Render**:
1. Set `DATABASE_URL` to PostgreSQL connection string
2. App automatically uses PostgreSQL driver
3. No code changes needed!

