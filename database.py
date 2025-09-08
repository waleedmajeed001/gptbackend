from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings
import os

# Ensure the database directory exists
db_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(db_dir, exist_ok=True)

# Use the database URL from settings (Neon for production, SQLite for local)
DATABASE_URL = settings.DATABASE_URL

# For SQLite, ensure the database directory exists
if "sqlite" in DATABASE_URL:
    db_path = os.path.join(db_dir, "techticks.db")
    DATABASE_URL = f"sqlite:///{db_path}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
