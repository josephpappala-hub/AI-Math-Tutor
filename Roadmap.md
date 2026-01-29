Project Roadmap (Final)

This document records the actual development timeline, decisions, pauses, and conclusion of the Telangana State Board Mathematics AI Tutor project.

The project was developed alongside full-time academic responsibilities and was intentionally concluded prior to Telangana Board Examinations.

Phase 0 — Project Foundation

1 November 2024 – 31 December 2024

Key Decisions

1 Nov 2024 — Identified the problem of conceptual misunderstanding in Telangana State Board mathematics

4 Nov 2024 — Decided to focus on Grades 8–10 Mathematics only

8 Nov 2024 — Chose a Retrieval-Augmented Generation (RAG) approach instead of a generic chatbot

12 Nov 2024 — Selected FastAPI for backend implementation

18 Nov 2024 — Decided that correctness would be rule-based, not AI-determined

22 Nov 2024 — Selected Supabase as the vector database

28 Nov 2024 — Designed curriculum-aligned concept chunks (definitions, reasoning, misconceptions)

Work Completed

Backend project structure created

Curriculum broken into chapter-level concepts

Deterministic answer validation implemented

Vector-based concept retrieval implemented

AI explanation generation integrated with strict constraints

Learned and applied:

API design

Vector embeddings

Retrieval pipelines

AI failure handling

Outcome
By 31 Dec 2024, a functional backend prototype existed that could:

Accept student questions

Validate answers deterministically

Retrieve relevant curriculum concepts

Generate explanations based on retrieved knowledge

Phase 1 — Scope Freeze Due to Board Exam Preparation

1 January 2025 – 31 March 2025

Key Decisions

3 Jan 2025 — Decision made to pause active development

5 Jan 2025 — No new features to be added

10 Jan 2025 — Project declared “feature-frozen”

Reason
Telangana Board examination preparation required full academic focus.

Limited Actions Taken

README documentation updates

Code cleanup and organization

Example API requests written

No architectural changes introduced

Outcome
The project remained stable but unchanged during this period.

Phase 2 — Post-Freeze Evaluation and Conclusion

1 April 2025 – 10 April 2025

Key Decisions

1 Apr 2025 — Reviewed overall project complexity and learning outcomes

4 Apr 2025 — Determined that further expansion would introduce diminishing educational value

7 Apr 2025 — Decided not to pursue frontend deployment or additional grades

10 Apr 2025 — Project officially concluded

Rationale for Conclusion

The project had already achieved its learning objectives

Technical scope exceeded initial expectations for a solo student project

Further work would prioritize polish over learning

Academic responsibilities remained the primary priority

Final Project Status

Status: Concluded (April 2025)

What This Project Demonstrates

Independent problem identification

Curriculum-aligned system design

Responsible use of AI with deterministic safeguards

Understanding of modern AI architectures (RAG)

Willingness to stop when marginal returns outweighed benefits

What This Project Is Not

A commercial product

A finished educational platform

A startup prototype

It is a documented learning initiative.

Repository Contents (Final)

/backend — FastAPI backend prototype

/curriculum — Curriculum-aligned concept data

/examples — Sample API requests and responses

README.md — Project overview and reflection

ROADMAP.md — This document

Closing Statement

This project was intentionally concluded after meeting its educational goals.
The decision to stop reflects prioritization, judgment, and respect for academic commitments.
