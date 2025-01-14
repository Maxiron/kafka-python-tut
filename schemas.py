from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum

class TransactionType(str, Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    TRANSFER = "transfer"

class Transaction(BaseModel):
    transaction_id: str
    user_id: str
    amount: float
    transaction_type: TransactionType
    timestamp: str
    description: Optional[str] = None
    status: str = "pending"