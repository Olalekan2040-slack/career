from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .config import settings
from .database import Base, engine
from .routers import admin, auth, checkout, consultation, dashboard, leads, meta, questions, result, submit, webhooks

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Global Digital Skills Career Assessment API", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url, "http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(dashboard.router)
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
