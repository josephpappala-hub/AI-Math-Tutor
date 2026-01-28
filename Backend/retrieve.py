from supabase_client import supabase
import logging
from typing import Any, cast
import requests
import os

logger = logging.getLogger(__name__)

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
HUGGINGFACE_EMBED_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"


def embed_text(text: str) -> list[float]:
    """Convert text to embedding vector using HuggingFace API."""
    try:
        if not text or not text.strip():
            raise ValueError("Text cannot be empty")
        
        headers = {
            "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(
            HUGGINGFACE_EMBED_URL,
            headers=headers,
            json={"inputs": text.strip()},
            timeout=30
        )
        
        if response.status_code == 200:
            embedding = response.json()
            if isinstance(embedding, list) and len(embedding) > 0:
                return embedding[0] if isinstance(embedding[0], list) else embedding
            return embedding
        else:
            logger.error(f"HuggingFace embedding API error: {response.status_code}")
            raise Exception(f"Embedding failed: {response.text}")
            
    except Exception as e:
        logger.error(f"Error embedding text: {str(e)}")
        raise


def retrieve_concepts(
    query_text: str,
    grade: int,
    top_k: int = 5
) -> list[dict[str, Any]]:
    """
    Retrieve relevant concepts from Supabase using semantic search.
    
    Args:
        query_text: The question or topic to search for
        grade: Grade level (8, 9, or 10)
        top_k: Number of concepts to retrieve (default 5)
    
    Returns:
        List of concept dictionaries with name and definition
    """
    try:
        if grade not in [8, 9, 10]:
            logger.warning(f"Invalid grade {grade}, using grade 8")
            grade = 8
            
        query_embedding = embed_text(query_text)

        response = supabase.rpc(
            "match_concepts",
            {
                "query_embedding": query_embedding,
                "match_count": min(top_k, 10),
                "filter_grade": grade
            }
        ).execute()

        concepts: list[dict[str, Any]] = []
        
        if response and hasattr(response, 'data') and response.data:
            data = response.data
            if isinstance(data, list):
                concepts = cast(list[dict[str, Any]], data)
            elif isinstance(data, dict):
                concepts = [cast(dict[str, Any], data)]
        
        logger.info(f"Retrieved {len(concepts)} concepts for grade {grade}")
        return concepts
        
    except Exception as e:
        logger.error(f"Error retrieving concepts: {str(e)}")
        return []
