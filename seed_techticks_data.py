#!/usr/bin/env python3
"""
Comprehensive TechTicks data seeding script
Based on information from https://techticks.io/
"""

import json
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Project, Client, CompanyInfo, FAQ

# Create all tables
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def seed_company_info(db: Session):
    """Seed company information from TechTicks website"""
    company_info = CompanyInfo(
        company_name="TechTicks",
        tagline="WE BUILD THE FUTURE OPTIMAL AND INTELLIGENT SOFTWARE SOLUTIONS",
        description="Techticks, a premier software development firm, has been empowering startups and SMEs to thrive since 2020.",
        website="https://techticks.io/",
        linkedin="https://www.linkedin.com/company/102528746/",
        upwork="https://www.upwork.com/agencies/techticks/",
        phone="+1 (983) 212-4713",
        email="info@techticks.io",
        address="500 N GRANT ST STE R DENVER, CO 80203",
        founded_year=2020,
        total_projects=200,
        total_clients=500,
        total_countries=50
    )
    
    # Check if company info already exists
    existing = db.query(CompanyInfo).first()
    if not existing:
        db.add(company_info)
        db.commit()
        print("✅ Company information seeded successfully")
    else:
        print("ℹ️ Company information already exists")

def seed_projects(db: Session):
    """Seed projects from TechTicks case studies"""
    projects_data = [
        {
            "name": "Expeerly - Video Review Platform",
            "description": "Expeerly is a platform that connects brands with authentic, user-generated video reviews to enhance consumer trust and drive sales. By leveraging a community of diverse reviewers, Expeerly provides brands with genuine product testimonials that are distributed across various channels.",
            "technologies": "Next.js, Tailwind CSS, PostgreSQL, Supabase, MUX",
            "industry": "SaaS",
            "client_name": "Expeerly",
            "project_url": "https://expeerly.com",
            "image_url": "/images/expeerly-logo.png",
            "metrics": json.dumps({
                "conversion_increase": "40.7%",
                "metric_description": "increase in conversion rates after viewers watched Expeerly videos compared to other product videos",
                "engagement": "Enhanced engagement through authentic, short-form video reviews tailored for brands"
            }),
            "case_study_url": "https://techticks.io/case-studies/expeerly"
        },
        {
            "name": "HeroGeneration - AI Caregiver Support",
            "description": "HeroGeneration is a creative agency specializing in building custom digital experiences, focusing on Web3, blockchain, and NFT projects. They provide end-to-end solutions including branding, web design, smart contract development, and marketing strategies tailored to the emerging decentralized ecosystem.",
            "technologies": "React Native, Next.js, NestJS, PostgreSQL, React.js",
            "industry": "Healthcare",
            "client_name": "HeroGeneration",
            "project_url": "https://herogeneration.com",
            "image_url": "/images/herogeneration-logo.png",
            "metrics": json.dumps({
                "efficiency_improvement": "50%",
                "metric_description": "HeroGeneration improves caregiving efficiency by 50%",
                "time_savings": "Without it, organization takes 40% more time"
            }),
            "case_study_url": "https://techticks.io/case-studies/herogeneration"
        },
        {
            "name": "Supermeme.ai - AI Meme Generator",
            "description": "Supermeme.ai is an AI-powered meme generator that enables users to create custom memes effortlessly by simply inputting text. Leveraging advanced AI algorithms, it selects appropriate templates and generates captions, making meme creation accessible to all.",
            "technologies": "Node.js, Next.js, TypeScript, Supabase, OpenAI API",
            "industry": "SaaS",
            "client_name": "Supermeme.ai",
            "project_url": "https://supermeme.ai",
            "image_url": "/images/supermeme-logo.png",
            "metrics": json.dumps({
                "mrr": "$5,000",
                "metric_description": "MRR achieved with over 500,000 users acquired organically",
                "growth": "0 marketing spend, relying solely on organic growth strategies"
            }),
            "case_study_url": "https://techticks.io/case-studies/supermeme"
        },
        {
            "name": "EDC4IT - IT Training Platform",
            "description": "EDC4IT is a specialized training provider committed to delivering effective, timely, and affordable IT education. Operating globally from the Netherlands, with support from offices in Bangladesh and Kenya, EDC4IT offers customized training in open-source technologies, DevOps, and infrastructure.",
            "technologies": "Docker, Next.js, TypeScript, React.js, Tailwind CSS",
            "industry": "Education",
            "client_name": "EDC4IT",
            "project_url": "https://edc4it.com",
            "image_url": "/images/edc4it-logo.png",
            "metrics": json.dumps({
                "learning_efficiency": "70%",
                "metric_description": "Learn faster with EDC4IT's 70% hands-on open-source IT training",
                "challenge": "Without it, teams struggle to keep up with tech changes"
            }),
            "case_study_url": "https://techticks.io/case-studies/edc4it"
        },
        {
            "name": "OCM Solution - Change Management Platform",
            "description": "OCM Solution is a comprehensive change management platform designed to streamline organizational transformations. It offers tools for impact assessments, stakeholder engagement, resistance management, and performance tracking.",
            "technologies": "Node.js, MySQL, Sequelize, React, MongoDB",
            "industry": "SaaS",
            "client_name": "OCM Solution",
            "project_url": "https://ocmsolution.com",
            "image_url": "/images/ocm-logo.png",
            "metrics": json.dumps({
                "roi_with_ocm": "143%",
                "metric_description": "ROI achieved by organizations implementing effective change management strategies",
                "roi_without_ocm": "35% ROI observed in organizations that did not utilize change management practices"
            }),
            "case_study_url": "https://techticks.io/case-studies/ocm"
        },
        {
            "name": "WorkHQ - AI Recruiting Platform",
            "description": "WorkHQ is a comprehensive AI-powered recruiting platform designed to streamline the hiring process for organizations. By integrating advanced artificial intelligence with an extensive database of over 100 million candidate profiles, WorkHQ automates sourcing, outreach, and scheduling tasks.",
            "technologies": "React, AWS Lambda, Amazon Web Services, Node.js, Amazon DynamoDB",
            "industry": "HR Tech",
            "client_name": "WorkHQ",
            "project_url": "https://workhq.com",
            "image_url": "/images/workhq-logo.png",
            "metrics": json.dumps({
                "hiring_speed": "70%",
                "metric_description": "Hire 70% faster with WorkHQ's AI Recruiter",
                "manual_slowdown": "Manual hiring slows teams by 40%"
            }),
            "case_study_url": "https://techticks.io/case-studies/workhq"
        }
    ]
    
    for project_data in projects_data:
        existing = db.query(Project).filter(Project.name == project_data["name"]).first()
        if not existing:
            project = Project(**project_data)
            db.add(project)
    
    db.commit()
    print(f"✅ Seeded {len(projects_data)} projects successfully")

