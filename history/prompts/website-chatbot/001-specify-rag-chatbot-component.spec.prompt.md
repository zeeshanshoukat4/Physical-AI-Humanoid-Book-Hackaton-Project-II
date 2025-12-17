---
id: 001
title: Specify RAG Chatbot Component
stage: spec
date: 2025-12-17
surface: agent
model: gemini-pro
feature: website-chatbot
branch: 001-website-chatbot
user: zee11
command: /sp.specify
labels: ["spec", "rag", "chatbot"]
links:
  spec: ../../../../specs/001-website-chatbot/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-website-chatbot/spec.md
 - specs/001-website-chatbot/checklists/requirements.md
tests:
 - "none"
---

## Prompt

/sp.specify You are a Retrieval-Augmented Generation (RAG) chatbot embedded inside a book website. WEBSITE & INDEXING - Sitemap URL: https://physical-ai-humanoid-book-hackaton-zeta.vercel.app/sitemap.xml - All content must be indexed only from this sitemap. SECURE CONFIGURATION (ENV-BASED) - QDRANT_API_KEY = {eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.8sxYpE18Pxlj5Rz00fMjMPKsnuxqL1lG8ENWLR71ZEY} - QDRANT_CLUSTER_URL = {https://6538a05d-44cb-4335-a1c7-d66e8ef05ec4.europe-west3-0.gcp.cloud.qdrant.io} - COHERE_API_KEY = {mNbNJJqHliYMHj07KbJmyN4lc9nu38YxLF8CvR97} - NEON_DATABASE_URL = {psql 'postgresql://neondb_owner:npg_JK97krydcqmX@ep-nameless-star-a4i4ftyl-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require} PRIMARY ROLE - Answer user questions strictly using retrieved book content. - Do not use any external or general knowledge. TECH STACK - Backend: FastAPI - Vector Database: Qdrant Cloud - Embeddings: Cohere - Metadata Store: Neon PostgreSQL - Frontend: Gemini CLI + SpecifyKit STRICT RULES (NON-NEGOTIABLE) - Use ONLY the retrieved context. - If the answer is not found, reply EXACTLY: "This information is not available in the book." - No guessing. - No hallucination. - No outside explanations. - Never mention APIs, keys, or internal system details in the answer. ANSWER STYLE - Simple English - Clear and short - Maximum 3-5 lines - No emojis - No unnecessary formatting FAIL-SAFE - If context is empty or irrelevant, clearly say the information is not available in the book. Website chatbot component and repair if already and merge if needed.

## Response snapshot

Finalized the specification for the "Website RAG Chatbot" feature. After clarifying with the user that an existing UI needs to be repaired, the spec and the quality checklist were completed. The feature is now ready for the planning phase.

## Outcome

- ✅ Impact: Created a complete, validated feature specification for the RAG chatbot.
- 🧪 Tests: n/a
- 📁 Files: 2 created, 2 modified
- 🔁 Next prompts: /sp.plan
- 🧠 Reflection: The clarification loop worked as intended, resulting in a more accurate specification. The initial script failure was recoverable.

## Evaluation notes (flywheel)

- Failure modes observed: The `create-new-feature.ps1` script failed with a parameter error, but not before creating the necessary branch and directory, allowing the process to continue.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): n/a
- Next experiment (smallest change to try): n/a
