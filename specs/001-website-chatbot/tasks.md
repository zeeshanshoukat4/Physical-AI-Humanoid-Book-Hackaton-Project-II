# Tasks: Website RAG Chatbot

**Input**: Design documents from `specs/001-website-chatbot/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/openapi.yaml

**Tests**: Tests are included for backend API validation, following the decisions in `research.md`.

**Organization**: Tasks are grouped by foundational phases and then by user story to enable incremental, testable implementation.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)

---
## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Initialize the backend project structure and dependencies.

- [X] T001 Create the root directory for the new backend service at `backend/`.
- [X] T002 [P] Initialize a new Python project using Poetry in `backend/` by running `poetry init`.
- [X] T003 [P] Add core production dependencies to `backend/pyproject.toml`: `fastapi`, `uvicorn`, `pydantic`, `python-dotenv`, `cohere`, `qdrant-client`, `psycopg2-binary`.
- [X] T004 [P] Add core development dependencies to `backend/pyproject.toml`: `pytest`, `httpx` (for testing).
- [X] T005 [P] Create the basic directory structure: `backend/src/api`, `backend/src/services`, `backend/src/models`, `backend/src/core`, and `backend/tests`.
- [X] T006 [P] Configure linting for the backend project with `ruff` in `backend/pyproject.toml`.

---
## Phase 2: Foundational (Blocking RAG Pipeline)

**Purpose**: Build the core RAG pipeline and data ingestion scripts. This is the prerequisite for all user-facing functionality.

- [X] T007 Create a configuration module in `backend/src/core/config.py` to load secrets (API keys, DB URLs) from environment variables.
- [X] T008 Implement a data loading service in `backend/src/services/data_loader.py` to fetch and parse content from the sitemap URL specified in the constitution.
- [X] T009 Implement a text splitting utility in `backend/src/core/text_splitter.py` to chunk the loaded content into manageable pieces.
- [X] T010 Implement a vector DB service in `backend/src/services/qdrant_service.py` to connect to Qdrant Cloud and handle collection creation.
- [X] T011 Implement an embedding service in `backend/src/services/cohere_service.py` that uses the Cohere API key to generate embeddings for text chunks.
- [X] T012 Create a standalone ingestion script `backend/ingest.py` that uses the data loader, text splitter, and embedding service to process and upload content chunks and their vectors to Qdrant.
- [X] T013 Implement the core RAG logic in `backend/src/services/rag_service.py` which retrieves context from Qdrant and uses Cohere to generate an answer based on a user query. This service must include the fail-safe logic to return the "not available" message.
- [X] T014 Define the request and response Pydantic models (UserQuery, GeneratedResponse) in `backend/src/models/chat.py` based on `data-model.md`.
- [X] T015 Implement the API endpoint `POST /api/v1/chat` in `backend/src/api/chat.py` that uses the `rag_service` to respond to user queries.
- [X] T016 [P] Set up the main FastAPI application in `backend/src/main.py` and include the chat API router.

**Checkpoint**: The backend is now capable of handling chat requests. The data ingestion script can be run to populate the vector database.

---
## Phase 3: User Story 1 - Answer Retrieval (Priority: P1) 🎯 MVP

**Goal**: Connect the backend to the frontend and allow users to ask questions and receive answers from book content.

**Independent Test**: The full user flow can be tested by opening the chatbot on the website, asking a question with a known answer, and verifying the correct answer is displayed in the UI.

### Tests for User Story 1 ⚠️
- [X] T017 [P] [US1] Write an integration test in `backend/tests/test_chat_api.py` to verify the `/api/v1/chat` endpoint returns a successful response (200 OK) for a valid query.

### Implementation for User Story 1
- [X] T018 [P] [US1] Analyze the existing Docusaurus component at `src/components/ChatbotWindow/index.tsx` to understand its structure and state management.
- [X] T019 [US1] Create a state management solution (e.g., React `useState` or `useReducer`) inside `src/components/ChatbotWindow/index.tsx` to handle user input, chat message history, and loading status.
- [X] T020 [US1] Implement the API call logic within `src/components/ChatbotWindow/index.tsx` to send the user's query to the `POST /api/v1/chat` backend endpoint.
- [X] T021 [US1] Update the rendering logic in `src/components/ChatbotWindow/index.tsx` to display the chat history, including the user's query and the response from the backend.
- [X] T022 [US1] Ensure the UI in `src/components/ChatbotWindow/index.tsx` displays a loading indicator while waiting for the API response.

**Checkpoint**: The chatbot is now fully functional on the website for retrieving answers.

---
## Phase 4: User Story 2 - Handling Out-of-Scope Questions (Priority: P2)

**Goal**: Ensure the system correctly identifies out-of-scope questions and responds with the standardized "not available" message.

**Independent Test**: Can be tested by asking the chatbot an off-topic question (e.g., "What is the weather?") and verifying the UI displays the exact text "This information is not available in the book."

### Tests for User Story 2 ⚠️
- [X] T023 [P] [US2] Add an integration test case to `backend/tests/test_chat_api.py` to verify the `/api/v1/chat` endpoint returns the "not available" message when the RAG service cannot find a relevant context.

### Implementation for User Story 2
- [X] T024 [US2] Verify and, if needed, refine the logic in `backend/src/services/rag_service.py` to ensure it correctly triggers the fail-safe "not available" response when no relevant context is found. (No new files, just validation/refinement).

**Checkpoint**: The chatbot now correctly handles both in-scope and out-of-scope questions as per the specification.

---
## Phase 5: Polish & Cross-Cutting Concerns

- [X] T025 [P] Add a `README.md` to the `backend/` directory explaining setup and execution, referencing `quickstart.md`.
- [X] T026 [P] Review and add inline documentation (docstrings, comments) to the backend Python code where logic is complex.
- [X] T027 [P] Perform a final review of environment variable handling in `backend/src/core/config.py` to ensure no secrets are hardcoded.

---
## Dependencies & Execution Order

- **Phase 1 (Setup)** must be completed first.
- **Phase 2 (Foundational)** depends on Phase 1 and is a blocker for all user stories.
- **Phase 3 (US1)** depends on Phase 2.
- **Phase 4 (US2)** depends on the services built in Phase 2 and can be worked on after T013 is complete, but is logically tested after the MVP in US1 is working.
- **Phase 5 (Polish)** can be done after all user stories are complete.

## Implementation Strategy

### MVP First (User Story 1)

1.  Complete **Phase 1** and **Phase 2** to build the entire backend pipeline.
2.  Run the `ingest.py` script to populate the database.
3.  Complete **Phase 3** to connect the frontend to the backend.
4.  **STOP and VALIDATE**: The core feature is now testable end-to-end. Demo the MVP.

### Incremental Delivery

1.  After the MVP is validated, proceed to **Phase 4** to explicitly test and harden the out-of-scope response behavior.
2.  Complete **Phase 5** for final cleanup and documentation.
