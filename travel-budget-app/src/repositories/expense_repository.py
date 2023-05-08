from entities.expense import Expense
from database_connection import get_database_connection


class ExpenseRepository:
    """Class responsible for database operations related to expenses"""

    def __init__(self, connection):
        """
        Class constructor.

        Args:
            connection: database connection object
        """

        self.connection = connection

    def create_expense(self, expense):
        """
        Saves a new expense to the 'expenses' database.

        Args:
            expense: Expense object to be stored in the database
        """

        cursor = self.connection.cursor()
        cursor.execute(
            "insert into expenses (expense_id, expense_description, trip_id, amount, category) values (?,?,?,?,?);",  # pylint: disable=line-too-long
            (expense.expense_id, expense.description,
             expense.trip_id, expense.amount, expense.category))
        self.connection.commit()

    def find_all_expenses(self):
        """
        Function finds and returns all expenses from the 'expenses' database.

        Returns:
            list of Expense objects
        """

        cursor = self.connection.cursor()
        rows = cursor.execute("select * from expenses").fetchall()
        return [Expense(row["expense_id"], row["expense_description"],
                        row["trip_id"], row["amount"], row["category"]) for row in rows]

    def find_expense(self, expense_id):
        """
        Searches and returns a particular expense based on its id.

        Args:
            expense_id: unique id number of the expense

        Returns:
            Particular Expense object if there exists such 
            expense in the database with the given id. 
            Otherwise None
        """

        cursor = self.connection.cursor()
        cursor.execute(
            "select * from expenses where expense_id = ?", (expense_id,))
        row = cursor.fetchone()
        if row:
            return Expense(row["expense_id"], row["expense_description"],
                           row["trip_id"], row["amount"], row["category"])
        return None


expense_repository = ExpenseRepository(get_database_connection())
