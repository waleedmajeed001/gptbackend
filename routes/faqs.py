from typing import List, Optional
from fastapi import APIRouter, Query
from pydantic import BaseModel
import sys
import os

# Add the backend directory to the path to import simple_faqs
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simple_faqs import FAQS, search_faqs, get_suggested_questions

router = APIRouter()

class FAQCreate(BaseModel):
    question: str
    answer: str
    category: Optional[str] = "general"
    keywords: Optional[str] = ""

class FAQUpdate(BaseModel):
    question: Optional[str] = None
    answer: Optional[str] = None
    category: Optional[str] = None
    keywords: Optional[str] = None

class FAQOut(BaseModel):
    id: int
    question: str
    answer: str
    category: str
    keywords: str

    class Config:
        from_attributes = True

class FAQSearchResponse(BaseModel):
    faqs: List[FAQOut]
    suggested_questions: List[str]
    related_categories: List[str]

# In-memory storage for dynamic FAQs
dynamic_faqs = FAQS.copy()
next_id = len(dynamic_faqs) + 1

@router.get("/", response_model=List[FAQOut])
def list_faqs(
    category: Optional[str] = Query(None, description="Filter by category")
):
    if category:
        return [faq for faq in dynamic_faqs if faq["category"] == category]
    return dynamic_faqs

@router.get("/categories")
def get_faq_categories():
    categories = list(set([faq["category"] for faq in dynamic_faqs]))
    return {"categories": categories}

@router.get("/search", response_model=FAQSearchResponse)
def search_faqs_endpoint(
    q: str = Query(..., description="Search query"),
    category: Optional[str] = Query(None, description="Filter by category")
):
    # Search in questions, answers, and keywords
    search_query = q.lower()
    
    query = [faq for faq in dynamic_faqs if (
        search_query in faq["question"].lower() or
        search_query in faq["answer"].lower() or
        search_query in faq["keywords"].lower()
    )]
    
    if category:
        query = [faq for faq in query if faq["category"] == category]
    
    # Get suggested questions based on search
    suggested_questions = []
    if query:
        categories = [faq["category"] for faq in query]
        for cat in categories:
            cat_questions = [faq["question"] for faq in dynamic_faqs if faq["category"] == cat]
            suggested_questions.extend(cat_questions)
        suggested_questions = list(set(suggested_questions))[:5]
    
    # Get related categories
    related_categories = list(set([faq["category"] for faq in query]))
    
    return FAQSearchResponse(
        faqs=query,
        suggested_questions=suggested_questions,
        related_categories=related_categories
    )

@router.post("/", response_model=FAQOut)
def create_faq(data: FAQCreate):
    global next_id
    
    # Check if FAQ already exists
    for faq in dynamic_faqs:
        if faq["question"] == data.question:
            return faq
    
    new_faq = {
        "id": next_id,
        "question": data.question,
        "answer": data.answer,
        "category": data.category,
        "keywords": data.keywords
    }
    
    dynamic_faqs.append(new_faq)
    next_id += 1
    
    return new_faq

@router.put("/{faq_id}", response_model=FAQOut)
def update_faq(faq_id: int, data: FAQUpdate):
    for faq in dynamic_faqs:
        if faq["id"] == faq_id:
            for field, value in data.dict(exclude_unset=True).items():
                faq[field] = value
            return faq
    
    return {"error": "FAQ not found"}

@router.delete("/{faq_id}")
def delete_faq(faq_id: int):
    global dynamic_faqs
    original_length = len(dynamic_faqs)
    dynamic_faqs = [faq for faq in dynamic_faqs if faq["id"] != faq_id]
    
    if len(dynamic_faqs) < original_length:
        return {"message": "FAQ deleted successfully"}
    return {"error": "FAQ not found"}

@router.get("/suggestions")
def get_faq_suggestions(
    topic: Optional[str] = Query(None, description="Topic to get suggestions for")
):
    if topic:
        # Get FAQs related to the topic
        related_faqs = search_faqs(topic)
        
        # Get suggested questions from related categories
        categories = [faq["category"] for faq in related_faqs]
        suggested_questions = []
        
        for cat in categories:
            cat_questions = [faq["question"] for faq in dynamic_faqs if faq["category"] == cat]
            suggested_questions.extend(cat_questions)
        
        return {
            "related_faqs": related_faqs,
            "suggested_questions": list(set(suggested_questions))[:5]
        }
    
    # Return general suggestions
    general_faqs = [faq for faq in dynamic_faqs if faq["category"] == "general"]
    return {
        "general_faqs": general_faqs,
        "categories": list(set([faq["category"] for faq in dynamic_faqs]))
    }


