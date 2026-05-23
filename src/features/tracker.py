from models.transaction import Transaction
from features.storage import TransactionRepository

class TrackerService:
    transaction_repo: TransactionRepository
    
    def __init__(self):
        self.transaction_repo = TransactionRepository()
    
    def get_all_transactions(self) -> list[Transaction]:
        self.transaction_repo.load()
    
    def add_transaction(self, trans: Transaction):
        self.transaction_repo.append(transaction=trans)
    
    def delete_transaction(self, id) -> str:
        try:
            self.transaction_repo.remove(id)
            return f"{id} - Removed."
        except ValueError:
            return "Transaction not found"
    
    def filter_by_category(self, transaction_category: str) -> list[Transaction]:
        trans: list[Transaction] = self.transaction_repo.load()
        filtered_transactions: list[Transaction] = [tcat for tcat in trans if tcat.category.value == transaction_category]
        return filtered_transactions