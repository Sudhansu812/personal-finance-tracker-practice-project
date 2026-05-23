import uuid
import cli
from models.transaction import Transaction
from features.storage import TransactionRepository

class TrackerService:
    transaction_repo: TransactionRepository
    
    def __init__(self):
        self.transaction_repo = TransactionRepository()
    
    def add_transaction(self):
        id = uuid.uuid7()
        transactionType = cli.get_transaction_type()
        amount = cli.get_numeric_input("Transaction Amount:")
        category = cli.get_transaction_category()
        print("Transaction Date:")
        date = cli.get_date_input()
        description = cli.get_string_input("Description:")
    
        trans: Transaction = Transaction(id = id, amount = amount, category = category, date = date, description = description, type = transactionType)
        self.transaction_repo.append(transaction=trans)
    
    def delete_transaction(self):
        trans: list[Transaction] = self.transaction_repo.load()
        id: uuid.UUID = cli.get_delete_choice_input(trans)
        self.transaction_repo.remove(id)
        return
    
    def filter_by_category(self):
        transaction_category: str = cli.get_transaction_category()
        trans: list[Transaction] = self.transaction_repo.load()
        filtered_transactions: list[Transaction] = [tcat for tcat in trans if tcat.category.value == transaction_category]
        cli.print_transactions(filtered_transactions)
        return filtered_transactions
    
    def get_summary(self):
        trans: list[Transaction] = self.transaction_repo.load()
        cli.print_transactions(trans)