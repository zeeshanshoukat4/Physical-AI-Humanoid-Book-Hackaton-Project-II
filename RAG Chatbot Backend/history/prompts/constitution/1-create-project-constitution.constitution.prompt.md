---
id: 1
title: Create Project Constitution
stage: constitution
date: 2025-12-15
surface: agent
model: gemini
feature: none
branch: main
user: Zeeshan Shoukat
command: /sp.constitution
labels: [constitution, initialization]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - none
---

## Prompt

/sp.constitution         Project: Integrated RAG Chatbot for published book

  Core principles:
  - Accuracy: Answers must be strictly based on the book's content; no hallucinations.
  - Relevance: Responses must be contextually tied to user-selected text.
  - Efficiency: Fast retrieval and response generation using Chore API embeddings.
  - Security: API keys must remain confidential; no exposure to frontend.
  - Usability: Smooth UX for text selection, chatbot interaction, and response display.

  Key standards:
  - Retrieval: All answers are derived from Qdrant vector search results.
  - Chunking: Book content split into semantic chunks (paragraph/section level).
  - API Usage: Use Chore API for embedding and generation; OpenAI API not allowed.
  - Citation: Responses must include reference to page/section from the book.
  - Logging: All queries and retrievals logged in Postgres for debugging and improvement.

  Constraints:
  - Tech stack: FastAPI backend, Neon Serverless Postgres DB, Qdrant Cloud Free Tier, Gemini CLI + SpecificallyKit Plus frontend integration.
  - Response time: <= 2 seconds per query.
  - Chatbot interaction: Triggered by icon; can answer based on selected text or whole book fallback.
  - Security: No API keys exposed; queries validated on backend.

  Success criteria:
  - All answers strictly traceable to book content.
  - Zero hallucinations; fallback warning if text not found.
  - Fully integrated frontend (icon + chat interface) functional on book website.
  - Efficient retrieval from Qdrant and secure API handling.
  - Positive user experience with accurate, fast, context-based responses.

## Response snapshot

I have created the project constitution and verified that the templates and commands are consistent.

## Outcome

- ✅ Impact: The project now has a constitution that defines its core principles and standards.
- 🧪 Tests: none
- 📁 Files: .specify/memory/constitution.md
- 🔁 Next prompts: none
- 🧠 Reflection: The initial constitution provides a solid foundation for the project.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none
