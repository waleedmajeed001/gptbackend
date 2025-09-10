#!/usr/bin/env python3
"""
Drop and recreate all database tables
"""

from database import engine, Base
from models import FAQ, Project, Client, CompanyInfo, User, ChatSession, ChatMessage

def recreate_database():
    """Drop all tables and recreate them"""
    print("Dropping all existing tables...")
    Base.metadata.drop_all(bind=engine)
    
    print("Creating all tables...")
    Base.metadata.create_all(bind=engine)
    
    print("Database tables recreated successfully!")

if __name__ == "__main__":
    recreate_database()

