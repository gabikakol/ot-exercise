from entities.expense import Expense
from repositories.expense_repository import expense_repository


class ExpenseService:
    def __init__(self, expense_rep=expense_repository):
        self.expense_rep = expense_rep
        self.expense = None

    def add_expense(self, description, trip_id, amount, category):
        if description and amount and category != "select an option":
            self.expense_rep.create_expense(
                Expense(None, description, trip_id, amount, category))
            print("expense added successfully")
        else:
            print("adding expense error")


expense_service = ExpenseService()
