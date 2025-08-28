from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import get_db
from models import FAQ


router = APIRouter()


class FAQCreate(BaseModel):
    question: str
    answer: str


class FAQOut(BaseModel):
    id: int
    question: str
    answer: str

    class Config:
        from_attributes = True


@router.get("/", response_model=List[FAQOut])
def list_faqs(db: Session = Depends(get_db)):
    return db.query(FAQ).all()


@router.post("/", response_model=FAQOut)
def create_faq(data: FAQCreate, db: Session = Depends(get_db)):
    exists = db.query(FAQ).filter(FAQ.question == data.question).first()
    if exists:
        raise HTTPException(status_code=400, detail="FAQ with this question already exists")
    faq = FAQ(question=data.question, answer=data.answer)
    db.add(faq)
    db.commit()
    db.refresh(faq)
    return faq


