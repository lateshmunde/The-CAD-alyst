import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
key = os.getenv("GOOGLE_API_KEY")

print(f"Testing Key: {key[:8]}... (last 4: {key[-4:]})")

client = genai.Client(api_key=key)

print("\n--- Available Models on your Key ---")
try:
    # In the new SDK, we just print the names directly to see what's there
    for model in client.models.list():
        print(f"USE THIS STRING: {model.name}")
except Exception as e:
    print(f"Failed to list models: {e}")
