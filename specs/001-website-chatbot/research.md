# Research: Website RAG Chatbot

This document records the decisions made to resolve ambiguities in the implementation plan.

## 1. Testing Frameworks

### Decision
- **Backend (FastAPI)**: We will use `pytest` for all levels of testing (unit, integration).
- **Frontend (React/Docusaurus)**: We will use `Jest` as the test runner and `React Testing Library (RTL)` for rendering components and simulating user interactions.

### Rationale
- `pytest` is the most widely adopted, powerful, and flexible testing framework in the Python ecosystem, with extensive plugin support for web frameworks like FastAPI.
- `Jest` is the standard testing framework for React applications, created and maintained by Facebook. It includes a test runner, assertion library, and mocking capabilities out of thethe-box.
- `React Testing Library` is the recommended library for testing React components in a way that resembles how users interact with them, which leads to more robust and maintainable tests. This is the standard for Docusaurus sites.

### Alternatives Considered
- **Backend**: `unittest` (built-in to Python, but more verbose and less flexible than pytest).
- **Frontend**: `Mocha`/`Chai` (another popular combination, but Jest provides a more integrated "all-in-one" experience for React projects).
