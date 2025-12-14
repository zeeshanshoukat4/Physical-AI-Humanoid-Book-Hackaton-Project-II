# Quickstart: Book Chapters and Content

**Date**: 2025-12-14
**Feature**: [Book Chapters and Content](./spec.md)

This document provides a brief guide to getting started with the new components and data structures for this feature.

## 1. Content Management

- **Adding a New Chapter**: To add a new chapter, create a new Markdown file in the `/content/chapters/` directory. The filename should be prefixed with the chapter number and a slug (e.g., `11-advanced-robotics.md`).
- **Frontmatter**: Ensure the new file includes the required frontmatter:
  ```yaml
  ---
  title: "11. Advanced Robotics"
  order: 11
  ---
  ```
- **Content**: Add chapter content in Markdown format directly below the frontmatter. Use standard Markdown headings (`##`, `###`, etc.) to structure sections within a chapter. Docusaurus will automatically generate a Table of Contents based on these headings, which provides in-content navigation. The sidebar will also provide collapsible categories if you group documents using `_category_.json` or explicit sidebar items.


## 2. Key Components

- **`ChapterList` (`src/components/chapter-list.tsx`)**: This component fetches the metadata for all chapters and displays them as a navigable list.
- **`ChapterContent` (`src/components/chapter-content.tsx`)**: This component takes the Markdown content of a single chapter as a prop and uses `react-markdown` to render it to the screen.
- **`Collapsible` (`src/components/ui/collapsible.tsx`)**: A UI component used within `ChapterContent` to create expandable and collapsible sections.

## 3. Data Fetching

- The core data fetching logic resides in `src/lib/chapters.ts`.
- It reads all files from the `content/chapters` directory at build time.
- It uses `gray-matter` to parse the frontmatter and `fs` to read the file content.
- This data is then provided as props to the page components (`src/app/chapters/page.tsx` and `src/app/chapters/[slug]/page.tsx`).
