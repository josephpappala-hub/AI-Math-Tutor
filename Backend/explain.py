from dotenv import load_dotenv
import os
import logging
import requests

load_dotenv()

logger = logging.getLogger(__name__)

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
HF_ENDPOINT = "https://router.huggingface.co/models/google/flan-t5-small"

if not HUGGINGFACE_API_KEY:
    raise ValueError("HUGGINGFACE_API_KEY must be set in .env file")


def generate_explanation(
    question: str,
    student_answer: str,
    correct_answer: str,
    expected_type: str,
    concepts: list[dict]
) -> str:
    """Generate explanation for student answer using HuggingFace API."""
    try:
        concept_block = "\n".join(
            f"- {c.get('concept_name', 'Unknown')}: {c.get('definition', '')}"
            for c in concepts
        ) if concepts else "No relevant concepts available"

        prompt = f"""You are a Telangana State Board mathematics teacher.

Student question: {question}
Student answer: {student_answer}
Correct answer: {correct_answer}
Answer type: {expected_type}

Relevant concepts:
{concept_block}

Explain step-by-step why the answer is correct or incorrect. Keep it short and clear."""

        headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
        
        payload = {
            "inputs": prompt,
            "options": {
                "wait_for_model": True
            }
        }

        logger.info("Sending request to HuggingFace router endpoint")
        
        response = requests.post(
            HF_ENDPOINT,
            headers=headers,
            json=payload,
            timeout=60
        )

        logger.info(f"HuggingFace API response status: {response.status_code}")
        
        output = response.json()
        
        # Handle error response from API
        if isinstance(output, dict) and "error" in output:
            logger.error(f"HuggingFace API error: {output['error']}")
            return f"Error: {output['error']}"
        
        # Handle successful response
        if isinstance(output, list) and len(output) > 0:
            generated_text = output[0].get("generated_text", "")
            if generated_text:
                logger.info("Successfully generated explanation")
                return generated_text.strip()
        
        logger.warning(f"Unexpected response format: {output}")
        return "Error: Unable to generate explanation"
            
    except requests.exceptions.Timeout:
        logger.error("HuggingFace API request timed out (60 seconds)")
        return "Error: Request timed out. Please try again."
    except requests.exceptions.RequestException as e:
        logger.error(f"HuggingFace API request error: {str(e)}")
        return f"Error: {str(e)}"
    except Exception as e:
        logger.error(f"Error generating explanation: {str(e)}")
        return f"Error: {str(e)}"
