from pydantic import BaseModel

class TransactionStatusResponse(BaseModel):
    transaction_id: str
    status: str
