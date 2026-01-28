# Test script - save as test_huggingface.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
MODEL = "google/flan-t5-small"

prompt = "Solve step-by-step: If twice a number minus 3 is 7, find the number."

# Use the router endpoint
response = requests.post(
    f"https://router.huggingface.co/models/{MODEL}",
    headers={"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"},
    json={"inputs": prompt, "options": {"wait_for_model": True}},
    timeout=120
)

print("Status Code:", response.status_code)
print("Response Text:", response.text)

if response.status_code == 200:
    try:
        result = response.json()
        print("Response JSON:", result)
    except Exception as e:
        print("Error parsing JSON:", str(e))
else:
    print("Error:", response.text)