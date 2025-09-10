from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from pydantic import BaseModel
from typing import List, Optional
import sys
import os
import json

# Add the backend directory to the path to import simple_faqs
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simple_faqs import search_faqs, get_suggested_questions
from services.llm import ask_gemini
from ready_made_questions import get_questions_by_category, get_all_categories, get_featured_questions, get_questions_for_category
from database import get_db
from models import ChatSession, ChatMessage, User
from routes.auth import get_current_user

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[int] = None
    conversation_history: Optional[List[dict]] = []

class ChatResponse(BaseModel):
    response: str
    related_faqs: List[dict]
    suggested_questions: List[str]
    confidence_score: float

def get_comprehensive_techticks_knowledge() -> str:
    """Get comprehensive TechTicks knowledge base"""
    return """
    TechTicks is a premier software development firm founded in 2020, empowering startups and SMEs to thrive globally.

    COMPANY OVERVIEW:
    - Founded: 2020
    - Mission: "WE BUILD THE FUTURE OPTIMAL AND INTELLIGENT SOFTWARE SOLUTIONS"
    - Description: A premier software development firm empowering startups and SMEs to thrive
    - Location: 500 N GRANT ST STE R DENVER, CO 80203, USA
    - Contact: +1 (983) 212-4713, info@techticks.io

    SERVICES:
    1. AI Development and Integration - Advanced AI solutions, machine learning, automation
    2. DevOps and Deployment - Streamlined delivery, automated infrastructure, enhanced agility
    3. Web App Development - Innovative web apps with seamless UX, top performance, scalable design
    4. Mobile App Development - User-focused, innovative mobile apps for iOS, Android, React Native, Flutter
    5. Search Engine Optimization - Digital marketing and SEO services
    6. Quality Assurance - Comprehensive QA & testing services ensuring high standards

    INDUSTRIES SERVED:
    Travel, SaaS, Automobile, Healthcare, Education, Logistics, Fintech

    TECHNOLOGIES:
    React, Next.js, Node.js, Python, TypeScript, AI/ML frameworks, AWS, Supabase, PostgreSQL, MongoDB, Docker, Kubernetes

    COMPANY STATS:
    - 200+ Projects Completed
    - 500+ Happy Customers
    - 50+ Global Countries
    - 200+ Positive Reviews

    CASE STUDIES & SUCCESS STORIES:
    1. Expeerly - Video Review Platform: 40.7% increase in conversion rates, Next.js, Tailwind CSS, PostgreSQL, Supabase, MUX
    2. HeroGeneration - AI Caregiver Support: 50% improvement in caregiving efficiency, React Native, Next.js, NestJS, PostgreSQL
    3. Supermeme.ai - AI Meme Generator: $5,000 MRR with 500,000+ organic users, Node.js, Next.js, TypeScript, Supabase, OpenAI API
    4. EDC4IT - IT Training Platform: 70% faster learning with hands-on training, Docker, Next.js, TypeScript, React.js, Tailwind CSS
    5. OCM Solution - Change Management Platform: 143% ROI vs 35% without change management, Node.js, MySQL, Sequelize, React, MongoDB
    6. WorkHQ - AI Recruiting Platform: 70% faster hiring, React, AWS Lambda, Node.js, Amazon DynamoDB

    CLIENT TESTIMONIALS:
    - Expeerly CEO: "TechTicks delivered exceptional results for our video review platform. The 40.7% increase in conversion rates speaks for itself."
    - HeroGeneration Founder: "The AI-driven caregiver support system has revolutionized our operations. We've seen a 50% improvement in caregiving efficiency."
    - Supermeme.ai Founder: "TechTicks helped us achieve $5,000 MRR with over 500,000 organic users. Their AI integration expertise was exactly what we needed."

    DEVELOPMENT PROCESS:
    1. Requirement gathering
    2. Documentation
    3. Planning
    4. Development
    5. Quality assurance
    6. Deployment
    7. Launch
    8. Maintenance

    SOCIAL MEDIA & LINKS:
    - Website: https://techticks.io/
    - LinkedIn: https://www.linkedin.com/company/102528746/
    - Upwork: https://www.upwork.com/agencies/techticks/

    PRICING & APPROACH:
    - Competitive rates for startups and SMEs
    - Cost-effective solutions
    - Project timelines: 4-8 weeks for simple projects, 3-6 months for complex enterprise solutions
    - Client-centered approach with reliable support
    """

def generate_ai_response(message: str, related_faqs: List[dict]) -> str:
    """Generate AI response using Gemini API with comprehensive TechTicks knowledge"""
    
    # Build context with related FAQs
    faq_context = ""
    if related_faqs:
        faq_context = "\n\nRELEVANT FAQS:\n"
        for faq in related_faqs:
            faq_context += f"Q: {faq['question']}\nA: {faq['answer']}\n\n"
    
    # Create comprehensive prompt for Gemini
    prompt = f"""
    You are an AI assistant for TechTicks, a premier software development company. 
    Answer the user's question about TechTicks using the comprehensive knowledge base below.
    Be helpful, professional, and provide specific details when available.
    If the question is not directly about TechTicks, politely redirect to TechTicks services.

    USER QUESTION: {message}

    TECHTICKS KNOWLEDGE BASE:
    {get_comprehensive_techticks_knowledge()}
    {faq_context}

    INSTRUCTIONS:
    - Provide accurate, helpful information about TechTicks.
    - Include specific details, metrics, and examples when relevant.
    - Be conversational and professional.
    - If asked about services, mention specific case studies and technologies.
    - If asked about pricing, mention competitive rates and contact for quotes.
    - If asked about contact, provide all contact information.
    - Keep responses concise but informative.
    - Always maintain a positive, professional tone representing TechTicks.
    - IMPORTANT: Format the entire answer in clean Markdown with:
      - A short bolded summary line at the top
      - Bullet points for lists and key facts
      - Subheadings (###) for sections when useful
      - Inline links where appropriate
      - No surrounding backticks unless showing code

    RESPONSE (Markdown only):
    """
    
    try:
        # Use Gemini API to generate response
        response = ask_gemini(prompt)
        return response
    except Exception as e:
        # Fallback to simple response if Gemini fails
        return f"Thank you for your question about '{message}'. TechTicks is a premier software development firm specializing in AI development, web and mobile apps, DevOps, and more. We've completed 200+ projects for 500+ clients across 50+ countries. For specific information, please contact us at info@techticks.io or visit https://techticks.io/"

