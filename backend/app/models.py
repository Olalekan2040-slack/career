import uuid
from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    JSON,
    String,
)
from sqlalchemy.orm import relationship

from .database import Base


def gen_id() -> str:
    return uuid.uuid4().hex


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=gen_id)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    leads = relationship("Lead", back_populates="user")


class Lead(Base):
    __tablename__ = "leads"

    id = Column(String, primary_key=True, default=gen_id)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, index=True)
    consent_given = Column(Boolean, default=False)
    user_id = Column(String, ForeignKey("users.id"), nullable=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="leads")
    responses = relationship("AssessmentResponse", back_populates="lead")
    consultations = relationship("Consultation", back_populates="lead")


class AssessmentResponse(Base):
    __tablename__ = "assessment_responses"

    id = Column(String, primary_key=True, default=gen_id)
    lead_id = Column(String, ForeignKey("leads.id"), nullable=False)
    answers = Column(JSON, nullable=False)
    submitted_at = Column(DateTime, default=datetime.utcnow)

    lead = relationship("Lead", back_populates="responses")
    result = relationship("Result", back_populates="response", uselist=False)


class Result(Base):
    __tablename__ = "results"

    id = Column(String, primary_key=True, default=gen_id)
    response_id = Column(String, ForeignKey("assessment_responses.id"), nullable=False)
    primary_category = Column(String, nullable=False)
    secondary_category = Column(String, nullable=False)
    scores = Column(JSON, nullable=False)
    track = Column(String, nullable=False)
    close_call = Column(Boolean, default=False)
    unlocked = Column(Boolean, default=False)
    free_email_sent = Column(Boolean, default=False)
    paid_email_sent = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    response = relationship("AssessmentResponse", back_populates="result")
    payments = relationship("Payment", back_populates="result")


class Payment(Base):
    __tablename__ = "payments"

    id = Column(String, primary_key=True, default=gen_id)
    result_id = Column(String, ForeignKey("results.id"), nullable=False)
    provider = Column(String, nullable=False)  # stripe | paystack
    amount = Column(Float, nullable=False)
    currency = Column(String, nullable=False)
    status = Column(String, default="pending")  # pending | success | failed
    provider_reference = Column(String, nullable=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    result = relationship("Result", back_populates="payments")


class Consultation(Base):
    __tablename__ = "consultations"

    id = Column(String, primary_key=True, default=gen_id)
    lead_id = Column(String, ForeignKey("leads.id"), nullable=False)
    preferred_time = Column(String, nullable=True)
    note = Column(String, nullable=True)
    status = Column(String, default="requested")
    created_at = Column(DateTime, default=datetime.utcnow)

    lead = relationship("Lead", back_populates="consultations")


class WaitlistEntry(Base):
    """Tracks users waiting on a not-yet-launched category's curriculum (Phase 2/3)."""

    __tablename__ = "waitlist_entries"

    id = Column(String, primary_key=True, default=gen_id)
    email = Column(String, nullable=False, index=True)
    category_key = Column(String, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
