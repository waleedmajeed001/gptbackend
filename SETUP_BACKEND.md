# TechTicks Backend Setup (FastAPI)

This file contains copy-paste commands to run the backend on a new machine.

## 1) Clone and enter project
```bash
# Replace with your repo URL
git clone <your-repo-url>
cd gpt/backend
```

## 2) Create and activate virtual environment
### Windows (CMD/PowerShell)
```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux (bash/zsh)
```bash
python3 -m venv venv
source venv/bin/activate
```

## 3) Install dependencies
```bash
pip install -r requirements.txt
```

## 4) Configure environment variables
Create a `.env` file in `backend/` with the following content (choose ONE database option):

```env
# Option A: Local SQLite (recommended for development)
DATABASE_URL=sqlite:///./techticks.db

# Option B: Neon PostgreSQL (production/remote)
# DATABASE_URL=postgresql://<user>:<password>@<host>/<db>?sslmode=require

# Required for AI responses
GEMINI_API_KEY=YOUR_GEMINI_KEY
```

## 5) Initialize database schema
```bash
# Create all tables (idempotent)
python -c "from database import Base,engine; Base.metadata.create_all(bind=engine)"
```

## 6) Seed TechTicks data (projects, clients, FAQs, company info)
```bash
python seed_techticks_data.py
```

## 7) Run the API server
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

API will be available at:
- Swagger UI: http://localhost:8000/docs
- Health check: http://localhost:8000/health

---

## Notes
- To switch from SQLite to Neon later, update `backend/.env` `DATABASE_URL`, then rerun the schema init step (Step 5). Seed (Step 6) is safe to run once; it will skip duplicates.
- Keep your `GEMINI_API_KEY` private.
- If you wiped the local SQLite file, just re-run Steps 5–7.
