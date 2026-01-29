# AI-Powered Mathematics Tutor (Telangana State Board)

## Overview

This project is an AI-powered mathematics tutoring system designed for students following the Telangana State Board curriculum for Grades 8, 9, and 10. The aim of the project is to go beyond simple answer checking and instead focus on conceptual understanding, reasoning, and mistake analysis.

The system is built as a backend-first application that uses curriculum-aligned concept knowledge, semantic retrieval, and a language model to generate explanations for student questions.

This repository represents my first large independent technical initiative, built without prior experience in AI systems or backend development.

---

## Motivation

While studying mathematics, I noticed that most tools available to students only verify whether an answer is correct or incorrect. They do not explain why an answer is wrong or which concept a student is misunderstanding.

I wanted to explore whether AI could be used as a tutor rather than an answer checker, especially for board-level mathematics where conceptual clarity is critical.

---

## Project Scope

- Grades covered: 8, 9, and 10  
- Curriculum: Telangana State Board Mathematics  
- Focus: Concept understanding, reasoning steps, and common misconceptions  
- Platform: Web-based backend API  

---

## High-Level Architecture

The system follows a Retrieval-Augmented Generation (RAG) approach:

Student question  
→ Semantic embedding  
→ Vector database of curriculum concepts  
→ Retrieval of relevant concepts  
→ Language model prompt using retrieved concepts  
→ Generated explanation and feedback  

---

## Repository Structure

backend/
main.py FastAPI application
retrieve.py Concept retrieval logic
explain.py Explanation generation logic
supabase_client.py Supabase database connection

examples/
sample_request.json
sample_response.json
README.md


---

## Development Timeline

November 2025  
I began the project by defining the problem and choosing the Telangana State Board mathematics syllabus as the scope. During this phase, I learned the basics of APIs, embeddings, vector databases, and retrieval-based AI systems. I designed the system architecture independently.

December 2025  
I implemented the backend using FastAPI and structured curriculum concepts into a format suitable for semantic retrieval. I integrated a vector database and worked on connecting retrieval with explanation generation. This phase involved significant trial and error.

January–February 2026  
Most of this period was spent debugging and refining the system. I encountered and resolved issues related to data types, API keys, embedding formats, and function mismatches. I learned how to read stack traces, debug backend errors, and refactor code to make it more maintainable.

March 2026  
Development was paused to focus on Telangana State Board board examinations. This was a deliberate decision to prioritize academics, with plans to resume work after exams.

---

## Challenges and Learning

This project required learning multiple unfamiliar concepts simultaneously, including backend development, vector databases, and AI model integration. The most difficult aspects were designing a system that reflects how students think, structuring mathematical knowledge into concepts, and debugging without external guidance.

Through this process, I developed stronger problem-solving skills, technical reading ability, and discipline in managing a long-term project independently.

---

## Leadership and Initiative

This project demonstrates initiative through identifying a real educational problem and attempting to solve it independently. All system design, implementation, debugging, and documentation were done without templates or guided tutorials.

The repository is structured to be understandable and extendable by others, reflecting an effort to think beyond personal use and toward real-world application.

---

## Current Status

The core backend is implemented, concept-based retrieval is functional, and example API usage is documented. The project is currently paused due to board examinations and is intended to be continued afterward.

---

## Planned Next Steps

- Expand concept coverage across all chapters and grades  
- Improve explanation quality and grading logic  
- Add a simple frontend interface for students  
- Test the system with real users  

---

## Author

Joseph  
Student and independent project developer
