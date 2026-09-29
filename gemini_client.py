import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
_client = None


def ask_gemini(prompt: str) -> str:
    global _client
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        return "Error: GEMINI_API_KEY not set. Create a .env file (see .env.example)."
    try:
        if _client is None:
            _client = genai.Client(api_key=key)
        resp = _client.models.generate_content(model=MODEL, contents=prompt)
        return resp.text or "Error: empty response from model."
    except Exception as e:
        return f"Error: {e}"
