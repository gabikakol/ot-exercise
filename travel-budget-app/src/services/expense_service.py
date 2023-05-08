from entities.expense import Expense
from repositories.expense_repository import expense_repository
from errors.errors_handling import EmptyInputError, NotFloatError, CatNotSelectedError


class ExpenseService:
    """Class responsible for the application logic related to expenses."""

    def __init__(self, expense_rep=expense_repository):
        """
        Class constructor.

        Args:
            expense_rep: ExpenseRepository object (default value is expense_repository)
        """

        self.expense_rep = expense_rep
        self.expense = None

    def add_expense(self, description, trip_id, amount, category):
        """
        Creates a new expense to the database if the inputs are valid.

        Args:
            description: description of the expense
            trip_id: id of the trip the expense belongs to
            amount: cost of the expense
            category: category of the expense

        Raises:
            EmptyInputError: if the expense description or cost inputs are empty
            NotFloatError: if the cost input is not a numeric value
            CatNotSelectedError: if the category input is not selected
        """

        if not description or not amount:
            raise EmptyInputError(
                "Expense description and cost cannot be empty")

        if not self.is_float(amount):
            raise NotFloatError(
                "Expense cost has to be a numeric value (use '.' if input is a fraction)")

        if category == "select an option":
            raise CatNotSelectedError("Category has to be selected")

        self.expense_rep.create_expense(
            Expense(None, description, trip_id, amount, category))

    def is_float(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False


# This variable will be used by the application and services
# to avoid making multiple instances of ExpenseService
expense_service = ExpenseService()
