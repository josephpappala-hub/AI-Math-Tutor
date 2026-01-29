1. Overview

The project implements a Retrieval-Augmented Generation (RAG) pipeline for explaining math concepts while keeping correctness rule-based. The architecture balances AI usage, deterministic grading, and curriculum alignment.

2. High-Level Components

Frontend (HTML + JS)

Single-page interface

Dropdown to select question/chapter

Input box for student answers

Button to submit answers

Output area: correctness, explanation, and mistakes

Backend (FastAPI)

Receives requests from the frontend

Validates student answers using rule-based grading

Retrieves top relevant concept chunks from the vector database

Calls AI model for explanation using retrieved concepts

Returns structured JSON response

Vector Database (Supabase)

Stores curriculum concept embeddings

Each entry contains:

Chapter name

Concept definition

Reasoning steps

Common misconceptions

Example patterns

Supports Top-K similarity search for retrieval

LLM / AI Component

Hosted small model via Hugging Face (free-tier)

Receives top concepts + student question

Generates step-by-step explanation using only syllabus-approved methods

Does not grade correctness

3. Data Flow

The data flow follows these steps:

Student Question
       ↓
Frontend sends request to FastAPI /check-answer
       ↓
Backend validates answer using deterministic rules
       ↓
Query for chapter concepts (embedding → Supabase vector DB)
       ↓
Top-K relevant concepts retrieved
       ↓
AI model receives:
    - Student question
    - Student answer
    - Retrieved concepts
       ↓
AI generates explanation / hint / example
       ↓
Backend responds to frontend:
    - correct: True/False
    - explanation: Generated text
    - mistake: Optional feedback
       ↓
Frontend displays results

4. Module Interactions
Module	Responsibility
main.py (FastAPI)	Endpoint handling, correctness checking, AI explanation orchestration
retrieve.py	Retrieves top relevant concepts from Supabase using vector similarity
explain.py	Calls hosted AI to generate explanation using provided concepts
/curriculum/*.json	Stores chapter-wise concept chunks for embedding
Frontend (index.html)	Collects user input, displays response from /check-answer endpoint
5. Design Principles

Separation of Concerns: AI, grading rules, and database retrieval are independent.

Deterministic Grading: AI only explains, never marks correctness.

Curriculum Alignment: Concepts and explanations strictly adhere to Telangana State Board syllabus.

Scalability: Adding new chapters or grades only requires adding concept embeddings to the database.

Minimal Frontend: Focused on functionality; avoids complex frameworks to simplify integration.

6. Deployment Notes

Backend can be run locally via uvicorn main:app --reload

Supabase database stores embeddings and is accessed via API key

AI calls require a hosted model; local LLM is optional but resource-intensive

Frontend simply calls /check-answer and renders JSON responses
