# Data Model: Website RAG Chatbot

This document defines the key data entities that flow through the RAG (Retrieval-Augmented Generation) pipeline. These are not stored in traditional database tables but represent the structure of data in-transit.

## 1. User Query

Represents the input sent from the frontend to the backend.

-   **Type**: JSON Object
-   **Fields**:
    -   `query` (string, required): The question or text submitted by the user.
-   **Validation**:
    -   Must be a non-empty string.
    -   Length must be between 1 and 500 characters.

## 2. Content Chunk

Represents a piece of context retrieved from the vector database (Qdrant).

-   **Type**: Internal Data Structure
-   **Fields**:
    -   `page_content` (string): The actual text content of the chunk.
    -   `metadata` (object): Associated metadata for the chunk.
        -   `source_url` (string): The URL from the sitemap where the content originated.
        -   `title` (string): The title of the source page.

## 3. Generated Response

Represents the final answer sent from the backend to the frontend.

-   **Type**: JSON Object
-   **Fields**:
    -   `response` (string): The answer synthesized by the language model, or the predefined "not available" message.
-   **Validation**:
    -   Must be a non-empty string.
