# Implementation Plan: [FEATURE]

**Branch**: `[###-feature-name]` | **Date**: [DATE] | **Spec**: [link]
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This feature involves implementing a Retrieval-Augmented Generation (RAG) chatbot on the book website. The chatbot will answer user questions strictly based on the book's content, which will be indexed from a provided sitemap. The implementation requires repairing and integrating with an existing UI component and building a FastAPI backend that uses Qdrant, Cohere, and Neon PostgreSQL to power the RAG pipeline.

## Technical Context

**Language/Version**: Python 3.11 (Backend), TypeScript/React (Frontend)
**Primary Dependencies**: FastAPI, Qdrant, Cohere, Neon PostgreSQL, React
**Storage**: Qdrant (Vector DB), Neon PostgreSQL (Metadata Store)
**Testing**: pytest (Backend), Jest & React Testing Library (Frontend)
**Target Platform**: Web Browser
**Project Type**: Web application
**Performance Goals**: p90 latency < 3 seconds for chatbot responses.
**Constraints**: Must only use retrieved book content for answers; must provide a specific "not found" response; must not expose internal system details.
**Scale/Scope**: A single chatbot component on the existing Docusaurus website.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [X] **I. WEBSITE & INDEXING**: Compliant. FR-002 specifies indexing from the sitemap.
- [X] **II. SECURE CONFIGURATION (ENV-BASED)**: Compliant. Assumed sensitive keys will be handled via environment variables.
- [X] **III. PRIMARY ROLE**: Compliant. FR-004 ensures answers only come from retrieved content.
- [X] **IV. TECH STACK**: Compliant. The plan will follow the specified stack.
- [X] **V. STRICT RULES (NON-NEGOTIABLE)**: Compliant. FR-003 and FR-005 enforce the strict rules.
- [X] **VI. ANSWER STYLE**: Compliant. FR-006 defines the answer style.
- [X] **VII. FAIL-SAFE**: Compliant. FR-003 handles cases where answers are not found.

**All constitutional gates passed.**

## Project Structure

### Documentation (this feature)

```text
specs/001-website-chatbot/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)
```text
# Web application structure
backend/
├── src/
│   ├── models/
│   ├── services/
│   └── api/
└── tests/

src/  (Existing Docusaurus frontend)
├── components/
│   ├── ChatbotButton/
│   └── ChatbotWindow/  # Repair and merge here
└── ...
```

**Structure Decision**: The project will use a hybrid structure. A new `backend` directory will be created for the FastAPI application. The frontend work will involve modifying existing components within the `src/components` directory of the Docusaurus application, as specified in FR-007.
## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
