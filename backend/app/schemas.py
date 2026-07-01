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


class SubmitRequest(BaseModel):
    lead_id: str
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
