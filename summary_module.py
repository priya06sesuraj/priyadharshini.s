from gemini_client import ask_gemini


def summarize_text(text: str) -> str:
    return ask_gemini(
        "Summarize the following passage into a concise, easy-to-understand "
        "version. Keep the core information and remove redundancy:\n\n" + text
    )
