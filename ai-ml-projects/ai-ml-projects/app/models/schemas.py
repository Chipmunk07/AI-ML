from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str
    app: str
    environment: str


class AnswerRequest(BaseModel):
    question: str = Field(..., min_length=3, max_length=500)


class AnswerResponse(BaseModel):
    question: str
    matched_topic: str
    answer: str
    confidence: float
