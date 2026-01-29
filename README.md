# AI-Powered Mathematics Tutor (Telangana State Board)

## Overview

This project is an AI-powered mathematics tutoring system designed for **Telangana State Board students (Grades 8–10)**.  
The goal is not to simply check answers, but to **understand mathematical concepts**, identify **student misconceptions**, and provide **clear, concept-based explanations** for any curriculum-aligned question.

The system uses a **Retrieval-Augmented Generation (RAG)** approach, combining:
- Curriculum-aligned concept knowledge
- Semantic retrieval from a vector database
- A language model to generate explanations

This repository represents my **first large independent technical initiative**, developed entirely on my own.

---

## Motivation

During my studies, I noticed that:
- Students often memorize procedures without understanding concepts
- Most online tools only verify answers, not reasoning
- Teachers lack scalable tools to give individualized feedback

I wanted to build a system that behaves more like a **tutor**, not an answer checker.

---

## Project Scope

- Grades: **8, 9, and 10**
- Curriculum: **Telangana State Board Mathematics**
- Focus: **Concept understanding, reasoning steps, and misconceptions**
- Platform: **Web-based API (backend-first design)**

---

## Architecture (High-Level)

Student Question
↓
Semantic Embedding
↓
Vector Database (Concept Chunks)
↓
Top Relevant Concepts Retrieved
↓
LLM Prompt (Concepts + Question)
↓
Generated Explanation / Feedback


---

## Repository Structure

backend/
├── main.py # FastAPI application
├── retrieve.py # Concept retrieval logic
├── explain.py # Explanation generation
├── supabase_client.py # Database connection

examples/
├── sample_request.json
├── sample_response.json
└── README.md

README.md


---

## Timeline & Development Journey

### 🟢 November 2025 — Project Start
- Chose problem statement and curriculum scope
- Learned basics of:
  - APIs
  - Vector databases
  - Embeddings
  - Retrieval-Augmented Generation
- Designed the system architecture independently

### 🟡 December 2025 — Core Implementation
- Built a FastAPI backend from scratch
- Structured curriculum concepts into retrievable units
- Integrated a vector database (Supabase Vector)
- Faced major challenges with:
  - API design
  - Type errors
  - Embedding formats
  - Data modeling for education

### 🔴 January–February 2026 — Debugging & Refinement
- Resolved:
  - API key handling
  - Data type mismatches
  - Retrieval vs generation logic
- Learned to read stack traces and debug production-style errors
- Added examples and documentation to make the project usable by others

### ⏸️ March 2026 — Temporary Pause
Development was **intentionally paused** to focus on:
- Telangana State Board **Board Examinations**
- Academic priorities

This pause was a conscious decision to balance academics with long-term projects.

---

## Challenges Faced (Key Learning)

- Understanding how **AI systems actually work end-to-end**
- Translating textbook questions into **concept-based knowledge**
- Debugging without mentors or prior experience
- Managing scope as a solo developer
- Designing for **real users**, not just code correctness

Every challenge significantly improved my:
- Problem-solving ability
- Technical reading skills
- Project planning discipline

---

## Leadership & Initiative

This project demonstrates leadership through:
- Identifying a real educational gap
- Designing a system independently
- Persisting through repeated failures
- Structuring the project for others to understand and extend
- Documenting work clearly for non-technical reviewers

No external templates or boilerplate projects were used.

---

## Current Status

- Core backend implemented
- Concept-based retrieval functional
- Example API usage documented
- Project paused for exams, **planned to resume**

---

## Planned Next Steps (Post-Exams)

- Expand concept coverage across all chapters
- Improve explanation quality and grading logic
- Add a simple frontend for student use
- Conduct pilot testing with real students/teachers

---

## Why This Project Matters

This initiative reflects my interest in:
- Artificial Intelligence
- Education technology
- Systems thinking
- Independent problem-solving

More importantly, it represents my ability to **start, struggle, learn, and build** — not just succeed instantly.

---

## Author

**Joseph**  
Student | Aspiring Engineer  
Independent Project Developer
