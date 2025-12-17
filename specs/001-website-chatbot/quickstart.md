# Quickstart: Website RAG Chatbot Backend

This guide provides instructions to set up and run the FastAPI backend for the RAG chatbot.

## Prerequisites

-   Python 3.11 or later
-   Poetry for dependency management
-   Access to environment variables for `QDRANT_API_KEY`, `QDRANT_CLUSTER_URL`, `COHERE_API_KEY`, and `NEON_DATABASE_URL`.

## 1. Setup Backend Environment

From the repository root:

```bash
# Navigate to the backend directory
cd backend

# Install dependencies using Poetry
poetry install
```

## 2. Configure Environment Variables

Create a `.env` file in the `backend` directory and add the following secrets:

```env
QDRANT_API_KEY="your-qdrant-api-key"
QDRANT_CLUSTER_URL="your-qdrant-cluster-url"
COHERE_API_KEY="your-cohere-api-key"
NEON_DATABASE_URL="your-neon-database-url"
```

Replace the placeholder values with the actual credentials as defined in the project constitution.

## 3. Run the Backend Server

Once the dependencies are installed and the environment is configured, run the FastAPI server:

```bash
# From the backend directory
poetry run uvicorn src.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## 4. Interact with the API

You can interact with the API via the automatically generated documentation at `http://127.0.0.1:8000/docs`.

Alternatively, you can use `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/chat" \
-H "Content-Type: application/json" \
-d '{"query": "What is Natural Human-Robot Interaction?"}'
```

**Expected Response:**

```json
{
  "response": "Natural Human-Robot Interaction focuses on creating intuitive and seamless communication between humans and robots, often using verbal and non-verbal cues. The goal is to make interacting with a robot feel as natural as interacting with another person."
}
```
