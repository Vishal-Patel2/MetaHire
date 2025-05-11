# app/interview_model.py
import random
import json

def load_questions():
    with open("app/questions.json", "r") as f:
        return json.load(f)

def get_random_question():
    questions = load_questions()
    return random.choice(questions)
