from sqlalchemy import Column, Integer, String, DateTime, func
from app.db import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(String, unique=True, index=True)
    validation_status = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
