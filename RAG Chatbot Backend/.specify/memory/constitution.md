<!--
---
version_change: "none → 1.0.0"
modified_principles: []
added_sections:
  - Core Principles
  - Key Standards
  - Constraints
  - Success Criteria
  - Governance
removed_sections: []
templates_requiring_updates:
  - path: .specify/templates/plan-template.md
    status: "✅ updated"
  - path: .specify/templates/spec-template.md
    status: "✅ updated"
  - path: .specify/templates/tasks-template.md
    status: "✅ updated"
follow_up_todos: []
---
-->
# Integrated RAG Chatbot for published book Constitution

## Core Principles

### Accuracy
Answers must be strictly based on the book's content; no hallucinations.

### Relevance
Responses must be contextually tied to user-selected text.

### Efficiency
Fast retrieval and response generation using Chore API embeddings.

### Security
API keys must remain confidential; no exposure to frontend.

### Usability
Smooth UX for text selection, chatbot interaction, and response display.

## Key Standards

- **Retrieval**: All answers are derived from Qdrant vector search results.
- **Chunking**: Book content split into semantic chunks (paragraph/section level).
- **API Usage**: Use Chore API for embedding and generation; OpenAI API not allowed.
- **Citation**: Responses must include reference to page/section from the book.
- **Logging**: All queries and retrievals logged in Postgres for debugging and improvement.

## Constraints

- **Tech stack**: FastAPI backend, Neon Serverless Postgres DB, Qdrant Cloud Free Tier, Gemini CLI + SpecificallyKit Plus frontend integration.
- **Response time**: <= 2 seconds per query.
- **Chatbot interaction**: Triggered by icon; can answer based on selected text or whole book fallback.
- **Security**: No API keys exposed; queries validated on backend.

## Success Criteria
- All answers strictly traceable to book content.
- Zero hallucinations; fallback warning if text not found.
- Fully integrated frontend (icon + chat interface) functional on book website.
- Efficient retrieval from Qdrant and secure API handling.
- Positive user experience with accurate, fast, context-based responses.

## Governance

This constitution is the single source of truth for project principles and standards. All development, reviews, and deployments must adhere to it. Amendments require team consensus, documentation of the change, and a clear migration plan for any affected components.

**Version**: 1.0.0 | **Ratified**: 2025-12-15 | **Last Amended**: 2025-12-15