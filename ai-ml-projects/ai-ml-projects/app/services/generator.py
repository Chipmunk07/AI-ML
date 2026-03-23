from app.services.retriever import retrieve_answer


def generate_response(question: str) -> dict:
    result = retrieve_answer(question)
    return {
        "question": question,
        "matched_topic": result.topic,
        "answer": result.answer,
        "confidence": result.confidence,
    }
