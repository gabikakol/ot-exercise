from entities.expense import Expense
from database_connection import get_database_connection


class ExpenseRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_expense(self, expense):
        cursor = self.connection.cursor()
        cursor.execute("insert into expenses (expense_id, expense_description, trip_id, amount, category) values (?,?,?,?,?);",
                       (expense.expense_id, expense.description, expense.trip_id, expense.amount, expense.category))
        self.connection.commit()

    def find_all_expenses(self):
        cursor = self.connection.cursor()
        rows = cursor.execute("select * from expenses").fetchall()
        return [Expense(row["expense_id"], row["expense_description"], row["trip_id"], row["amount"], row["category"]) for row in rows]

    def find_expense(self, expense_id):
        cursor = self.connection.cursor()
        cursor.execute(
            "select * from expenses where expense_id = ?", (expense_id,))
        row = cursor.fetchone()
        if row:
            return Expense(row["expense_id"], row["expense_description"], row["trip_id"], row["amount"], row["category"])
        return None

    def delete(self):
        cursor = self.connection.cursor()
        cursor.execute("delete from expenses")
        self.connection.commit()


expense_repository = ExpenseRepository(get_database_connection())
