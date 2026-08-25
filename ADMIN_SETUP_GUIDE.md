# Admin Dashboard Setup Guide

## Overview
A complete admin dashboard has been created for managing assessment results, viewing respondent data, and exporting reports in CSV and PDF formats.

## Features Implemented

### 1. Admin Authentication
- **Protected Admin Page**: Only users with admin credentials can access `/admin`
- **Email-based Access Control**: Admin email `olalekanquadri58@gmail.com` is auto-configured
- **Session Management**: Uses token-based authentication with 30-day expiry

### 2. Assessment Results Dashboard
Shows all respondents who have completed the assessment with:
- **Respondent Name & Email**
- **Submission Date**
- **Top 2 Career Recommendations** with scores
- Career details (duration, focus, etc.)

### 3. Data Export Capabilities
- **CSV Export**: Downloads as spreadsheet (.csv)
  - Columns: Name, Email, Date, Top Recommendation, Score, 2nd Recommendation, Score
  - File naming: `assessment-results-YYYY-MM-DD.csv`

- **PDF Export**: Professional PDF report (.pdf)
  - Title page with generation date
  - Formatted table with all results
  - Summary statistics
  - File naming: `assessment-results-YYYY-MM-DD.pdf`

### 4. Admin Respondents View
Lists all registered users with name, email, and registration date

## Setup Instructions

### Step 1: Backend Configuration (Already Done)
The `.env` file is pre-configured with:
```
ADMIN_EMAILS=olalekanquadri58@gmail.com
```

### Step 2: Frontend Dependencies (Already Done)
Required packages have been installed:
- `jspdf`: PDF generation library
- `jspdf-autotable`: PDF table formatting

### Step 3: Create Admin Account

**Option A: Using the Web Interface**
1. Go to `/login` page
2. Click "Sign up" or navigate to registration
3. Enter:
   - Name: Any name (e.g., "Admin User")
   - Email: `olalekanquadri58@gmail.com`
   - Password: `Asmaa@2019`
4. The system automatically grants admin privileges to this email
5. After login, you'll be redirected to `/admin` and see "Admin" link in navbar

**Option B: Using Backend/Database**
If you need to create the admin account programmatically:
```python
from app.auth import hash_password
from app.models import User
from app.database import SessionLocal

db = SessionLocal()
user = User(
    name="Admin",
    email="olalekanquadri58@gmail.com",
    password_hash=hash_password("Asmaa@2019"),
    is_admin=True
)
db.add(user)
db.commit()
```

## Accessing the Admin Dashboard

### Login Flow
1. Navigate to `/login`
2. Enter credentials:
   - Email: `olalekanquadri58@gmail.com`
   - Password: `Asmaa@2019`
3. Click "Log in"
4. If login successful:
   - Redirected to `/admin` dashboard
   - "Admin" link visible in navbar
   - All respondent data displays

### Dashboard Tabs

#### Assessment Results Tab (Default)
- Shows all respondents who completed the assessment
- Displays top 2 recommendations with scores
- Shows submission date
- **Export Buttons:**
  - "📥 Export CSV" - Downloads spreadsheet
  - "📄 Export PDF" - Downloads professional report

#### All Respondents Tab
- Shows all registered users (those who started but may not have completed)
- Lists name, email, registration date
- Useful for identifying engaged vs. inactive users

## API Endpoints

### Admin Assessment Results
```
GET /api/admin/assessment-results
Authorization: Bearer {token}
```
Returns:
```json
[
  {
    "result_id": "...",
    "lead_name": "John Doe",
    "lead_email": "john@example.com",
    "submitted_at": "2024-01-15T10:30:00",
    "close_call": false,
    "recommendations": [
      {
        "rank": 1,
        "score": 85.5,
        "reason": "Strong match for...",
        "career": {
          "key": "data-science",
          "name": "Data Science",
          "focus": "...",
          "duration": "6-12 months",
          "curriculum": [...],
          "resources": [...]
        }
      }
    ]
  }
]
```

### Admin Leads
```
GET /api/admin/leads
Authorization: Bearer {token}
```

### Admin Users
```
GET /api/admin/users
Authorization: Bearer {token}
```

## Security Features

1. **Admin Verification**: `get_current_admin` middleware checks if user is admin
2. **Email Whitelist**: Only emails in `ADMIN_EMAILS` config get admin access
3. **Token Authentication**: All requests require valid Bearer token
4. **Session Expiry**: Tokens expire after 30 days

## Troubleshooting

### Issue: Cannot access admin dashboard
**Solution:**
1. Verify email is exactly: `olalekanquadri58@gmail.com` (case-insensitive)
2. Check `.env` file has correct `ADMIN_EMAILS` setting
3. Ensure user account exists and `is_admin=True` in database
4. Clear browser cache and localStorage (F12 → Application → Clear)

### Issue: Export buttons not working
**Solution:**
1. Check browser console for errors (F12 → Console)
2. Ensure jsPDF and jspdf-autotable are installed: `npm install --legacy-peer-deps`
3. Verify assessment results exist in database
4. Check browser allows downloads

### Issue: No assessment results showing
**Solution:**
1. Ensure respondents have completed assessments (not just registered)
2. Check database for `assessment_responses` and `results` entries
3. Verify SQL JOIN queries in admin router are correct

## Customization Options

### Change Admin Email
Edit `.env`:
```
ADMIN_EMAILS=newemail@example.com
```
Or use comma-separated for multiple admins:
```
ADMIN_EMAILS=admin1@example.com,admin2@example.com
```

### Modify PDF Report Format
Edit `frontend/src/pages/Admin.jsx` in `exportToPDF()` function:
- Change colors: `backgroundColor: [41, 128, 185]`
- Adjust margins: `margin: { top: 35, right: 10, bottom: 10, left: 10 }`
- Modify table columns: Update `head` array in `doc.autoTable()`

### Add More Columns
Update the table in Admin.jsx to include:
- Age range, education level, tech exposure (from intake)
- Payment status
- Consultation booking status
- Custom fields from the assessment response

## Files Modified/Created

### Backend
- `app/schemas.py` - Added `AdminAssessmentResultOut`
- `app/routers/admin.py` - Added `/api/admin/assessment-results` endpoint

### Frontend
- `src/pages/Admin.jsx` - Complete rewrite with export functionality
- `package.json` - Added jspdf, jspdf-autotable dependencies
- `src/api/client.js` - Added `getAdminAssessmentResults()` method

## Next Steps

1. **Test Admin Access**: Create account and verify login works
2. **Test Export**: Submit assessments and verify CSV/PDF export
3. **Customize**: Modify styling, columns, or branding as needed
4. **Deploy**: Push changes to production environment
5. **Monitor**: Track admin access logs and export usage

---

**Questions?** Check browser console (F12) for detailed error messages.
