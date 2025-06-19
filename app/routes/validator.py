from fastapi import APIRouter, HTTPException
from app.db import get_db_connection
from app.models import TransactionValidationResult

router = APIRouter()  # ← ✅ THIS LINE IS MISSING

@router.get("/validate/{transaction_id}", response_model=TransactionValidationResult)
def validate_transaction(transaction_id: str):
    print(f"🔍 Looking for: {transaction_id}")
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT status FROM transactions WHERE transaction_id = ?", (transaction_id,))
    row = cur.fetchone()
    conn.close()

    if row:
        print("✅ Found:", row["status"])
        return TransactionValidationResult(
            transaction_id=transaction_id,
            validation_status=row["status"]
        )
    else:
        print("❌ Not Found in DB!")
        raise HTTPException(status_code=404, detail="Transaction not found")
