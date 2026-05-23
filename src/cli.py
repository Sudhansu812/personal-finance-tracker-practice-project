from questionary import select, text, Choice
from datetime import datetime
from models.enums import TransactionCategory, TransactionType
from models.transaction import Transaction

def show_main_menu() -> int:
    choice = select("Select the operation:"
        , choices = [
            Choice("View summary", value = 0),
            Choice("Register transaction", value = 1),
            Choice("View by category", value = 2),
            Choice("Delete transaction", value = 3),
            Choice("Exit", value=99)
        ]
    ).ask()

    return choice

def get_transaction_type() -> str:
    choices: list[Choice] = [
        Choice(title=ttype.name.title(), value=ttype) for ttype in TransactionType
    ]
    choice = select("Type of transaction: ",
                    choices=choices
                ).ask()
    return choice

def get_transaction_category() -> str:
    choices = [
        Choice(title=cat.name.title(), value=cat) for cat in TransactionCategory
    ]
    choice = select("Transaction Category: ", choices=choices).ask()
    return choice.value

def get_string_input(prompt: str) -> str:
    return text(
        prompt,
        validate=lambda text: True if len(text) > 0 else "Please enter a value"
    ).ask()

def get_numeric_input(prompt: str) -> float:
    return float(
        text(
            prompt,
            validate=_validate_floating_point_input
        ).ask()
    )

def get_date_input(prompt: str = "date") -> str:
    choice: int = int(select(f"How would you like to set the {prompt}?",
                            choices=[
                                Choice("Current date", value=0),
                                Choice("Custom date", value=1)
                            ]).ask())
    if choice == 0:
        return datetime.now().strftime("%d-%m-%Y")
    elif choice == 1:
        prompt = "Please enter the date in dd-mm-yyyy format: "
        return text(prompt, default=datetime.today().strftime("%d-%m-%Y"), validate=_validate_date_input).ask()
        
    return datetime.now().strftime("%d-%m-%Y")

def get_delete_choice_input(transactions: list[Transaction]):
    choices: list[Choice] = []
    print(f"{'Type':<15} {'Amount':<15} {'Category':<15} {'Date':<15} {'Description':<50}")
    print("-" * 100)
    for tran in transactions:
        choices.append(Choice(f"{tran.type.value:<15} {tran.amount:<15} {tran.category.value:<15} {tran.date.strftime('%d-%B-%Y'):<15} {tran.description:<50}", value=tran.id))
    choice = select("Select the transaction to delete:", choices=choices).ask()
    return choice
    
def print_transactions(transaction_list: list[Transaction]) -> None:
    print(f"{'Type':<15} {'Amount':<15} {'Category':<15} {'Date':<15} {'Description':<50}")
    print("-" * 100)
    for tran in transaction_list:
        print(f"{tran.type.value:<15} {tran.amount:<15} {tran.category.value:<15} {tran.date.strftime('%d-%B-%Y'):<15} {tran.description:<50}")

# Private helper members
def _validate_floating_point_input(text: str) -> bool | str:
    try:
        float(text)
        return True
    except ValueError:
        return "Please enter a valid number"
    
def _validate_date_input(text: str) -> bool | str:
    try:
        datetime.strptime(text, "%d-%m-%Y")
        return True
    except ValueError:
        return "Please enter a date in dd-mm-yyyy format"