from typing import List

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import get_db
from models import Project


router = APIRouter()


class ProjectCreate(BaseModel):
    name: str
    description: str
    technologies: str = ""
    industry: str = ""
    client_name: str = ""
    project_url: str = ""
    image_url: str = ""
    metrics: str = ""
    case_study_url: str = ""


class ProjectOut(BaseModel):
    id: int
    name: str
    description: str
    technologies: str
    industry: str
    client_name: str
    project_url: str
    image_url: str
    metrics: str
    case_study_url: str

    class Config:
        from_attributes = True


@router.get("/", response_model=List[ProjectOut])
def list_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()


@router.post("/", response_model=ProjectOut)
def create_project(data: ProjectCreate, db: Session = Depends(get_db)):
    project = Project(
        name=data.name,
        description=data.description,
        technologies=data.technologies,
        industry=data.industry,
        client_name=data.client_name,
        project_url=data.project_url,
        image_url=data.image_url,
        metrics=data.metrics,
        case_study_url=data.case_study_url
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


