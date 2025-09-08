from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from database import Base

class FAQ(Base):
    __tablename__ = "faqs"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, unique=True, index=True)
    answer = Column(Text)
    category = Column(String, index=True)  # e.g., "services", "pricing", "technology"
    keywords = Column(Text)  # comma-separated keywords for better search
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    technologies = Column(Text)  # comma-separated tech stack
    industry = Column(String, index=True)
    client_name = Column(String)
    project_url = Column(String)
    image_url = Column(String)
    metrics = Column(Text)  # JSON string for project metrics
    case_study_url = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    logo_url = Column(String)
    industry = Column(String, index=True)
    website = Column(String)
    testimonial = Column(Text)
    testimonial_author = Column(String)
    testimonial_position = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class CompanyInfo(Base):
    __tablename__ = "company_info"
    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, default="TechTicks")
    tagline = Column(String, default="WE BUILD THE FUTURE OPTIMAL AND INTELLIGENT SOFTWARE SOLUTIONS")
    description = Column(Text, default="Techticks, a premier software development firm, has been empowering startups and SMEs to thrive since 2020.")
    website = Column(String, default="https://techticks.io/")
    linkedin = Column(String, default="https://www.linkedin.com/company/102528746/admin/dashboard/")
    upwork = Column(String, default="https://www.upwork.com/agencies/techticks/")
    phone = Column(String, default="+1 (983) 212-4713")
    email = Column(String, default="info@techticks.io")
    address = Column(String, default="500 N GRANT ST STE R DENVER, CO 80203")
    founded_year = Column(Integer, default=2020)
    total_projects = Column(Integer, default=200)
    total_clients = Column(Integer, default=500)
    total_countries = Column(Integer, default=50)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
