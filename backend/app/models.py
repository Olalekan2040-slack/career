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
    is_admin = Column(Boolean, default=False, nullable=False)
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

    # Intake / background context — used to branch question selection and to
    # decide whether an "advanced entry" career recommendation needs a caveat.
    # Only age_range, education_level, field_of_study, and tech_exposure feed
    # the logic; gender is optional and collected for reporting only.
    age_range = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    education_level = Column(String, nullable=True)
    field_of_study = Column(String, nullable=True)
    tech_exposure = Column(String, nullable=True)  # none | some | significant
    interest_area = Column(String, nullable=True)

    lead = relationship("Lead", back_populates="responses")
    result = relationship("Result", back_populates="response", uselist=False)


class Result(Base):
    __tablename__ = "results"

    id = Column(String, primary_key=True, default=gen_id)
    response_id = Column(String, ForeignKey("assessment_responses.id"), nullable=False)
    recommendations = Column(JSON, nullable=False)  # ranked list of {career_key, score, reason}
    close_call = Column(Boolean, default=False)
    unlocked = Column(Boolean, default=False)  # True = 4 recommendations visible, False = 2
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
