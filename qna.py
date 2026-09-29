from gemini_client import ask_gemini


def answer_question(question: str) -> str:
    return ask_gemini(
        "You are a helpful teacher. Answer clearly and concisely:\n" + question
    )
