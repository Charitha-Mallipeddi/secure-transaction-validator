from fastapi import FastAPI
from app.routes import validator

app = FastAPI(
    title="Secure Transaction Validator API",
    description="API to validate transaction IDs and return their status",
    version="1.0.0"
)

app.include_router(validator.router)
