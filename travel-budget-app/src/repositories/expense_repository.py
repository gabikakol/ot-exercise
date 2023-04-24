from entities.expense import Expense
from database_connection import get_database_connection

class ExpenseRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_expense(self, expense):
        cursor = self.connection.cursor()
        cursor.execute("insert into expenses (expense_id, expense_description, trip_id, amount, category) values (?,?,?,?,?);", (expense.expense_id, expense.description, expense.trip_id, expense.amount, expense.category))
        self.connection.commit()

expense_repository = ExpenseRepository(get_database_connection())