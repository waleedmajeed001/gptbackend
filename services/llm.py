import google.generativeai as genai

from config import settings


genai.configure(api_key=settings.GEMINI_API_KEY)


def ask_gemini(prompt: str) -> str:
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text


