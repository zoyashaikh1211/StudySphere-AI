import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv(Path(__file__).parent.parent / ".env")

# Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# ---------------- SUMMARY ---------------- #

def generate_summary(text):
    prompt = f"""
    Summarize the following study notes.

    Requirements:
    - Use bullet points
    - Keep language simple
    - Focus on important concepts
    - Make it exam-oriented

    Notes:
    {text}
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"⚠️ Gemini is temporarily busy.\n\n{e}"


# ---------------- KEY POINTS ---------------- #

def generate_keypoints(text):
    prompt = f"""
    Read these notes and extract:

    - 10 important key points
    - Short and easy to revise
    - Bullet points only
    - Focus on exams

    Notes:
    {text}
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"⚠️ Gemini is temporarily busy.\n\n{e}"


# ---------------- FLASHCARDS ---------------- #

def generate_flashcards(text):
    prompt = f"""
    Create 10 flashcards from these notes.

    Format:

    Q: Question

    A: Answer

    Keep answers short and easy to remember.

    Notes:
    {text}
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"⚠️ Gemini is temporarily busy.\n\n{e}"


# ---------------- TEST ---------------- #

if __name__ == "__main__":

    sample = """
    Photosynthesis is the process by which green plants make food
    using sunlight, carbon dioxide and water.
    """

    print(generate_summary(sample))