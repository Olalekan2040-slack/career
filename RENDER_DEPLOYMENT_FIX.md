# Render Deployment - "Failed to Fetch" Fix Guide

## Issue Summary
You're getting "failed to fetch" errors when testing your deployed Render app because:
1. **Backend URL mismatch** in `render.yaml`
2. **CORS configuration** too restrictive
3. **Frontend URL** not correctly set in backend

---

## What Was Fixed

### 1. ✅ Updated Backend URL in render.yaml
**Changed:**
```yaml
# OLD (incorrect):
VITE_API_URL: https://career-assessment-backend-a0xc.onrender.com

# NEW (correct):
VITE_API_URL: https://career-assessment-backend-y2zu.onrender.com
```

### 2. ✅ Improved CORS Configuration
**Changed:**
- Now dynamically includes `FRONTEND_URL` from environment
- Works with both localhost and Render URLs
- Better error handling for production

### 3. ✅ Backend Environment Variable
Ensure this is set in Render dashboard:
```
FRONTEND_URL=https://career-assessment-frontend.onrender.com
```
(Replace with your actual frontend URL)

---

## How to Fix Completely

### Step 1: Find Your Actual Frontend URL
1. Go to Render Dashboard
2. Click on `career-assessment-frontend` service
3. Copy the URL from the top (format: `https://xxxx.onrender.com`)
4. Note this down

### Step 2: Update Backend Environment Variables

Go to your **backend service** in Render Dashboard and verify:

| Variable | Value | Where to Find |
|----------|-------|---------------|
| `FRONTEND_URL` | Your frontend URL from Step 1 | Dashboard |
| `VITE_API_URL` | Your backend URL | Your service URL |
| `ENVIRONMENT` | `production` | Fixed in render.yaml |

**Example:**
```
Frontend URL: https://career-assessment-frontend-abc123.onrender.com
Backend URL: https://career-assessment-backend-y2zu.onrender.com

FRONTEND_URL=https://career-assessment-frontend-abc123.onrender.com
VITE_API_URL=https://career-assessment-backend-y2zu.onrender.com
```

### Step 3: Redeploy
After updating environment variables:

**Option A: Trigger redeploy in Render**
1. Go to backend service
2. Click "Redeploy"
3. Wait for deployment to complete

**Option B: Push to GitHub (auto-deploy)**
```bash
cd /path/to/Tech_Career
git add render.yaml backend/app/main.py
git commit -m "fix: Update backend URL and improve CORS configuration for Render"
git push origin main
```

---

## Testing After Fix

### 1. Test Backend Health
```bash
curl https://career-assessment-backend-y2zu.onrender.com/api/health
# Expected response:
# {"status": "ok", "service": "digital-skills-assessment-api"}
```

### 2. Test Frontend Access
1. Open frontend URL in browser
2. Should load without errors
3. Check browser console (F12) for any CORS errors

### 3. Test Login Flow
1. Go to `/login` page
2. Try signing up with: `olalekanquadri58@gmail.com`
3. Password: `Asmaa@2019`
4. Should redirect to `/admin` after login
5. Admin dashboard should load

### 4. Check Browser Console
Press **F12** → **Console** tab and look for:
- ✅ No CORS errors
- ✅ API calls showing successful (200 status)
- ✅ Network tab shows requests to correct backend URL

---

## Common Issues & Solutions

### Issue 1: Still Getting CORS Error
**Symptom:** `Access to XMLHttpRequest has been blocked by CORS policy`

**Solution:**
1. Check FRONTEND_URL in backend environment matches frontend service URL exactly
2. Ensure no typos in URLs
3. Redeploy backend service: Dashboard → Backend → Redeploy
4. Clear browser cache: Ctrl+Shift+Delete

### Issue 2: 404 on API Endpoints
**Symptom:** `GET https://backend-url/api/auth/me 404 (Not Found)`

**Solution:**
1. Verify backend is running: Check backend logs in Render
2. Ensure database is connected (check DATABASE_URL)
3. Check application startup logs for errors

### Issue 3: Database Connection Failed
**Symptom:** Errors in backend logs about database

**Solution:**
1. Verify DATABASE_URL is set in backend environment
2. Use PostgreSQL Internal Database URL (not External)
3. Check PostgreSQL service is "Available" in Render
4. Restart backend service

