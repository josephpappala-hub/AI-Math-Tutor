This document outlines the technical, academic, and operational limitations of the Telangana State Board Mathematics AI Tutor project.

The purpose is to provide transparency and context for reviewers, admissions officers, or collaborators.

1. Scope Limitations

Only Grades 8–10 Mathematics were considered; other subjects were excluded.

Grade coverage is partial:

Grade 9 has the most complete concept-chunk encoding

Grades 8 and 10 have limited or no concept encoding

The project is focused on conceptual explanations; it does not solve all possible student questions, especially out-of-syllabus or advanced problems.

The system cannot grade correctness using AI—all correctness checks are deterministic rules.

2. Technical Limitations

The AI explanation component depends on external LLMs via Hugging Face or OpenAI; performance may vary depending on API limits or server availability.

The system uses vector retrieval for concept chunks; coverage is limited to chapters that were encoded. Questions outside encoded concepts may return incomplete explanations.

No frontend styling or UX polish: the frontend is functional but minimal.

The backend requires an API key for the hosted LLM; local deployment is not fully offline.

Memory and computation limits:

Running the full model locally is not feasible on low-spec machines

Retrieval and embedding operations are constrained by Supabase or Pinecone limits

3. Academic Constraints

Development paused during Telangana Board examinations (Jan–Mar 2025)
→ No new features added during this period.

Time constraints meant some planned improvements were deferred or skipped:

Multi-grade concept coverage

Extensive frontend interactivity

Automated testing for every chapter

4. Design Constraints

Explanations are limited to syllabus-approved methods (no shortcuts, advanced math, or logarithms were included).

The system cannot create entirely new questions; it only explains existing ones or variations of encoded concepts.

Error handling is basic; unexpected inputs may result in minimal feedback.

5. Operational Constraints

No large-scale user testing was performed

No analytics or progress tracking

No deployment as a production web app; the backend can run locally or via a simple hosting service

6. Takeaways

Despite these limitations, the project successfully demonstrates:

Independent problem identification

Curriculum-aligned AI explanation

Responsible AI use with deterministic grading

Implementation of a modern AI + database architecture

The limitations reflect realistic scope management, academic priorities, and the constraints of a solo student project.
