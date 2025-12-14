# Research: Book Content Rendering

**Date**: 2025-12-14
**Feature**: [Book Chapters and Content](./spec.md)

## Objective

To determine the best method for rendering chapter content stored in local Markdown files within a Next.js application.

## 1. Markdown Rendering Library

### Decision
We will use the `react-markdown` library, along with `remark-gfm` for GitHub Flavored Markdown support (like tables and strikethroughs).

### Rationale
- **Ecosystem Compatibility**: `react-markdown` is a popular and well-maintained library designed specifically for rendering Markdown as React components, which fits perfectly into the Next.js/React technology stack.
- **Security**: It safely renders Markdown to HTML by default, preventing XSS attacks from embedded HTML in the Markdown files.
- **Extensibility**: It has a rich plugin ecosystem (using `remark` and `rehype` plugins) that allows for customization of rendering, syntax highlighting for code blocks, and more. `remark-gfm` is a key plugin that provides support for common Markdown extensions.
- **Server and Client Side**: It works seamlessly on both the server (for initial rendering in Next.js) and the client.

### Alternatives Considered
- **`next-mdx-remote`**: This is a powerful alternative that allows for embedding React components directly within Markdown files (MDX). While powerful, it adds a layer of complexity that is not required for this feature. The specification only calls for displaying text and code examples, not interactive components within the content itself. Sticking with plain Markdown and `react-markdown` is a simpler and more direct approach that fully meets the requirements.
- **Custom Parser**: Building a custom Markdown parser would be time-consuming and unnecessary given the high-quality, secure, and feature-rich open-source libraries available.
