import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv(Path(__file__).parent.parent / ".env")


# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_summary(text):
    prompt = f"""
    Summarize the following study notes into concise bullet points.
    Keep the language simple and easy to revise.

    Notes:
    {text}
    """

    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

    return response.text


if __name__ == "__main__":
    result = generate_summary(
        "Photosynthesis is the process by which green plants make food using sunlight, carbon dioxide and water."
    )

    print(result)