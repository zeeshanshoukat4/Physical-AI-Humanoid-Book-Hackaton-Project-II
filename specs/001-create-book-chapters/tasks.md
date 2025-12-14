# Tasks: Book Chapters and Content (Docusaurus)

**Input**: Design documents from `/specs/001-create-book-chapters/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

## Phase 1: Project Initialization

**Purpose**: Set up the Docusaurus project foundation.

- [X] T001 Initialize a new Docusaurus 'classic' project in the repository.
- [X] T002 [P] Clean up the default Docusaurus content (blog, default docs, default homepage) that is not needed for the book website.

---

## Phase 2: Configuration and Content Structure

**Purpose**: Configure the site and create the structure for the book's content.

- [X] T003 Configure `docusaurus.config.js` with the book's title ("Physical AI & Humanoid Robotics"), tagline, and other metadata.
- [X] T004 [P] Create the 10 placeholder chapter files as `.mdx` inside the `docs/` directory (e.g., `01-introduction.mdx`, `02-foundations.mdx`, etc.). Populate them with their titles and basic placeholder text.
- [X] T005 [US1] Create `sidebars.js` to define the exact order of the 10 chapters, ensuring they are listed correctly in the navigation.

---

## Phase 3: Theming and Styling (User Story 1, 2, 3)

**Purpose**: Implement the visual design requirements from the specification.

- [X] T006 [P] In `docusaurus.config.js`, set the default theme to 'dark'.
- [X] T007 Modify `src/css/custom.css` to implement the dark, futuristic theme with neon accents for key elements like links, headers, and code blocks.
- [X] T008 [P] Research and add a futuristic font (e.g., from Google Fonts) to the project via `custom.css`.
- [X] T009 [P] Style the interactive buttons and other elements to match the theme in `custom.css`.
- [X] T010 Customize the main homepage at `src/pages/index.js` to include the title, subtitle, and a "Start Reading" button that links to the first chapter.

---

## Phase 4: Content Implementation (User Story 2 & 3)

**Purpose**: Add content to the chapters and enable Docusaurus features.

- [X] T011 [P] Populate the content for `01-introduction.mdx` with 2-3 pages of text and example code, using Markdown and MDX features.
- [X] T012 [P] Populate the content for the remaining 9 chapters.
- [X] T013 [US3] Verify that the default collapsible sidebar categories and the collapsible sections in the main content area are working as expected. Docusaurus provides this functionality out-of-the-box. Add a note to `quickstart.md` about how to structure markdown headings to use this feature.

---

## Phase N: Polish & Cross-Cutting Concerns

- [X] T014 [P] Add the floating chatbot button. This can be done by "swizzling" the root layout component and adding a custom fixed-position component.
- [ ] T015 Review the entire site for responsiveness on mobile, tablet, and desktop viewports.
- [ ] T016 Run a Lighthouse audit to check for performance and accessibility, aiming for scores of >= 90.
- [ ] T017 Implement a proper 404 page by creating a `src/pages/404.js` file.
