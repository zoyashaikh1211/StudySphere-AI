import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv(Path(__file__).parent.parent / ".env")

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_summary(text):
    prompt = f"""
Summarize the following study notes into concise bullet points.
Keep the language simple and exam-oriented.

Notes:
{text}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception:
        return "⚠️ Gemini is currently busy. Please try again in a minute."


def generate_keypoints(text):
    prompt = f"""
Extract 10 important key points from these notes.

Notes:
{text}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception:
        return "⚠️ Gemini is currently busy. Please try again in a minute."


def generate_flashcards(text):
    prompt = f"""
Create 10 flashcards.

Format:
Q: Question
A: Answer

Notes:
{text}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception:
        return "⚠️ Gemini is currently busy. Please try again in a minute."


def generate_quiz(text):
    prompt = f"""
Create 10 MCQs.

Notes:
{text}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception:
        return "⚠️ Gemini is currently busy. Please try again in a minute."

