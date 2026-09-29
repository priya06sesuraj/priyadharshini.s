import json
import re
from gemini_client import ask_gemini


def clean_json_block(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```(?:json)?", "", text).strip()
    text = re.sub(r"```$", "", text).strip()
    return text


def generate_quiz(text: str):
    prompt = (
        "Create exactly 3 multiple-choice questions from the topic/passage "
        "below. Return ONLY valid JSON: a list of objects with keys "
        '"question", "options" (list of 4 strings) and "answer" (must be '
        "exactly one of the options).\n\n" + text
    )
    raw = ask_gemini(prompt)
    if raw.startswith("Error:"):
        return {"error": raw}
    try:
        quiz = json.loads(clean_json_block(raw))
        if not isinstance(quiz, list):
            raise ValueError("Response is not a list")
        return quiz
    except Exception as e:
        return {"error": f"Could not parse quiz JSON: {e}", "raw": raw}
