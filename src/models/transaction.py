from dataclasses import dataclass, field
from datetime import datetime
from models.enums import TransactionCategory, TransactionType
import uuid

@dataclass
class Transaction:
    id: uuid.UUID
    type: TransactionType
    amount: float
    category: TransactionCategory
    date: datetime
    description: str
    

    
    