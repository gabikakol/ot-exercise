from entities.expense import Expense
from repositories.expense_repository import expense_repository
from errors.errors_handling import EmptyInputError, NotFloatError, CatNotSelectedError


class ExpenseService:
    def __init__(self, expense_rep=expense_repository):
        self.expense_rep = expense_rep
        self.expense = None

    def add_expense(self, description, trip_id, amount, category):
        if not description or not amount:
            raise EmptyInputError("Expense description and cost cannot be empty")
        
        if not self.is_float(amount):
            raise NotFloatError("Expense cost has to be a numeric value (use '.' if input is a fraction)")

        if category == "select an option":
            raise CatNotSelectedError("Category has to be selected")
        
        self.expense_rep.create_expense(
            Expense(None, description, trip_id, amount, category))
        print("expense added successfully")

    def is_float(self,num):
        try:
            float(num)
            return True
        except ValueError:
            return False

expense_service = ExpenseService()
