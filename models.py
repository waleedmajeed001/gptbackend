from sqlalchemy import Column, Integer, String, Text
from database import Base

class FAQ(Base):
    __tablename__ = "faqs"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, unique=True, index=True)
    answer = Column(Text)

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    logo_url = Column(String)

class CompanyInfo(Base):
    __tablename__ = "company_info"
    id = Column(Integer, primary_key=True, index=True)
    tagline = Column(String)
    website = Column(String)
    linkedin = Column(String)
    upwork = Column(String)
