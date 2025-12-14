# Data Model: Book Chapters

**Date**: 2025-12-14
**Feature**: [Book Chapters and Content](./spec.md)

This document describes the data structure for the primary entities in this feature.

## Chapter Entity

Represents a single chapter in the book. The data will be sourced from Markdown files in the `content/chapters/` directory. Each file's frontmatter will contain the metadata, and the body will be the content.

### Attributes

| Attribute  | Type             | Description                                                                 | Required | Example                                  |
|------------|------------------|-----------------------------------------------------------------------------|----------|------------------------------------------|
| `slug`     | `string`         | Unique identifier for the URL, derived from the Markdown file name.         | Yes      | `01-introduction-to-physical-ai`         |
| `title`    | `string`         | The full title of the chapter.                                              | Yes      | "1. Introduction to Physical AI"         |
| `order`    | `number`         | A number to sort the chapters correctly.                                    | Yes      | `1`                                      |
| `content`  | `string`         | The full Markdown content of the chapter body.                              | Yes      | "## What is Physical AI? \n\n Physical AI is..." |

### Relationships

- A **Book** has many **Chapters**. (Implicit relationship, the "Book" is the website itself).

### Example File (`01-introduction-to-physical-ai.md`)

```markdown
---
title: "1. Introduction to Physical AI"
order: 1
---

## What is Physical AI?

Physical AI refers to artificial intelligence that interacts with the physical world through robotics...

### Code Example: Basic Agent Movement

```python
class Agent:
    def __init__(self, position):
        self.position = position

    def move(self, direction):
        # ... logic to move the agent
        print(f"Moving {direction}")

agent = Agent(position=(0, 0))
agent.move("forward")
```
```
