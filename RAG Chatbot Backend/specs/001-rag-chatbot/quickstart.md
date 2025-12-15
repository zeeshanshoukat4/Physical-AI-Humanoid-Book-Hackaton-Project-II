# Quickstart

This guide provides instructions for setting up and running the RAG chatbot backend.

## Prerequisites

-   Python 3.11+
-   pip
-   git
-   An environment with the following environment variables set:
    -   `NEON_DB_URL`
    -   `CHORE_API_KEY`
    -   `QDRANT_API_KEY`
    -   `QDRANT_CLUSTER_URL`

## 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-name>
```

## 2. Set up the environment

Create a virtual environment and install the dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r backend/requirements.txt
```

## 3. Run the backend server

```bash
uvicorn backend.src.api.main:app --reload
```

The server will be running at `http://127.0.0.1:8000`.

## 4. Run the data preparation script

To populate the Qdrant database with the book's content, run the data preparation script.

```bash
python backend/src/scripts/prepare_data.py
```

## 5. Test the API

You can use the automatically generated OpenAPI documentation at `http://127.0.0.1:8000/docs` to test the API endpoints.
