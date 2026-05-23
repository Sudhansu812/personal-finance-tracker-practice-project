from dataclasses import asdict
from datetime import datetime
from enum import Enum
from pathlib import Path
import uuid
from models.enums import TransactionCategory, TransactionType
from models.transaction import Transaction
import json
import os

class TransactionRepository:
    _filepath: str = ""
    
    def __init__(self):
        self._filepath = Path(__file__).resolve().parent.parent
        self._filepath = self._filepath / "data" / "transactions.json"
    
    def load(self) -> list[Transaction]:
        if os.path.exists(self._filepath):
            with open(self._filepath, 'r') as file:
                content = file.read()
                if not content.strip():
                    return []
                data = json.loads(content)
                return [
                    Transaction(
                        id=item['id'],
                        type=TransactionType(item['type']),
                        amount=item['amount'],
                        category=TransactionCategory(item['category']),
                        date=datetime.strptime(item['date'], '%d-%m-%Y'),
                        description=item['description']
                    ) for item in data
                ]
        else:
            return []
            
    def append(self, transaction: Transaction) -> None:
        transactionList: list[Transaction] = self.load()
        transactionList.append(transaction)
        self.save_changes(transactionList)
            
    def remove(self, id: uuid.UUID) -> None:
        transactionList: list[Transaction] = self.load()
        transaction = next((t for t in transactionList if t.id == id), None)
        transactionList.remove(transaction)
        self.save_changes(transactionList)
    
    def save_changes(self, transactionList: list[Transaction]) -> None:
        with open(self._filepath, 'w') as file:
            json.dump([asdict(t) for t in transactionList], file, indent=4, default=lambda o: o.value if isinstance(o, Enum) else o.strftime('%d-%m-%Y') if isinstance(o, datetime) else str(o))