from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from qna import answer_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app = FastAPI(title="EduGenie")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class Query(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.post("/qa")
def qa(q: Query):
    return {"result": answer_question(q.text)}


@app.post("/explain")
def explain(q: Query):
    return {"result": explain_concept(q.text)}


@app.post("/quiz")
def quiz(q: Query):
    return {"result": generate_quiz(q.text)}


@app.post("/summarize")
def summarize(q: Query):
    return {"result": summarize_text(q.text)}


@app.post("/learn/recommendations")
def learn(q: Query):
    return {"result": get_learning_recommendations(q.text)}
