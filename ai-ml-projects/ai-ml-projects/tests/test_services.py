from app.services.generator import generate_response
from app.services.retriever import retrieve_answer


def test_retrieve_answer_password_topic():
    result = retrieve_answer("How do I reset my password?")
    assert result.topic == "password"
    assert result.confidence > 0.9


def test_generate_response_general_fallback():
    result = generate_response("Tell me something unrelated")
    assert result["matched_topic"] == "general"
    assert 0.0 <= result["confidence"] <= 1.0
