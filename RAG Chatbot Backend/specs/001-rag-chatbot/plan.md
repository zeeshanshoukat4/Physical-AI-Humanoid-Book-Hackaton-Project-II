# Implementation Plan: Integrated RAG Chatbot for Published Book

**Branch**: `001-rag-chatbot` | **Date**: 2025-12-15 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-rag-chatbot/spec.md`

## Summary

This plan outlines the technical approach for building and deploying a fully functional RAG (Retrieval-Augmented Generation) chatbot. The chatbot will be embedded in a book's website to provide context-aware answers based on user-selected text. The core technologies to be used are FastAPI for the backend, Neon Serverless Postgres for data and log storage, Qdrant for vector search, and the Chore API for embeddings and text generation.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: FastAPI, Uvicorn, SQLAlchemy, psycopg2-binary, qdrant-client, httpx
**Storage**: Neon Serverless Postgres, Qdrant Cloud Free Tier
**Testing**: pytest
**Target Platform**: Linux server (for backend deployment)
**Project Type**: Web application (backend service)
**Performance Goals**: <= 2 seconds p95 latency for all queries.
**Constraints**: Must use Chore API for embeddings and generation; no OpenAI. All answers must be strictly derived from the book's content.
**Scale/Scope**: The initial scope is to support a single book's content and a moderate number of concurrent users.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Accuracy**: All answers are derived from retrieved text chunks, no external knowledge is used.
- **Relevance**: Retrieval is based on user-selected text, ensuring high relevance.
- **Efficiency**: Caching strategies and optimized queries will be used to meet the <= 2s response time.
- **Security**: All API keys and credentials will be stored as environment variables on the backend, never exposed to the frontend.
- **Usability**: The frontend integration will be handled by the Gemini CLI + SpecificallyKit Plus team.

## Project Structure

### Documentation (this feature)

```text
specs/001-rag-chatbot/
├── plan.md              # This file
├── research.md          # Research on best practices
├── data-model.md        # Data models for Postgres
├── quickstart.md        # Guide to run the backend
├── contracts/           # OpenAPI specification
└── tasks.md             # Implementation tasks
```

### Source Code (repository root)

```text
# Web application (backend only)
backend/
├── src/
│   ├── models/          # SQLAlchemy models
│   ├── services/        # Business logic for retrieval and generation
│   ├── api/             # FastAPI endpoints
│   └── core/            # Configuration and core settings
└── tests/
    ├── integration/
    └── unit/
```

**Structure Decision**: A dedicated `backend` directory will be created to house the FastAPI application, separating it from any potential frontend code in the future.

## Complexity Tracking

No violations of the constitution are anticipated.
