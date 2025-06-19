from pydantic import BaseModel

class TransactionValidationResult(BaseModel):
    transaction_id: str
    validation_status: str
