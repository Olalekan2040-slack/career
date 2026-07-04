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
    is_admin: bool = False

    class Config:
        from_attributes = True


class AdminUserOut(BaseModel):
    id: str
    name: str
    email: str
    is_admin: bool
    created_at: datetime

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


class AdminLeadOut(BaseModel):
    id: str
    name: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True


class QuestionOptionOut(BaseModel):
    key: str
    text: str
    hint: Optional[str] = None


class LikertQuestionOut(BaseModel):
    id: str
    text: str


class ChoiceQuestionOut(BaseModel):
    id: str
    text: str
    options: list[QuestionOptionOut]


class RankingQuestionOut(BaseModel):
    id: str
    text: str
    items: list[QuestionOptionOut]


class QuestionSetOut(BaseModel):
    likert: list[LikertQuestionOut]
    forced_choice: list[ChoiceQuestionOut]
    scenario: list[ChoiceQuestionOut]
    situational: list[ChoiceQuestionOut]
    ranking: list[RankingQuestionOut]


class AssessmentAnswers(BaseModel):
    likert: dict[str, int] = Field(default_factory=dict)
    forced_choice: dict[str, str] = Field(default_factory=dict)
    scenario: dict[str, str] = Field(default_factory=dict)
    situational: dict[str, str] = Field(default_factory=dict)
    ranking: dict[str, list[str]] = Field(default_factory=dict)


class IntakeAnswers(BaseModel):
    age_range: Optional[str] = None
    gender: Optional[str] = None
    education_level: Optional[str] = None
    field_of_study: Optional[str] = None
    tech_exposure: Optional[str] = None
    interest_area: Optional[str] = None


class IntakeOptionOut(BaseModel):
    key: str
    label: str


class IntakeFieldOut(BaseModel):
    key: str
    label: str
    required: bool
    options: list[IntakeOptionOut]


class NextQuestionRequest(BaseModel):
    intake: IntakeAnswers = Field(default_factory=IntakeAnswers)
    answers: AssessmentAnswers = Field(default_factory=AssessmentAnswers)
    skipped_ids: list[str] = Field(default_factory=list)
    elapsed_seconds: float = 0


class NextQuestionOut(BaseModel):
    section: str
    question: dict


class NextQuestionResponse(BaseModel):
    done: bool
    total_answered: int
    next: Optional[NextQuestionOut] = None


class SubmitRequest(BaseModel):
    lead_id: str
    intake: IntakeAnswers = Field(default_factory=IntakeAnswers)
    answers: AssessmentAnswers


class CareerOut(BaseModel):
    key: str
    name: str
    focus: str
    duration: str
    curriculum: list[str]
    resources: list[str]


class RecommendationOut(BaseModel):
    rank: int
    score: float
    reason: str
    entry_note: Optional[str] = None
    career: CareerOut


class ResultOut(BaseModel):
    id: str
    unlocked: bool
    visible_count: int
    close_call: bool
    close_call_message: Optional[str] = None
    recommendations: list[RecommendationOut]


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
