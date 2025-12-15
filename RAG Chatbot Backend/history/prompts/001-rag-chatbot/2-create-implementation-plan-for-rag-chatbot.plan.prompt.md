---
id: 2
title: Create Implementation Plan for RAG Chatbot
stage: plan
date: 2025-12-15
surface: agent
model: gemini
feature: 001-rag-chatbot
branch: 001-rag-chatbot
user: Zeeshan Shoukat
command: /sp.plan
labels: [plan, rag, chatbot]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-rag-chatbot/plan.md
  - specs/001-rag-chatbot/research.md
  - specs/001-rag-chatbot/data-model.md
  - specs/001-rag-chatbot/contracts/openapi.json
  - specs/001-rag-chatbot/quickstart.md
tests:
  - none
---

## Prompt

/sp.plan  Integrated RAG Chatbot for Published Book

Objective: Build and deploy a fully functional RAG chatbot embedded in the book website that answers questions based strictly on selected text using Chore API, Qdrant, and Neon Postgres.

Major Phases:

1. **Project Setup**
   - Initialize FastAPI backend project.  
   - Configure Neon Serverless Postgres database with schema for book text, embeddings, user queries, and logs.  
   - Set up Qdrant Cloud Free Tier for vector storage and semantic search.  
   - Integrate Chore API key securely in backend environment.

2. **Data Preparation**
   - Chunk book content into semantic sections/paragraphs.  
   - Generate embeddings for each chunk using Chore API.  
   - Upload embeddings to Qdrant with proper metadata (page/section reference).

3. **Backend Development**
   - API endpoint for receiving user queries from frontend.  
   - Retrieve relevant chunks from Qdrant based on user-selected text or fallback full-text search.  
   - Generate answers via Chore API, ensuring output strictly references retrieved text.  
   - Log all queries, retrievals, and responses in Neon Postgres.

4. **Frontend Integration**
   - Embed chat icon using Gemini CLI + SpecificallyKit Plus.  
   - Implement text selection listener to pass selected content to backend.  
   - Display chatbot responses inline, highlighting referenced book sections/pages.  
   - Handle errors or no-relevant-text fallback gracefully.

5. **Security & Optimization**
   - Ensure API keys (Chore, Qdrant, Neon) never exposed to frontend.  
   - Implement rate limiting and input validation in FastAPI.  
   - Optimize retrieval latency from Qdrant (target <= 2 seconds response time).

6. **Testing**
   - Unit tests for API endpoints and Qdrant retrieval logic.  
   - Functional tests for frontend chatbot interaction (icon click, text selection, response display).  
   - Validation tests to ensure no hallucinations; answers strictly traceable to book content.  

7. **Deployment**
   - Deploy FastAPI backend (VPS, Cloud, or serverless).  
   - Connect frontend website to backend.  
   - Monitor logs and performance metrics; fine-tune retrieval and generation.

Timeline:
- Phase 1-2 (Setup + Data Prep): 3-4 days  
- Phase 3 (Backend Dev): 4-5 days  
- Phase 4 (Frontend Integration): 2-3 days  
- Phase 5-6 (Security + Testing): 2-3 days  
- Phase 7 (Deployment + Monitoring): 1-2 days  

Credentials (for backend only):
- Neon Postgres: psql 'postgresql://neondb_owner:npg_i7zLwZ4xuSpa@ep-steep-math-a4v94vv6-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'  
- Chore API: TbFXEtlk1G89N7youeI0oLkMPFrLlNcBRcrRmCu7  
- Qdrant API Key: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.uBUft8CBOT7SMTd11bQlxkG_YnC-2eBUqeOzNqNPEJg  
- Qdrant Cluster Endpoint: https://0e891ad9-d08c-49c7-a45e-d062b0b81e2c.europe-west3-0.gcp.cloud.qdrant.io

Constraints:
- Responses generated via Chore API only; no OpenAI usage.  
- Must strictly answer based on retrieved book content.  
- Frontend integration via Gemini CLI + SpecificallyKit Plus.  
- Response latency <= 2 seconds.

## Response snapshot

I have created the implementation plan and all the necessary design artifacts for the RAG chatbot feature.

## Outcome

- ✅ Impact: The implementation plan for the RAG chatbot is now complete and ready for the task generation phase.
- 🧪 Tests: none
- 📁 Files: specs/001-rag-chatbot/plan.md, specs/001-rag-chatbot/research.md, specs/001-rag-chatbot/data-model.md, specs/001-rag-chatbot/contracts/openapi.json, specs/001-rag-chatbot/quickstart.md
- 🔁 Next prompts: /sp.tasks
- 🧠 Reflection: The planning phase was successful and all the required artifacts were generated.

## Evaluation notes (flywheel)

- Failure modes observed: I initially made a mistake by trying to read a file with an absolute path outside of the workspace. I corrected this by using a relative path.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none
