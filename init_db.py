#!/usr/bin/env python3
"""
Initialize the database with all tables
"""

from database import engine, Base
from models import FAQ, Project, Client, CompanyInfo, User, ChatSession, ChatMessage

def init_database():
    """Create all tables in the database"""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

if __name__ == "__main__":
    init_database()
