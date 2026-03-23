# AI/ML Project

A production-style Python repository that demonstrates sound software engineering practices using FastAPI, modular service layers, tests, containerization, and CI.

## What this repo shows
- Clean Python project structure
- FastAPI backend with typed request/response models
- Service-oriented design
- Deterministic "retrieval + response" demo endpoint
- Unit and API tests with `pytest`
- Docker support
- GitHub Actions CI workflow
- Environment-based configuration

## Project structure

```text
ai-ml-projects-template/
├── app/
│   ├── api/
│   │   └── routes.py
│   ├── core/
│   │   └── config.py
│   ├── models/
│   │   └── schemas.py
│   ├── services/
│   │   ├── generator.py
│   │   └── retriever.py
│   └── main.py
├── tests/
│   ├── test_api.py
│   └── test_services.py
├── .github/workflows/ci.yml
├── .env.example
├── Dockerfile
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Quick start

### 1) Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Run locally
```bash
uvicorn app.main:app --reload
```

API docs:
- Swagger UI: `http://127.0.0.1:8000/docs`
- Health: `http://127.0.0.1:8000/health`

## Example request
```bash
curl -X POST "http://127.0.0.1:8000/answer" \
  -H "Content-Type: application/json" \
  -d '{"question": "How do I reset my password?"}'
```

## Run tests
```bash
pytest -q
```

## Docker
```bash
docker build -t ai-ml-projects-template .
docker run -p 8000:8000 ai-ml-projects-template
```

## Why this works for applications
This repo is intentionally small, but it demonstrates the habits hiring teams care about:
- separation of concerns
- configuration management
- typed schemas
- test coverage
- CI/CD readiness
- reproducible local/dev environments

## Suggested GitHub repo names
- `ai-ml-projects`
- `python-ai-service-template`
- `rag-fastapi-starter`
- `ml-backend-engineering-demo`
