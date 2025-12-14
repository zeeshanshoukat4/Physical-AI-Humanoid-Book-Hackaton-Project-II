# Tasks: Book Chapters and Content

**Input**: Design documents from `/specs/001-create-book-chapters/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

## Phase 1: Setup (Shared Infrastructure)

- [ ] T001 [P] Install `react-markdown` and `remark-gfm` dependencies.
- [ ] T002 [P] Create the `content/chapters` directory and add placeholder Markdown files for all 10 chapters.
- [ ] T003 [P] Configure Tailwind CSS `tailwind.config.ts` with the dark theme colors and futuristic fonts.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core data loading and utility functions that all user stories depend on.

- [ ] T004 Create the chapter library file `src/lib/chapters.ts`.
- [ ] T005 Implement a function in `src/lib/chapters.ts` to get sorted metadata for all chapters (slug, title, order).
- [ ] T006 Implement a function in `src/lib/chapters.ts` to get the full content of a single chapter by its slug.
- [ ] T007 [P] Create a basic unit test file `tests/lib/chapters.test.ts` to verify the data loading functions.

---

## Phase 3: User Story 1 - View Chapter List (Priority: P1) 🎯 MVP

**Goal**: Display a list of all 10 book chapters.
**Independent Test**: Navigate to `/chapters` and verify all 10 chapter titles are listed and link correctly.

- [ ] T008 [P] Create the `ChapterList` component in `src/components/chapter-list.tsx` to display a list of chapter links.
- [ ] T009 Create the main chapters page at `src/app/chapters/page.tsx`.
- [ ] T010 In `src/app/chapters/page.tsx`, use the function from T005 to fetch all chapter metadata and pass it to the `ChapterList` component.
- [ ] T011 [P] Style the chapter list using Tailwind CSS according to the dark, futuristic theme.

---

## Phase 4: User Story 2 - Read Chapter Content (Priority: P2)

**Goal**: Display the content of a single selected chapter.
**Independent Test**: Navigate to `/chapters/[slug]` and verify the chapter's title and content are rendered correctly from its Markdown file.

- [ ] T012 [P] Create the `ChapterContent` component in `src/components/chapter-content.tsx`. This component will take Markdown content as a prop and use `react-markdown` to render it.
- [ ] T013 Create the dynamic chapter page at `src/app/chapters/[slug]/page.tsx`.
- [ ] T014 In `src/app/chapters/[slug]/page.tsx`, use the function from T006 to fetch the specific chapter's content based on the URL slug.
- [ ] T015 Pass the fetched content to the `ChapterContent` component for rendering.
- [ ] T016 [P] Style the rendered Markdown content (headings, paragraphs, code blocks) in `src/app/globals.css` or a similar global stylesheet for a consistent look.

---

## Phase 5: User Story 3 - Navigate with Collapsible Sections (Priority: P3)

**Goal**: Make sections within a chapter collapsible.
**Independent Test**: On a chapter page with multiple H2 or H3 sections, verify that clicking the section title expands and collapses its content.

- [ ] T017 [P] Create a reusable `Collapsible` UI component in `src/components/ui/collapsible.tsx`. This component will manage its own open/closed state.
- [ ] T018 [P] Test the `Collapsible` component in isolation.
- [ ] T019 Modify the `ChapterContent` component (T012) to use custom renderers with `react-markdown`.
- [ ] T020 In `ChapterContent`, create a custom renderer for heading elements (e.g., `h2`) that wraps the heading and its subsequent content in the `Collapsible` component.

---

## Phase N: Polish & Cross-Cutting Concerns

- [ ] T021 Implement the responsive design for all new components and pages, ensuring usability on mobile, tablet, and desktop.
- [ ] T022 Create the shared `Button` component in `src/components/ui/button.tsx` with futuristic styling.
- [ ] T023 Implement the not-found handling for dynamic chapter pages as defined in the spec's edge cases.
