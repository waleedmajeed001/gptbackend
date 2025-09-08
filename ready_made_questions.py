#!/usr/bin/env python3
"""
Ready-made questions for TechTicks chat interface
Organized by categories like Xseven website
"""

READY_MADE_QUESTIONS = {
    "services": {
        "title": "Our Services",
        "icon": "🚀",
        "questions": [
            "What services does TechTicks provide?",
            "Tell me about your AI development services",
            "Do you provide web application development?",
            "What mobile app development services do you offer?",
            "Can you help with DevOps and deployment?",
            "Do you offer SEO and digital marketing services?",
            "What quality assurance services do you provide?",
            "Can you help with cloud migration?"
        ]
    },
    "technologies": {
        "title": "Technologies & Stack",
        "icon": "💻",
        "questions": [
            "What technologies does TechTicks use?",
            "Do you work with React and Next.js?",
            "Can you develop with Python and AI/ML?",
            "Do you use cloud platforms like AWS?",
            "What databases do you work with?",
            "Do you develop mobile apps with React Native?",
            "Can you help with blockchain development?",
            "Do you work with modern DevOps tools?"
        ]
    },
    "industries": {
        "title": "Industries We Serve",
        "icon": "🏢",
        "questions": [
            "What industries does TechTicks specialize in?",
            "Do you have experience in healthcare technology?",
            "Can you help fintech companies?",
            "Do you work with SaaS startups?",
            "Have you worked with education technology?",
            "Do you serve the travel industry?",
            "Can you help automotive companies?",
            "Do you work with logistics companies?"
        ]
    },
    "case_studies": {
        "title": "Success Stories",
        "icon": "📈",
        "questions": [
            "Tell me about your case studies",
            "What results did you achieve for Expeerly?",
            "How did you help HeroGeneration improve efficiency?",
            "Tell me about the Supermeme.ai project",
            "What did you build for EDC4IT?",
            "How did OCM Solution achieve 143% ROI?",
            "Tell me about the WorkHQ recruiting platform",
            "What are your biggest success stories?"
        ]
    },
    "pricing": {
        "title": "Pricing & Process",
        "icon": "💰",
        "questions": [
            "What are your pricing options?",
            "How much does a typical project cost?",
            "Do you offer flexible payment plans?",
            "What's included in your development process?",
            "How long does a project typically take?",
            "Do you provide project maintenance?",
            "What's your development methodology?",
            "Do you offer post-launch support?"
        ]
    },
    "company": {
        "title": "About TechTicks",
        "icon": "🏆",
        "questions": [
            "Tell me about TechTicks company",
            "How long has TechTicks been in business?",
            "What makes TechTicks different?",
            "How many projects have you completed?",
            "How many clients do you serve?",
            "What's your company mission?",
            "Where is TechTicks located?",
            "What awards or recognition have you received?"
        ]
    },
    "contact": {
        "title": "Get In Touch",
        "icon": "📞",
        "questions": [
            "How can I contact TechTicks?",
            "What's your phone number?",
            "What's your email address?",
            "Where is your office located?",
            "Do you offer free consultations?",
            "How quickly do you respond to inquiries?",
            "Can I schedule a meeting?",
            "What are your business hours?"
        ]
    },
    "quick_start": {
        "title": "Quick Start",
        "icon": "⚡",
        "questions": [
            "I need a web application - can you help?",
            "I want to build a mobile app - where do I start?",
            "I need AI integration for my business",
            "I want to modernize my existing software",
            "I need help with cloud deployment",
            "I want to improve my website performance",
            "I need a custom software solution",
            "I want to automate my business processes"
        ]
    }
}

def get_questions_by_category(category: str = None):
    """Get questions by category or all questions"""
    if category and category in READY_MADE_QUESTIONS:
        return READY_MADE_QUESTIONS[category]
    return READY_MADE_QUESTIONS

def get_all_categories():
    """Get all available categories"""
    return list(READY_MADE_QUESTIONS.keys())

def get_featured_questions():
    """Get featured questions for quick access"""
    return [
        "What services does TechTicks provide?",
        "Tell me about your AI development services",
        "What technologies do you use?",
        "How can I contact TechTicks?",
        "Tell me about your case studies",
        "What are your pricing options?",
        "Do you provide mobile app development?",
        "What makes TechTicks different?"
    ]

def get_questions_for_category(category: str):
    """Get questions for a specific category"""
    if category in READY_MADE_QUESTIONS:
        return READY_MADE_QUESTIONS[category]["questions"]
    return []

if __name__ == "__main__":
    print("📋 TechTicks Ready-Made Questions")
    print("=" * 50)
    
    for category, data in READY_MADE_QUESTIONS.items():
        print(f"\n{data['icon']} {data['title']}")
        print("-" * 30)
        for question in data['questions'][:3]:  # Show first 3 questions
            print(f"• {question}")
        if len(data['questions']) > 3:
            print(f"  ... and {len(data['questions']) - 3} more")
    
    print(f"\n📊 Total Categories: {len(READY_MADE_QUESTIONS)}")
    total_questions = sum(len(data['questions']) for data in READY_MADE_QUESTIONS.values())
    print(f"📊 Total Questions: {total_questions}")
