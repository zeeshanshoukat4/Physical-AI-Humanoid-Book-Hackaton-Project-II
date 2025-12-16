<!--
Sync Impact Report:
- Version change: 0.0.0 -> 1.0.0
- List of modified principles:
  - [PRINCIPLE_1_NAME] -> I. Retrieval-First
  - [PRINCIPLE_2_NAME] -> II. Context-Aware Generation
  - [PRINCIPLE_3_NAME] -> III. Defined Behavior
- Added sections: None
- Removed sections:
    - [PRINCIPLE_4_NAME]
    - [PRINCIPLE_5_NAME]
    - [PRINCIPLE_6_NAME]
    - [SECTION_2_NAME]
    - [SECTION_3_NAME]
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/spec-template.md
  - ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: None
-->
# AI Book Assistant Constitution

## Core Principles

### I. Retrieval-First
Retrieval of relevant text chunks MUST be performed using the Qdrant Vector Database. Embeddings for the book text MUST be generated using the Cohere API.

### II. Context-Aware Generation
Answer generation MUST use the embeddings to create context-aware responses. Every generated answer MUST reference the source paragraph from the book.

### III. Defined Behavior
Answers MUST be concise and clear. If the searched text does not contain the necessary information to answer a question, the assistant MUST respond with: "Sorry, the selected text does not provide this information."

## Governance

All development and functionality MUST adhere to the principles outlined in this constitution. Any amendments to this constitution require documentation, review, and a clear migration plan for existing implementations.

**Version**: 1.0.0 | **Ratified**: 2025-12-16 | **Last Amended**: 2025-12-16