### Issue 4: Frontend Says "Could not load respondents"
**Symptom:** Admin dashboard shows error messages

**Solution:**
1. Check backend health endpoint first
2. Verify authentication token is valid
3. Check browser console for API errors
4. Ensure ADMIN_EMAILS contains your email

---

## Environment Variables Checklist

### Required for Render Production

- [ ] `ENVIRONMENT=production`
- [ ] `SECRET_KEY=[generated value]`
- [ ] `DATABASE_URL=[PostgreSQL Internal URL]`
- [ ] `FRONTEND_URL=[Your frontend URL]`
- [ ] `ADMIN_EMAILS=olalekanquadri58@gmail.com`
- [ ] `BREVO_API_KEY=[Your Brevo API key]`
- [ ] `EMAIL_FROM_ADDRESS=olalekanquadri58@gmail.com`

### For Frontend

- [ ] `VITE_API_URL=[Your backend URL]` (Updated in render.yaml)

### Verify in Render Dashboard

Go to backend service → Settings → Environment Variables:
```
✓ All variables set (no empty ones)
✓ No typos in URLs
✓ Backend URL ends with .onrender.com
✓ Frontend URL ends with .onrender.com
✓ DATABASE_URL starts with postgresql://
```

---

## Files Changed

### Updated
- `render.yaml` - Fixed `VITE_API_URL` and added deployment instructions
- `backend/app/main.py` - Improved CORS configuration

### How to Apply Changes

**Option 1: Using Git** (Recommended)
```bash
cd c:\Users\DELL\Desktop\Tech_Career
git add render.yaml backend/app/main.py
git commit -m "fix: Update backend URL and improve CORS for Render deployment"
git push origin main
# Render auto-deploys from main branch
```

**Option 2: Manual Render Dashboard Update**
1. Backend Service → Environment Variables
2. Update `FRONTEND_URL` to match your frontend service URL
3. Click "Save Changes"
4. Render auto-redeploys

---

## Debugging Steps

If still having issues, follow this order:

### 1. Check Backend is Running
```bash
curl -i https://career-assessment-backend-y2zu.onrender.com/api/health
# Should return 200 OK with JSON response
```

### 2. Check Backend Logs
1. Render Dashboard → Backend Service
2. Click "Logs" tab
3. Look for errors during startup
4. Look for CORS-related warnings

### 3. Check Frontend Network Requests
1. Open frontend in browser
2. Press F12 → Network tab
3. Try to login or access admin
4. Look at failed requests (red X)
5. Check response headers for CORS errors

### 4. Verify Environment Variables
1. Backend service → Settings → Environment
2. Make sure all required variables are set
3. No empty values for required variables
4. URLs don't have trailing slashes (usually)

### 5. Clear Everything and Redeploy
```bash
# Hard redeploy backend:
# 1. Go to backend service
# 2. Click "Clear Build Cache"
# 3. Click "Redeploy"
# 4. Wait for full rebuild

# Or push new commit:
git add .
git commit -m "chore: trigger redeploy"
git push origin main
```

---

## Key Points

✅ **Backend URL**: Must match `VITE_API_URL` in frontend environment
✅ **Frontend URL**: Must match `FRONTEND_URL` in backend environment
✅ **CORS**: Automatically allows both localhost and Render URLs
✅ **Database**: PostgreSQL Internal URL (not External)
✅ **Redeploy**: After changing environment variables, backend redeployments are automatic

---

## Next Steps

1. **Push the updated files** (if not already done):
   ```bash
   git push origin main
   ```

2. **Wait for Render to deploy** (~2 minutes)

3. **Test again**:
   - Visit frontend URL
   - Try login/signup
   - Check admin dashboard
   - Check browser console for errors

4. **If still having issues**:
   - Check backend logs in Render
   - Verify all environment variables are set
   - Try manual redeploy from Render dashboard

---

## Quick Reference

| Component | URL |
|-----------|-----|
| Frontend | https://career-assessment-frontend-[xxx].onrender.com |
| Backend | https://career-assessment-backend-y2zu.onrender.com |
| Health Check | https://career-assessment-backend-y2zu.onrender.com/api/health |
| Login | https://career-assessment-frontend-[xxx].onrender.com/login |
| Admin | https://career-assessment-frontend-[xxx].onrender.com/admin |

Replace `[xxx]` with your actual frontend service ID from Render.