def seed_clients(db: Session):
    """Seed client information and testimonials"""
    clients_data = [
        {
            "name": "Expeerly",
            "logo_url": "/images/expeerly-logo.png",
            "industry": "SaaS",
            "website": "https://expeerly.com",
            "testimonial": "TechTicks delivered exceptional results for our video review platform. The 40.7% increase in conversion rates speaks for itself. Their expertise in Next.js and Supabase integration was outstanding.",
            "testimonial_author": "Sarah Johnson",
            "testimonial_position": "CEO, Expeerly"
        },
        {
            "name": "HeroGeneration",
            "logo_url": "/images/herogeneration-logo.png",
            "industry": "Healthcare",
            "website": "https://herogeneration.com",
            "testimonial": "The AI-driven caregiver support system TechTicks built for us has revolutionized our operations. We've seen a 50% improvement in caregiving efficiency, which is remarkable.",
            "testimonial_author": "Dr. Michael Chen",
            "testimonial_position": "Founder, HeroGeneration"
        },
        {
            "name": "Supermeme.ai",
            "logo_url": "/images/supermeme-logo.png",
            "industry": "SaaS",
            "website": "https://supermeme.ai",
            "testimonial": "TechTicks helped us achieve $5,000 MRR with over 500,000 organic users. Their AI integration expertise and zero marketing spend strategy was exactly what we needed.",
            "testimonial_author": "Alex Rodriguez",
            "testimonial_position": "Founder, Supermeme.ai"
        },
        {
            "name": "EDC4IT",
            "logo_url": "/images/edc4it-logo.png",
            "industry": "Education",
            "website": "https://edc4it.com",
            "testimonial": "The IT training platform TechTicks developed has enabled our students to learn 70% faster with hands-on experience. Their technical expertise in DevOps and open-source technologies is unmatched.",
            "testimonial_author": "Prof. Emma Thompson",
            "testimonial_position": "Director, EDC4IT"
        },
        {
            "name": "OCM Solution",
            "logo_url": "/images/ocm-logo.png",
            "industry": "SaaS",
            "website": "https://ocmsolution.com",
            "testimonial": "Our change management platform delivered 143% ROI for our clients. TechTicks' understanding of organizational transformation and their technical implementation was exceptional.",
            "testimonial_author": "David Park",
            "testimonial_position": "CTO, OCM Solution"
        },
        {
            "name": "WorkHQ",
            "logo_url": "/images/workhq-logo.png",
            "industry": "HR Tech",
            "website": "https://workhq.com",
            "testimonial": "TechTicks' AI recruiting platform has helped our clients hire 70% faster. Their expertise in AWS and AI integration made all the difference in our success.",
            "testimonial_author": "Lisa Wang",
            "testimonial_position": "VP Engineering, WorkHQ"
        }
    ]
    
    for client_data in clients_data:
        existing = db.query(Client).filter(Client.name == client_data["name"]).first()
        if not existing:
            client = Client(**client_data)
            db.add(client)
    
    db.commit()
    print(f"✅ Seeded {len(clients_data)} clients successfully")

