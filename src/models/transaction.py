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
    
    def __init__(self, type: TransactionType, amount: float, category: TransactionCategory, date: datetime, description: str, id: uuid.UUID = None):
        self.id = id
        self.type = type
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
    
    def generate_uuid7(self) -> uuid.UUID7:
        self.id = uuid.uuid7()
        return self.id
    

    
    