@router.post("/chat")
async def chat(req: ChatRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    # Get or create chat session
    if req.session_id:
        session = db.query(ChatSession).filter(
            ChatSession.id == req.session_id,
            ChatSession.user_id == current_user.id
        ).first()
        if not session:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Session not found"
            )
    else:
        # Create new session if none provided
        session = ChatSession(
            user_id=current_user.id,
            session_name="New Chat",
            is_guest_session=current_user.is_guest
        )
        db.add(session)
        db.commit()
        db.refresh(session)
    
    # Store user message
    user_message = ChatMessage(
        session_id=session.id,
        role="user",
        content=req.message
    )
    db.add(user_message)
    
    # Search for relevant FAQs
    search_query = req.message.lower()
    relevant_faqs = search_faqs(search_query)
    
    # Get suggested questions from related categories
    suggested_questions = []
    if relevant_faqs:
        categories = [faq["category"] for faq in relevant_faqs]
        for category in categories:
            category_questions = get_suggested_questions(category)
            suggested_questions.extend(category_questions)
        # Remove duplicates and limit
        suggested_questions = list(set(suggested_questions))[:5]
    else:
        suggested_questions = get_suggested_questions()
    
    # Generate AI response
    ai_response = generate_ai_response(req.message, relevant_faqs)
    
    # Calculate confidence score based on FAQ relevance
    confidence_score = min(0.9, 0.3 + (len(relevant_faqs) * 0.2))
    
    # Store assistant message
    assistant_message = ChatMessage(
        session_id=session.id,
        role="assistant",
        content=ai_response,
        related_faqs=json.dumps(relevant_faqs) if relevant_faqs else None,
        suggested_questions=json.dumps(suggested_questions) if suggested_questions else None,
        confidence_score=str(confidence_score)
    )
    db.add(assistant_message)
    
    # Update session timestamp
    session.updated_at = func.now()
    
    db.commit()
    
    return ChatResponse(
        response=ai_response,
        related_faqs=relevant_faqs,
        suggested_questions=suggested_questions,
        confidence_score=confidence_score
    )

@router.get("/chat/suggestions")
async def get_chat_suggestions(
    topic: Optional[str] = None
):
    """Get suggested questions for chat"""
    if topic:
        # Get FAQs related to the topic
        related_faqs = search_faqs(topic)
        return {
            "suggested_questions": [faq["question"] for faq in related_faqs],
            "related_topics": list(set([faq["category"] for faq in related_faqs]))
        }
    
    # Return general suggestions
    general_faqs = get_suggested_questions()
    return {
        "suggested_questions": general_faqs,
        "categories": ["general", "services", "pricing", "technology", "support"]
    }

@router.get("/chat/ready-made-questions")
async def get_ready_made_questions(
    category: Optional[str] = None
):
    """Get ready-made questions organized by categories"""
    if category:
        questions = get_questions_for_category(category)
        return {
            "category": category,
            "questions": questions
        }
    
    # Return all categories with their questions
    all_questions = get_questions_by_category()
    return {
        "categories": all_questions,
        "featured_questions": get_featured_questions()
    }

@router.get("/chat/categories")
async def get_question_categories():
    """Get all available question categories"""
    return {
        "categories": get_all_categories(),
        "featured_questions": get_featured_questions()
    }

@router.get("/chat/sessions/{session_id}/messages")
async def get_session_messages(
    session_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get messages for a specific chat session"""
    session = db.query(ChatSession).filter(
        ChatSession.id == session_id,
        ChatSession.user_id == current_user.id
    ).first()
    
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )
    
    messages = db.query(ChatMessage).filter(
        ChatMessage.session_id == session_id
    ).order_by(ChatMessage.created_at).all()
    
    return [
        {
            "id": msg.id,
            "role": msg.role,
            "content": msg.content,
            "related_faqs": json.loads(msg.related_faqs) if msg.related_faqs else None,
            "suggested_questions": json.loads(msg.suggested_questions) if msg.suggested_questions else None,
            "confidence_score": float(msg.confidence_score) if msg.confidence_score else None,
            "created_at": msg.created_at
        }
        for msg in messages
    ]

@router.get("/chat/sessions")
async def get_user_sessions(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all chat sessions for the current user"""
    sessions = db.query(ChatSession).filter(
        ChatSession.user_id == current_user.id
    ).order_by(ChatSession.updated_at.desc()).all()
    
    return [
        {
            "id": session.id,
            "session_name": session.session_name,
            "is_guest_session": session.is_guest_session,
            "created_at": session.created_at,
            "updated_at": session.updated_at,
            "message_count": len(session.messages)
        }
        for session in sessions
    ]


