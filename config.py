import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "TechTicks Chatbot"
    DATABASE_URL: str = os.getenv("DATABASE_URL")  # NeonDB
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")

settings = Settings()
