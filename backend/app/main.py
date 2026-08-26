from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .config import settings
from .database import Base, engine
from .routers import (
    admin,
    assessment,
    auth,
    checkout,
    consultation,
    leads,
    meta,
    questions,
    result,
    submit,
    webhooks,
)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Global Digital Skills Career Assessment API", version="2.0.0")

# CORS configuration — allow frontend service to access API
# In development: localhost:5173
# In production (Render): frontend service URL from FRONTEND_URL env variable
cors_origins = [
    settings.frontend_url,  # Production frontend URL (from env)
    "http://localhost:5173",  # Local development
    "http://127.0.0.1:5173",  # Local development (loopback)
]

# In production, also allow requests with onrender.com domain (for Render deployments)
if settings.is_production and "onrender.com" not in settings.frontend_url:
    # Fallback for Render if FRONTEND_URL not properly set
    cors_origins.append("*")

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(assessment.router)
app.include_router(meta.router)
app.include_router(leads.router)
app.include_router(questions.router)
app.include_router(submit.router)
app.include_router(result.router)
app.include_router(checkout.router)
app.include_router(webhooks.router)
app.include_router(consultation.router)


@app.get("/")
@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "digital-skills-assessment-api"}
