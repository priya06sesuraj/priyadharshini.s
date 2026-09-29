from gemini_client import ask_gemini


def get_learning_recommendations(topic: str) -> str:
    return ask_gemini(
        f"Create a structured learning path for '{topic}'. Organize it from "
        "beginner to advanced with timelines, key concepts per stage, and "
        "useful resources (videos, articles, books). Use clear headings and "
        "bullet points."
    )
