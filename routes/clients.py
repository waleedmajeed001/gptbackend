from typing import List

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import get_db
from models import Client, CompanyInfo


router = APIRouter()


class ClientCreate(BaseModel):
    name: str
    logo_url: str


class ClientOut(BaseModel):
    id: int
    name: str
    logo_url: str

    class Config:
        from_attributes = True


class CompanyInfoCreate(BaseModel):
    tagline: str | None = None
    website: str | None = None
    linkedin: str | None = None
    upwork: str | None = None


class CompanyInfoOut(CompanyInfoCreate):
    id: int

    class Config:
        from_attributes = True


@router.get("/", response_model=List[ClientOut])
def list_clients(db: Session = Depends(get_db)):
    return db.query(Client).all()


@router.post("/", response_model=ClientOut)
def create_client(data: ClientCreate, db: Session = Depends(get_db)):
    client = Client(name=data.name, logo_url=data.logo_url)
    db.add(client)
    db.commit()
    db.refresh(client)
    return client


@router.get("/company", response_model=CompanyInfoOut | None)
def get_company_info(db: Session = Depends(get_db)):
    return db.query(CompanyInfo).first()


@router.post("/company", response_model=CompanyInfoOut)
def upsert_company_info(data: CompanyInfoCreate, db: Session = Depends(get_db)):
    info = db.query(CompanyInfo).first()
    if info is None:
        info = CompanyInfo(**data.model_dump())
        db.add(info)
    else:
        for key, value in data.model_dump().items():
            setattr(info, key, value)
    db.commit()
    db.refresh(info)
    return info


