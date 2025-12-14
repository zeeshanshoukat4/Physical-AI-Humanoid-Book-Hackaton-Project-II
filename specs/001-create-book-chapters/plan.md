# Implementation Plan: Book Chapters and Content

**Branch**: `001-create-book-chapters` | **Date**: 2025-12-14 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `C:\Users\zee11\Desktop\Zee\ai-native-book\specs\001-create-book-chapters\spec.md`

## Summary

This plan outlines the technical approach for building the core content feature of the Physical AI book website. It involves creating a system to render 10 chapters from local Markdown files, implementing a dark-themed, responsive UI with collapsible sections, and establishing the necessary file structure and dependencies within the Next.js framework.

## Technical Context

**Language/Version**: TypeScript 5.x
**Primary Dependencies**: Next.js 14.x, React 18.x, Tailwind CSS 3.x, `react-markdown` for content rendering.
**Storage**: Chapter content will be stored as Markdown (`.md`) files within the project's file system at a dedicated `content/chapters` directory.
**Testing**: Jest and React Testing Library for unit and component tests.
**Target Platform**: Web (Desktop and Mobile browsers).
**Project Type**: Web Application.
**Performance Goals**: Achieve a Google Lighthouse score of >= 85 for Performance, Accessibility, and Best Practices. Initial page loads should be under 2 seconds.
**Constraints**: The solution must not require an external database or CMS; all content is to be managed within the git repository.

## Constitution Check

*GATE: All principles from the project constitution are addressed and adhered to.*

- ✅ **I. Technology Stack**: The plan uses the prescribed stack of Next.js and TypeScript.
- ✅ **II. Modern & Engaging User Experience**: The plan incorporates the required dark theme, responsive layout, and interactive elements.
- ✅ **III. Content Structure**: The content is structured into chapters as defined.
- ✅ **IV. Core Functionality**: The plan provides for chapter navigation and display.

## Project Structure

### Documentation (this feature)

```text
specs/001-create-book-chapters/
├── plan.md              # This file
├── spec.md              # The feature specification
└── tasks.md             # To be created by /sp.tasks
```

### Source Code (repository root)

```text
/
├── content/
│   ├── chapters/
│   │   ├── 01-introduction-to-physical-ai.md
│   │   ├── ... (and 9 more chapter files)
│   └── index.ts             # Helper to load all chapter metadata
├── src/
│   ├── app/
│   │   ├── chapters/
│   │   │   ├── page.tsx             # Main chapters list page (User Story 1)
│   │   │   └── [slug]/
│   │   │       └── page.tsx         # Dynamic page for a single chapter (User Story 2)
│   │   └── layout.tsx
│   ├── components/
│   │   ├── ui/
│   │   │   ├── button.tsx
│   │   │   └── collapsible.tsx      # Component for collapsible sections (User Story 3)
│   │   ├── chapter-list.tsx
│   │   └── chapter-content.tsx
│   └── lib/
│       └── chapters.ts          # Functions to read and parse Markdown files
└── tests/
    ├── components/
    └── lib/
```

**Structure Decision**: A standard Next.js (App Router) project structure will be used. Content is decoupled into a top-level `content/` directory to separate it from application logic. The `src/` directory will house all application code, including pages, components, and utility functions for data fetching.

## Complexity Tracking

No violations of the constitution were identified. Complexity is low and managed by adhering to framework best practices.