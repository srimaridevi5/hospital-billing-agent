import google.generativeai as genai

from app.config import settings

genai.configure(api_key=settings.GOOGLE_API_KEY)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def ask_gemini(prompt: str):

    response = model.generate_content(prompt)

    return response.text