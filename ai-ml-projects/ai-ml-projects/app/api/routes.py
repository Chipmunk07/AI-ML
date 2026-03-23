from fastapi import APIRouter

from app.core.config import settings
from app.models.schemas import AnswerRequest, AnswerResponse, HealthResponse
from app.services.generator import generate_response

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(
        status="ok",
        app=settings.app_name,
        environment=settings.app_env,
    )


@router.post("/answer", response_model=AnswerResponse)
def answer_question(payload: AnswerRequest) -> AnswerResponse:
    response = generate_response(payload.question)
    return AnswerResponse(**response)
