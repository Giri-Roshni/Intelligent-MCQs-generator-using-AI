from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_mcqs(syllabus_text, num_questions=50):
    # Trim syllabus to prevent token overflow
    syllabus_text = syllabus_text[:4000]

    prompt = f"""
You are an expert engineering question paper setter.

Using ONLY the syllabus text below, generate exactly {num_questions} multiple choice questions.

Rules:
- Each question must be directly related to the syllabus.
- Engineering university level.
- 4 options per question (A, B, C, D)
- Only one correct answer per question
- No extra explanations
- Strictly follow the topics and wording of the syllabus

SYLLABUS:
{syllabus_text}
"""

    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"ERROR generating MCQs: {str(e)}"
