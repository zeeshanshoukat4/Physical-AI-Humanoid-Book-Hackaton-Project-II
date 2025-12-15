---
description: "Task list for RAG Chatbot feature implementation"
---

# Tasks: Integrated RAG Chatbot for Published Book

**Input**: Design documents from `/specs/001-rag-chatbot/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)

## Path Conventions

- Paths shown below assume the `backend/` directory structure from `plan.md`.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Initialize FastAPI project in `backend/`
- [ ] T002 Create directory structure `backend/src/{api,core,models,services}` and `backend/tests/{integration,unit}`
- [ ] T003 [P] Configure database connection to Neon Serverless Postgres in `backend/src/core/database.py`
- [ ] T004 [P] Configure Qdrant client in `backend/src/core/qdrant.py`
- [ ] T005 [P] Configure Chore API client in `backend/src/core/chore.py`
- [ ] T006 [P] Create base SQLAlchemy models for `BookChunk`, `UserQuery`, and `QueryLog` in `backend/src/models/`

---

## Phase 2: Data Preparation

**Purpose**: Chunk, embed, and upload book content to Qdrant

- [ ] T007 Create a script `backend/src/scripts/prepare_data.py` to read the book content
- [ ] T008 Implement logic to chunk the book content into semantic sections/paragraphs
- [ ] T009 [P] For each chunk, generate embeddings using the Chore API
- [ ] T010 [P] Upload each chunk's embedding and metadata (page/section) to a Qdrant collection

---

## Phase 3: User Story 1 - Reader gets a context-aware answer

**Goal**: Implement the core functionality for a reader to get an answer from selected text.
**Independent Test**: Can be tested by sending a POST request to the `/query` endpoint.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T011 [P] [US1] Create unit test for the query embedding service in `backend/tests/unit/test_services.py`
- [ ] T012 [P] [US1] Create integration test for the `/query` endpoint in `backend/tests/integration/test_api.py`

### Implementation for User Story 1

- [ ] T013 [US1] Create the `/query` endpoint in `backend/src/api/main.py`
- [ ] T014 [US1] Implement the `QueryService` in `backend/src/services/query.py` to handle the business logic
- [ ] T015 [US1] In `QueryService`, generate an embedding for the incoming user query using the Chore API
- [ ] T016 [US1] In `QueryService`, retrieve relevant `BookChunk`s from Qdrant based on the query embedding and selected context
- [ ] T017 [US1] In `QueryService`, use the Chore API to generate a final answer from the retrieved chunks
- [ ] T018 [US1] Ensure the response includes the citation (page/section) from the `BookChunk` metadata

---

## Phase 4: User Story 2 - Developer monitors the chatbot

**Goal**: Implement logging for all chatbot interactions.
**Independent Test**: Can be tested by checking the Postgres database after sending a query.

### Tests for User Story 2 ⚠️

- [ ] T019 [P] [US2] Create unit test for the logging service in `backend/tests/unit/test_services.py`

### Implementation for User Story 2

- [ ] T020 [US2] Implement a `LoggingService` in `backend/src/services/logging.py`
- [ ] T021 [US2] In the `/query` endpoint, after a response is generated, call the `LoggingService`
- [ ] T022 [US2] The `LoggingService` should save the `UserQuery`, the generated response, and the retrieved chunks to the `QueryLog` table in the Postgres database

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T023 [P] Add input validation to the `/query` endpoint
- [ ] T024 [P] Implement rate limiting for the API
- [ ] T025 [P] Add comprehensive error handling for API and service layers
- [ ] T026 [P] Update `quickstart.md` with final instructions
- [ ] T027 [P] Review and refactor code for clarity and performance

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)** & **Data Preparation (Phase 2)** must be completed before any other phase.
- **User Story 1 (Phase 3)** can be implemented after Setup and Data Prep.
- **User Story 2 (Phase 4)** depends on User Story 1.
- **Polish (Phase 5)** can be done last.

### User Story Dependencies

- **User Story 2** is dependent on the core query functionality of **User Story 1**.

### Within Each User Story

- Tests MUST be written and FAIL before implementation.
- Core business logic in services should be implemented before the API endpoint.
