# app/feedback_engine.py

import spacy
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Load spaCy NLP pipeline
nlp = spacy.load("en_core_web_sm")

# Optional: Predefined job-relevant skills to detect
KEY_SKILLS = ["teamwork", "communication", "python", "project management", "leadership", "data analysis", "problem solving"]

def extract_keywords(text):
    doc = nlp(text)
    return list(set([token.lemma_.lower() for token in doc if token.pos_ in ["NOUN", "VERB", "PROPN"] and not token.is_stop]))

def score_grammar(text):
    # Use TextBlob grammar proxy
    blob = TextBlob(text)
    mistakes = len(blob.correct().split()) - len(blob.words)
    grammar_score = max(0, 1 - mistakes / max(1, len(blob.words)))
    return round(grammar_score, 2)

def analyze_response(response: str):
    # Sentiment
    sentiment = TextBlob(response).sentiment
    polarity = round(sentiment.polarity, 2)
    subjectivity = round(sentiment.subjectivity, 2)

    # Keywords and skill matching
    keywords = extract_keywords(response)
    matched_skills = [skill for skill in KEY_SKILLS if skill in keywords]

    # Grammar score
    grammar_score = score_grammar(response)

    # Feedback
    tips = []
    if polarity < 0:
        tips.append("Try using more confident or positive language.")
    if grammar_score < 0.8:
        tips.append("Check your grammar or sentence structure.")
    if not matched_skills:
        tips.append("Try to include relevant skills in your answer.")

    return {
        "sentiment": {
            "polarity": polarity,
            "subjectivity": subjectivity
        },
        "grammar_score": grammar_score,
        "keywords": keywords,
        "matched_skills": matched_skills,
        "tips": tips
    }
