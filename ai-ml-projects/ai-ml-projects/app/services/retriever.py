from dataclasses import dataclass


@dataclass(frozen=True)
class RetrievalResult:
    topic: str
    answer: str
    confidence: float


KNOWLEDGE_BASE = {
    "password": "To reset your password, go to the sign-in page and select 'Forgot password'.",
    "billing": "Billing questions can be handled from the account settings and invoices page.",
    "deployment": "Deployments should pass tests, build successfully, and include rollback notes.",
    "api": "API requests should be validated, logged appropriately, and return clear status codes.",
}


def retrieve_answer(question: str) -> RetrievalResult:
    normalized = question.lower()

    for topic, answer in KNOWLEDGE_BASE.items():
        if topic in normalized:
            return RetrievalResult(topic=topic, answer=answer, confidence=0.93)

    return RetrievalResult(
        topic="general",
        answer="I could not find an exact match, but I would route this to a fallback workflow or human review.",
        confidence=0.51,
    )
