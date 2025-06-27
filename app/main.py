# app/main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import OperationalError
import time
from pathlib import Path

from app.db import engine, Base           # engine is built from DATABASE_URL
from app.routes import validator          # your /validate router


app = FastAPI(title="Secure Transaction Validator")

# ───────────────────────────
# CORS  (relax during dev)   
# ───────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # tighten in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ───────────────────────────
# Static  &  HTML landing    
# ───────────────────────────
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/home", response_class=HTMLResponse, include_in_schema=False)
def serve_form():
    return Path("static/form.html").read_text()


# ───────────────────────────
# Startup hook  ⇢ ensure DB  
# ───────────────────────────
@app.on_event("startup")
def startup_create_tables():
    """
    Wait for the Postgres container to accept connections,
    then create tables (idempotent).
    """
    retries = 0
    while retries < 10:
        try:
            Base.metadata.create_all(bind=engine)
            print("✅ Database connected, tables ready.")
            break
        except OperationalError as e:
            retries += 1
            print(f"⏳ DB unavailable ({e}); retry {retries}/10 …")
            time.sleep(2)
    else:
        raise RuntimeError("Database never became available — aborting.")


# ───────────────────────────
# API routes                 
# ───────────────────────────
app.include_router(validator.router)
