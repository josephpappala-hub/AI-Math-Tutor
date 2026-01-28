from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import logging

from retrieve import retrieve_concepts
from explain import generate_explanation

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Math Tutor Backend",
    description="Telangana State Board Mathematics Tutor",
    version="1.0.0"
)


# ========================
# Request/Response Models
# ========================
class CheckAnswerRequest(BaseModel):
    grade: int = Field(..., ge=8, le=10, description="Grade level (8-10)")
    chapter: str = Field(..., min_length=1, description="Chapter name")
    question: str = Field(..., min_length=5, description="Student question")
    student_answer: str = Field(..., description="Student's answer")
    correct_answer: str = Field(..., description="Correct answer")
    expected_type: str = Field(default="text", description="Answer type")


class CheckAnswerResponse(BaseModel):
    correct: bool
    explanation: str
    mistake: Optional[str] = None


# ========================
# Helper Functions
# ========================
def normalize(ans: str) -> str:
    """Normalize answer for comparison."""
    return ans.strip().replace(" ", "").lower()


def check_correctness(student: str, correct: str, expected: str) -> tuple[bool, Optional[str]]:
    """Check if student answer matches correct answer."""
    s = normalize(student)
    c = normalize(correct)

    if expected == "integer":
        try:
            return int(s) == int(c), None
        except ValueError:
            return False, "Answer is not a valid integer"

    if expected == "polynomial":
        is_correct = s == c
        return is_correct, None if is_correct else "Polynomial terms or signs are incorrect"

    # Default: exact match after normalization
    is_correct = s == c
    return is_correct, None if is_correct else "Answer does not match expected result"


# ========================
# API Endpoints
# ========================
@app.post("/check-answer", response_model=CheckAnswerResponse)
def check_answer(data: CheckAnswerRequest) -> CheckAnswerResponse:
    """
    Check student answer and provide explanation.
    
    1️⃣ Validate student answer
    2️⃣ Retrieve top concepts from Supabase
    3️⃣ Generate explanation via Hugging Face
    """
    try:
        logger.info(f"Checking answer for grade {data.grade}, chapter {data.chapter}")
        
        # 1️⃣ Validate answer correctness
        correct, mistake = check_correctness(
            data.student_answer,
            data.correct_answer,
            data.expected_type
        )

        # 2️⃣ Retrieve top concepts from Supabase
        concepts = retrieve_concepts(
            query_text=f"{data.chapter}: {data.question}",
            grade=data.grade,
            top_k=5
        )

        if not concepts:
            logger.warning(f"No concepts found for {data.chapter}")

        # 3️⃣ Generate explanation via Hugging Face
        explanation = generate_explanation(
            question=data.question,
            student_answer=data.student_answer,
            correct_answer=data.correct_answer,
            expected_type=data.expected_type,
            concepts=concepts
        )

        logger.info(f"Successfully generated response for grade {data.grade}")
        
        return CheckAnswerResponse(
            correct=correct,
            explanation=explanation,
            mistake=mistake
        )
        
    except Exception as e:
        logger.error(f"Error checking answer: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/health")
def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}
