# Research and Best Practices

This document outlines best practices for the core technologies used in this project.

## FastAPI

-   **Project Structure**: A modular structure with `api`, `services`, and `models` directories will be used to organize code effectively.
-   **Dependencies**: `pydantic` will be used for data validation and `SQLAlchemy` for database interaction.
-   **Asynchronous Operations**: All I/O-bound operations (database queries, API calls) will be implemented using `async` and `await` to ensure non-blocking execution.
-   **Testing**: `pytest` will be used for unit and integration testing, with `httpx` for testing API endpoints.

## Qdrant

-   **Collections**: A single collection will be created to store the embeddings for the book's content.
-   **Indexing**: The collection will be indexed to optimize for speed and recall.
-   **Metadata**: Each vector will have metadata attached (page number, section title) to allow for filtering and citation.
-   **Filtering**: Searches will be filtered based on the user's selected text to ensure relevance.

## Neon Serverless Postgres

-   **Schema**: A simple schema will be designed to store the book's text, user queries, and logs.
-   **Connection Pooling**: Connection pooling will be used to manage connections efficiently in a serverless environment.
-   **Migrations**: `alembic` can be used to manage database schema migrations if the schema evolves.

## Chore API

-   **Client**: An `httpx` client will be used to interact with the Chore API.
--   **Error Handling**: The client will implement robust error handling and retry logic for transient network issues.
-   **Security**: The API key will be stored securely as an environment variable and never hardcoded.
