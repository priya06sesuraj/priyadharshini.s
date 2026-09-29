# EduGenie – Gemini Powered Learning Assistant

## Setup
1. Python 3.10+ install pannunga.
2. Terminal la project folder ku poga:
   ```
   python -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. `.env.example` a copy panni `.env` nu rename pannunga, unga Gemini API key podunga
   (https://aistudio.google.com -> Get API key).
4. Run:
   ```
   uvicorn main:app --reload
   ```
5. Browser la open: http://127.0.0.1:8000

## Notes
- Explain task: first time LaMini-Flan-T5-783M model download aagum (~3GB). Load aagalana automatic ah Gemini use pannum.
- Model name change panna `.env` la `GEMINI_MODEL` maathunga.
