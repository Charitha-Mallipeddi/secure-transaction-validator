from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.routes import validator  # existing router

BASE_DIR = Path(__file__).parent.parent
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(
    title="Secure Transaction Validator API",
    description="API to validate transaction IDs and return their status",
    version="1.0.0",
)

# ✅ Register the validator route
app.include_router(validator.router)

# Mount /static ➜ ./static
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Serve the Tailwind UI at /home
@app.get("/home", response_class=HTMLResponse)
async def home():
    return (STATIC_DIR / "form.html").read_text(encoding="utf-8")

# Optional root redirect
@app.get("/", include_in_schema=False)
async def root():
    return HTMLResponse('<meta http-equiv="refresh" content="0; url=/home" />', status_code=307)
