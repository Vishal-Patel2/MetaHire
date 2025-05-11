# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from app.interview_model import get_random_question
from app.feedback_engine import analyze_response

app = FastAPI()

class ResponseModel(BaseModel):
    response: str

@app.get("/question")
def ask_question():
    question = get_random_question()
    return {"question": question}

@app.post("/feedback")
def give_feedback(data: ResponseModel):
    feedback = analyze_response(data.response)
    return feedback
