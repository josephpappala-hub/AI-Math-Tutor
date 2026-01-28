import json
import os
from openai import OpenAI
from supabase_client import supabase
import logging

logger = logging.getLogger(__name__)

# Initialize OpenAI (uses OPENAI_API_KEY from .env)
client = OpenAI()

def upload_concepts_from_json(file_path: str, grade: int):
    """Upload concepts from JSON file to Supabase."""
    try:
        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            return
            
        with open(file_path, "r", encoding="utf-8") as f:
            concepts = json.load(f)

        logger.info(f"Uploading {len(concepts)} concepts for grade {grade}")
        
        for i, concept in enumerate(concepts):
            # Generate embedding for concept text
            concept_text = concept.get("concept_name", "") + " " + concept.get("definition", "")
            
            embedding = client.embeddings.create(
                model="text-embedding-3-small",
                input=concept_text
            ).data[0].embedding

            # Insert into Supabase
            supabase.table("concepts").insert({
                "concept_name": concept.get("concept_name"),
                "definition": concept.get("definition"),
                "grade": grade,
                "embedding": embedding
            }).execute()
            
            if (i + 1) % 10 == 0:
                logger.info(f"Uploaded {i + 1}/{len(concepts)} concepts")
        
        logger.info(f"Successfully uploaded all concepts from {file_path}")
        
    except Exception as e:
        logger.error(f"Error uploading concepts: {str(e)}")
        raise

if __name__ == "__main__":
    # Example usage
    upload_concepts_from_json("concepts/grade_10/circles.json", grade=10)
