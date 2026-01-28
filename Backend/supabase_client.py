from dotenv import load_dotenv
import os
from supabase import create_client
import logging

logger = logging.getLogger(__name__)

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    error_msg = "SUPABASE_URL and SUPABASE_KEY must be set in .env file"
    logger.error(error_msg)
    raise ValueError(error_msg)

try:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    logger.info("Supabase client initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize Supabase client: {str(e)}")
    raise