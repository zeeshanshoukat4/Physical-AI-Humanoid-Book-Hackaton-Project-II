---
id: 1
title: Establish AI Book Assistant Constitution
stage: constitution
date: 2025-12-16
surface: agent
model: gemini-cli
feature: none
branch: main
user: zee11
command: /sp.constitution You are an AI assistant embedded in a book website. ...
labels: [constitution, setup]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
 - .specify/templates/plan-template.md
tests:
 - none
---

## Prompt

/sp.constitution You are an AI assistant embedded in a book website. 
Your task is to answer questions **only based on the text selected by the user**. 
Use the following constraints:

1. Retrieval:
   - Use Qdrant Vector Database for searching relevant text chunks.
   - Embed book text using Cohere API embeddings.

2. Generation:
   - Use the embeddings to generate context-aware answers.
   - Always reference the source paragraph from the book.

3. Behavior:
   - Answer concisely and clearly.
   - If the text does not contain the answer, say: "Sorry, the selected text does not provide this information."
quick plz

## Response snapshot

I have updated the project constitution to version 1.0.0, establishing the core principles for the AI Book Assistant. The constitution file at `.specify/memory/constitution.md` and the planning template at `.specify/templates/plan-template.md` have been updated to reflect these new rules.

Suggested commit message:
`docs: establish constitution v1.0.0 for AI Book Assistant`

## Outcome

- ✅ Impact: High. Established foundational principles for the project.
- 🧪 Tests: N/A.
- 📁 Files: 2 files modified.
- 🔁 Next prompts: Follow-up could involve creating a spec for the first feature.
- 🧠 Reflection: The process of updating the constitution and propagating the changes to templates worked smoothly.

## Evaluation notes (flywheel)

- Failure modes observed: Initial `mkdir` command failed due to incorrect syntax for PowerShell.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): null
- Next experiment: N/A
