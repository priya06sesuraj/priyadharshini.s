"""Concept explanation using local LaMini-Flan-T5-783M.
Falls back to Gemini if the local model cannot be loaded."""
from gemini_client import ask_gemini

_pipe = None
_failed = False


def _load():
    global _pipe, _failed
    if _pipe is None and not _failed:
        try:
            from transformers import pipeline
            _pipe = pipeline("text2text-generation",
                             model="MBZUAI/LaMini-Flan-T5-783M")
        except Exception as e:
            print("Local model unavailable, using Gemini:", e)
            _failed = True
    return _pipe


def explain_concept(topic: str) -> str:
    pipe = _load()
    if pipe is None:
        return ask_gemini("Explain in very simple words for a beginner:\n" + topic)
    out = pipe(f"Explain in simple words: {topic}",
               max_length=300, do_sample=True, temperature=0.4)
    return out[0]["generated_text"]
