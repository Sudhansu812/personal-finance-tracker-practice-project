import uuid
from cli import get_transaction_input, get_delete_choice_input, get_transaction_category, print_transactions
from models.transaction import Transaction
from features.storage import TransactionRepository

class TrackerService:
    transactions: list[Transaction]
    
    def add_transaction():
        trans: Transaction = get_transaction_input()
        repo: TransactionRepository = TransactionRepository()
        repo.append(transaction=trans)
    
    def delete_transaction():
        repo = TransactionRepository()
        trans: list[Transaction] = repo.load()
        id: uuid.UUID = get_delete_choice_input(trans)
        repo.remove(id)
        return
    
    def filter_by_category():
        transaction_category: str = get_transaction_category()
        repo = TransactionRepository()
        trans: list[Transaction] = repo.load()
        filtered_transactions: list[Transaction] = [tcat for tcat in trans if tcat.category.value == transaction_category]
        print_transactions(filtered_transactions)
        return filtered_transactions
    
    def get_summary():
        repo = TransactionRepository()
        trans: list[Transaction] = repo.load()
        print_transactions(trans)