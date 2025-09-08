import json
import os

# Simple in-memory FAQ storage
FAQS = [
    {
        "id": 1,
        "question": "What services does TechTicks provide?",
        "answer": "TechTicks offers comprehensive software development services including AI Development and Integration, DevOps and Deployment, Web App Development, Mobile App Development, Search Engine Optimization, and Quality Assurance. We specialize in creating intelligent software solutions for startups and SMEs.",
        "category": "services",
        "keywords": "services, development, AI, DevOps, web apps, mobile apps, SEO, QA"
    },
    {
        "id": 2,
        "question": "What industries does TechTicks specialize in?",
        "answer": "We serve multiple industries including Travel, SaaS, Automobile, Healthcare, Education, Logistics, and Fintech. Our team has experience across various sectors and can adapt our solutions to meet industry-specific requirements.",
        "category": "industries",
        "keywords": "travel, SaaS, automobile, healthcare, education, logistics, fintech, industries"
    },
    {
        "id": 3,
        "question": "How much does it cost to develop a custom software solution?",
        "answer": "Our pricing varies based on project complexity, scope, and requirements. We offer competitive rates and work with startups and SMEs to provide cost-effective solutions. Contact us for a detailed quote based on your specific needs.",
        "category": "pricing",
        "keywords": "cost, pricing, budget, quote, affordable, competitive rates"
    },
    {
        "id": 4,
        "question": "What technologies does TechTicks use for development?",
        "answer": "We use modern, cutting-edge technologies including React, Next.js, Node.js, Python, AI/ML frameworks, cloud platforms, and more. Our tech stack is chosen based on project requirements to ensure optimal performance and scalability.",
        "category": "technology",
        "keywords": "technologies, React, Next.js, Node.js, Python, AI, cloud, modern tech"
    },
    {
        "id": 5,
        "question": "How long does it take to complete a project?",
        "answer": "Project timelines depend on complexity and scope. Simple projects may take 4-8 weeks, while complex enterprise solutions can take 3-6 months. We provide detailed timelines during the planning phase and keep you updated throughout development.",
        "category": "timeline",
        "keywords": "timeline, duration, project completion, development time, planning"
    }
]

def search_faqs(query):
    """Simple search function"""
    query = query.lower()
    results = []
    
    for faq in FAQS:
        if (query in faq["question"].lower() or 
            query in faq["answer"].lower() or 
            query in faq["keywords"].lower()):
            results.append(faq)
    
    return results

def get_suggested_questions(category=None):
    """Get suggested questions"""
    if category:
        return [faq["question"] for faq in FAQS if faq["category"] == category]
    return [faq["question"] for faq in FAQS[:5]]

if __name__ == "__main__":
    print("FAQ System Ready!")
    print(f"Total FAQs: {len(FAQS)}")
    
    # Test search
    results = search_faqs("services")
    print(f"Search for 'services' found: {len(results)} results")
    
    # Test suggestions
    suggestions = get_suggested_questions()
    print(f"Suggested questions: {len(suggestions)}")


