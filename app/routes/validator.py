from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Transaction

router = APIRouter()

@router.get("/validate/{tx_id}")
def validate_transaction(tx_id: str, db: Session = Depends(get_db)):
    tx = db.query(Transaction).filter(Transaction.transaction_id == tx_id).first()
    if tx:
        return {"transaction_id": tx.transaction_id, "validation_status": tx.validation_status}
    else:
        return {"transaction_id": tx_id, "validation_status": "Unknown"}
