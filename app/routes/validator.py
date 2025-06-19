from fastapi import APIRouter, HTTPException
from app.db import get_db_connection
from app.models import TransactionStatusResponse

router = APIRouter()

@router.get("/validate/{transaction_id}", response_model=TransactionStatusResponse)
def validate_transaction(transaction_id: str):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT status FROM transactions WHERE transaction_id = ?", (transaction_id,))
    row = cur.fetchone()
    conn.close()

    if row:
        return {"transaction_id": transaction_id, "status": row["status"]}
    else:
        raise HTTPException(status_code=404, detail="Transaction not found")
