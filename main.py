from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import chat, faqs, projects, clients
from database import Base, engine

app = FastAPI(title="TechTicks Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://your-frontend-domain.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(chat.router, prefix="/api", tags=["Chat"])
app.include_router(faqs.router, prefix="/api/faqs", tags=["FAQs"])
app.include_router(projects.router, prefix="/api/projects", tags=["Projects"])
app.include_router(clients.router, prefix="/api/clients", tags=["Clients"])


@app.get("/health")
def health():
    return {"ok": True}
