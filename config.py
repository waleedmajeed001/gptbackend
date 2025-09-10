import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "TechTicks Chatbot"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://neondb_owner:npg_iSovf6EF1xQK@ep-cold-recipe-addin5xk-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "AIzaSyD99HAlUqCojaxTwf8I-zrpcQGVfOxrXoU")

settings = Settings()