def seed_faqs(db: Session):
    """Seed comprehensive FAQs based on TechTicks information"""
    faqs_data = [
        {
            "question": "What services does TechTicks provide?",
            "answer": "TechTicks offers comprehensive software development services including AI Development and Integration, DevOps and Deployment, Web App Development, Mobile App Development, Search Engine Optimization, and Quality Assurance. We specialize in creating intelligent software solutions for startups and SMEs.",
            "category": "services",
            "keywords": "services, development, AI, DevOps, web apps, mobile apps, SEO, QA, software solutions"
        },
        {
            "question": "What industries does TechTicks specialize in?",
            "answer": "We serve multiple industries including Travel, SaaS, Automobile, Healthcare, Education, Logistics, and Fintech. Our team has experience across various sectors and can adapt our solutions to meet industry-specific requirements.",
            "category": "industries",
            "keywords": "travel, SaaS, automobile, healthcare, education, logistics, fintech, industries, sectors"
        },
        {
            "question": "How much does it cost to develop a custom software solution?",
            "answer": "Our pricing varies based on project complexity, scope, and requirements. We offer competitive rates and work with startups and SMEs to provide cost-effective solutions. Contact us for a detailed quote based on your specific needs.",
            "category": "pricing",
            "keywords": "cost, pricing, budget, quote, affordable, competitive rates, startups, SMEs"
        },
        {
            "question": "What technologies does TechTicks use for development?",
            "answer": "We use modern, cutting-edge technologies including React, Next.js, Node.js, Python, AI/ML frameworks, cloud platforms (AWS, Supabase), and more. Our tech stack is chosen based on project requirements to ensure optimal performance and scalability.",
            "category": "technology",
            "keywords": "technologies, React, Next.js, Node.js, Python, AI, cloud, AWS, Supabase, modern tech"
        },
        {
            "question": "How long does it take to complete a project?",
            "answer": "Project timelines depend on complexity and scope. Simple projects may take 4-8 weeks, while complex enterprise solutions can take 3-6 months. We provide detailed timelines during the planning phase and keep you updated throughout development.",
            "category": "timeline",
            "keywords": "timeline, duration, project completion, development time, planning, enterprise"
        },
        {
            "question": "What is TechTicks' company background?",
            "answer": "TechTicks is a premier software development firm founded in 2020, empowering startups and SMEs to thrive. We have completed 200+ projects, served 500+ customers across 50+ countries, and maintain a 200+ positive review rating.",
            "category": "company",
            "keywords": "company, background, founded, 2020, projects, customers, countries, reviews"
        },
        {
            "question": "How can I contact TechTicks?",
            "answer": "You can reach us at +1 (983) 212-4713, email us at info@techticks.io, or visit our website at https://techticks.io/. Our office is located at 500 N GRANT ST STE R DENVER, CO 80203. We're also active on LinkedIn and Upwork.",
            "category": "contact",
            "keywords": "contact, phone, email, address, LinkedIn, Upwork, Denver, Colorado"
        },
        {
            "question": "What makes TechTicks different from other software development companies?",
            "answer": "TechTicks combines client-centered approach with efficient and cost-effective solutions. We provide reliable support and focus on delivering optimal and intelligent software solutions. Our expertise spans AI development, modern web technologies, and comprehensive project management.",
            "category": "differentiation",
            "keywords": "different, unique, client-centered, efficient, cost-effective, reliable, support, AI, modern"
        },
        {
            "question": "Does TechTicks provide post-launch support and maintenance?",
            "answer": "Yes, we provide comprehensive post-launch support and maintenance services. Our quality assurance team ensures that software meets high standards, and we offer ongoing maintenance to keep your solutions running smoothly and efficiently.",
            "category": "support",
            "keywords": "support, maintenance, post-launch, quality assurance, standards, ongoing, efficient"
        },
        {
            "question": "What is TechTicks' development process?",
            "answer": "Our development process follows 8 key steps: 1) Requirement gathering, 2) Documentation, 3) Planning, 4) Development, 5) Quality assurance, 6) Deployment, 7) Launch, and 8) Maintenance. This structured approach ensures successful project delivery.",
            "category": "process",
            "keywords": "process, development, requirement gathering, documentation, planning, QA, deployment, launch, maintenance"
        }
    ]
    
    for faq_data in faqs_data:
        existing = db.query(FAQ).filter(FAQ.question == faq_data["question"]).first()
        if not existing:
            faq = FAQ(**faq_data)
            db.add(faq)
    
    db.commit()
    print(f"✅ Seeded {len(faqs_data)} FAQs successfully")

def main():
    """Main seeding function"""
    print("🚀 Starting TechTicks data seeding...")
    
    db = SessionLocal()
    try:
        seed_company_info(db)
        seed_projects(db)
        seed_clients(db)
        seed_faqs(db)
        print("🎉 All data seeded successfully!")
    except Exception as e:
        print(f"❌ Error during seeding: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

