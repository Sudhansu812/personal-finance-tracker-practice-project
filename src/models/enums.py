from enum import Enum

class TransactionCategory(Enum):
    # Income
    SALARY = "Salary"
    FREELANCE = "Freelance"
    INVESTMENT = "Investment"
    # Living
    RENT = "Rent"
    GROCERIES = "Groceries"
    UTILITIES = "Utilities"
    HEALTHCARE = "Healthcare"
    # Transport
    FUEL = "Fuel"
    PUBLIC_TRANSPORT = "Public transport"
    PARKING = "Parking"
    # Lifestyle
    DINING_OUT = "Dining out"
    ENTERTAINMENT = "Entertainment"
    SHOPPING = "Shopping"
    TRAVEL = "Travel"
    SUBSCRIPTIONS = "Subscriptions"
    # Other
    EDUCATION = "Education"
    GIFTS = "Gifts"
    SAVINGS = "Savings"
    OTHER = "Other"
    
class TransactionType(Enum):
    DEBIT = "Debit"
    CREDIT = "Credit"