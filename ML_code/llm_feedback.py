# app/llm_feedback.py
import openai

openai.api_key = "AIzaSyD5935VpdFvmfTbsVaZvM7Eu4a_o0vSpGw3285"

def get_llm_feedback(question: str, answer: str):
    prompt = f"""
    You are an expert interview coach. Analyze the following response to an interview question.
    
    Question: "{question}"
    Response: "{answer}"
    
    Provide constructive feedback on tone, structure, clarity, and professional impact. Suggest improvements if necessary.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message["content"]
