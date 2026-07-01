from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class SignupRequest(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    email: EmailStr
    password: str = Field(min_length=8, max_length=200)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: str
    name: str
    email: str

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    user: UserOut


class LeadCreate(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    email: EmailStr
    consent_given: bool = True


class LeadOut(BaseModel):
    id: str
    name: str
    email: str

    class Config:
        from_attributes = True


class QuestionOptionOut(BaseModel):
    key: str
    text: str


class QuestionOut(BaseModel):
    id: str
    text: str
    options: list[QuestionOptionOut]


class QuestionSetOut(BaseModel):
    orientation: list[QuestionOut]
    track_a_deep_dive: list[QuestionOut]
    track_b_deep_dive: list[QuestionOut]


class SubmitRequest(BaseModel):
    lead_id: str
    orientation_answers: dict[str, str]
    deep_dive_answers: dict[str, str]


class CategoryOut(BaseModel):
    key: str
    name: str
    track: str
    focus: Optional[str] = None
    duration: Optional[str] = None
    phase_1: bool
    curriculum: Optional[list[str]] = None
    resources: Optional[list[str]] = None


class ResultOut(BaseModel):
    id: str
    track: str
    unlocked: bool
    close_call: bool
    close_call_message: Optional[str] = None
    primary: CategoryOut
    secondary: CategoryOut
    scores: dict[str, int]


class DashboardResultOut(ResultOut):
    created_at: datetime


class CheckoutRequest(BaseModel):
    result_id: str


class CheckoutResponse(BaseModel):
    checkout_url: str
    provider: str


class ConsultationCreate(BaseModel):
    lead_id: str
    preferred_time: Optional[str] = None
    note: Optional[str] = None


class ConsultationOut(BaseModel):
    id: str
    status: str

    class Config:
        from_attributes = True


class WaitlistJoin(BaseModel):
    email: EmailStr
    category_key: str
