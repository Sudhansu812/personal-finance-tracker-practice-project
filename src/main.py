import uuid
import cli
from features.tracker import TrackerService
from transaction import Transaction

def main():
    app: TrackerService = TrackerService()
    while (True):
        choice = cli.show_main_menu()
        if choice == 0:
            cli.print_transactions(app.get_all_transactions())
        elif choice == 1:
            id = uuid.uuid7()
            transactionType = cli.get_transaction_type()
            amount = cli.get_numeric_input("Transaction Amount:")
            category = cli.get_transaction_category()
            date = cli.get_date_input("transaction date")
            description = cli.get_string_input("Description:")
            trans: Transaction = Transaction(id = id, amount = amount, category = category, date = date, description = description, type = transactionType)
            app.add_transaction(trans)
        elif choice == 2:
            transaction_category: str = cli.get_transaction_category()
            filtered_transactions: list[Transaction] = app.filter_by_category(transaction_category)
            cli.print_transactions(filtered_transactions)
        elif choice == 3:
            trans: list[Transaction] = app.get_all_transactions()
            id: uuid.UUID = cli.get_delete_choice_input(trans)
            app.delete_transaction(id)
        else:
            return

        input("Press any key to continue...")

if __name__ == '__main__':
    main()