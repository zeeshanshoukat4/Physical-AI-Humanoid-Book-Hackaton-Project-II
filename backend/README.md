# Backend Service for RAG Chatbot

This directory contains the FastAPI backend service that powers the AI RAG (Retrieval-Augmented Generation) chatbot for the book website.

## Overview

The service provides a single API endpoint (`/api/v1/chat`) that accepts a user's query and returns an answer generated based on the content of the book.

It uses a RAG pipeline with the following components:
- **FastAPI**: For the web framework.
- **Qdrant**: As the vector database for storing and retrieving content chunks.
- **Cohere**: For generating text embeddings and generating final answers.
- **Neon**: As the metadata store (if needed in the future).

## Setup and Execution

For detailed instructions on how to set up the environment, install dependencies, and run the server, please refer to the quickstart guide for this feature located at:

`../specs/001-website-chatbot/quickstart.md`

### Basic Steps

1.  Create a `.env` file in this directory (use `.env.example` as a template).
2.  Install dependencies using `pip install -r requirements.txt`.
3.  Run the data ingestion script: `python ingest.py`.
4.  Run the server: `uvicorn src.main:app --reload`.
