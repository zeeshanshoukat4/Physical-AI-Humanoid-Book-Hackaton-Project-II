# Feature Specification: RAG FastAPI Backend

**Feature Branch**: `001-rag-fastapi-backend`
**Created**: 2025-12-16
**Status**: Draft
**Input**: User description: "Build a FastAPI backend that handles these operations: 1. POST /embed_text: - Input: Text chunks from the book. - Action: Generate embeddings using Cohere API. - Store embeddings in Qdrant collection. 2. POST /query: - Input: User question + selected text context. - Action: Search Qdrant for top relevant embeddings. - Generate answer using the retrieved text + RAG logic. 3. DB: - Use Neon Serverless Postgres to store: - Book metadata (titles, chapters) - User queries and responses (optional for analytics) 4. Security: - Keep all API keys (Cohere, Qdrant, Neon) in .env file."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Embed Book Content (Priority: P1)

As a system administrator, I want to submit chunks of book text to an API endpoint to be converted into vector embeddings and stored for future retrieval.

**Why this priority**: This is the foundational step. Without the book's content being vectorized and stored, no queries can be answered.

**Independent Test**: This can be tested by sending a sample text chunk to the `/embed_text` endpoint and verifying that a corresponding vector is created in the Qdrant collection.

**Acceptance Scenarios**:

1.  **Given** a valid text chunk from a book, **When** a POST request is made to `/embed_text`, **Then** the system should return a success status and the text's vector embedding should be present in the Qdrant collection.
2.  **Given** a request to `/embed_text` with an invalid API key for the Cohere service, **When** the request is processed, **Then** the system should return an authentication error and no embedding should be stored.

---

### User Story 2 - Query for Answers (Priority: P1)

As a user, I want to send a question to an API endpoint and receive a contextually relevant answer generated from the book's content.

**Why this priority**: This is the core value proposition for the end-user, allowing them to interact with the book's content in a conversational way.

**Independent Test**: This can be tested by sending a question to the `/query` endpoint and verifying that the response is a coherent answer that cites a relevant source from the book content.

**Acceptance Scenarios**:

1.  **Given** the book content has been embedded, **When** a user sends a question to the `/query` endpoint, **Then** the system returns a successful response containing an answer generated from relevant text passages.
2.  **Given** a question that cannot be answered from the embedded book content, **When** the user sends the question to the `/query` endpoint, **Then** the system returns a response indicating that the information is not available in the text.

---

### User Story 3 - Store Metadata and Analytics (Priority: P2)

As a system administrator, I want to store book metadata and a log of user queries to analyze usage patterns and improve the service.

**Why this priority**: This is important for operational management and future improvements, but not critical for the initial user-facing functionality.

**Independent Test**: This can be tested by sending a text chunk for embedding and a user query, then verifying that the corresponding book metadata and query log have been created in the Postgres database.

**Acceptance Scenarios**:

1.  **Given** a new book's text is being embedded, **When** the `/embed_text` endpoint is used, **Then** the book's metadata (title, chapters) is successfully stored in the Postgres database.
2.  **Given** a user has asked a question via the `/query` endpoint, **When** an answer is generated, **Then** the user's question and the system's response are optionally logged in the Postgres database.

---

### Edge Cases

-   What happens when the Cohere API is unavailable or returns an error during embedding? The system should return a clear error message.
-   How does the system handle very long text chunks for embedding? The system MUST reject text chunks larger than a predefined token limit (e.g., 512 tokens) and return an error. The client is responsible for appropriately chunking the text.
-   What happens if the Qdrant database is unavailable? The system should return a service unavailable error.
-   How are different books or versions of books managed in the Qdrant collection? Different books and versions of books MUST be managed within a single Qdrant collection by filtering based on `book_id` and `version` metadata fields associated with each embedded text chunk.

## Requirements *(mandatory)*

### Functional Requirements

-   **FR-001**: The system MUST provide a `POST /embed_text` endpoint to receive and process text chunks.
-   **FR-002**: The system MUST generate vector embeddings for text chunks using the Cohere API.
-   **FR-003**: The system MUST store the generated embeddings in a Qdrant vector collection.
-   **FR-004**: The system MUST provide a `POST /query` endpoint to receive and process user questions.
-   **FR-005**: The system MUST search the Qdrant collection to find text chunks semantically relevant to the user's question.
-   **FR-006**: The system MUST use the retrieved text chunks to generate a context-aware answer (Retrieval-Augmented Generation).
-   **FR-007**: The system MUST store book metadata, such as titles and chapters, in a Neon Serverless Postgres database.
-   **FR-008**: The system MAY store user queries and system responses in the Postgres database for analytics purposes.
-   **FR-009**: The system MUST load all external service credentials (Cohere API Key, Qdrant API Key, Neon DB URL) from a `.env` file at runtime.
-   **FR-010**: The system MUST NOT contain any hardcoded secrets in the source code.

### Key Entities *(include if feature involves data)*

-   **Book Text Chunk**: A segment of text from a book, identified by a unique ID, book ID, chapter, and paragraph number.
-   **Vector Embedding**: A high-dimensional numerical representation of a text chunk, stored in the vector database.
-   **Book Metadata**: Data describing a book, including its title, author, and chapter divisions. Stored in Postgres.
-   **Query Log**: A record containing a user's question, the system-generated answer, and timestamps. Stored in Postgres.

## Success Criteria *(mandatory)*

### Measurable Outcomes

-   **SC-001**: 99% of valid text chunks submitted to the `/embed_text` endpoint are successfully vectorized and stored in under 5 seconds per chunk.
-   **SC-002**: The `/query` endpoint has a p95 latency of less than 3 seconds for generating an answer.
-   **SC-003**: The system can handle at least 50 concurrent queries without a significant increase in response latency or error rates.
-   **SC-004**: A security scan of the codebase confirms that no API keys, credentials, or other secrets are present in the source code.