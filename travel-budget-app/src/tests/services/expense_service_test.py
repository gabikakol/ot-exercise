import unittest
from entities.expense import Expense
from services.expense_service import ExpenseService
from tests.testing_env.test_repository import test_expense_repository
from errors.errors_handling import EmptyInputError, NotFloatError, CatNotSelectedError

class TestExpenseService(unittest.TestCase):
    def setUp(self):
        self.expense_service = ExpenseService(test_expense_repository)
        self.expense1 = Expense("mm22nn", "lunch", "a1b2c3", "12.35", "restaurants")

    def test_add_expense(self):
        self.expense_service.add_expense("shopping", "a1b2c3", "34.23", "groceries")

        self.assertRaises(EmptyInputError, lambda: self.expense_service.add_expense("", "", "10.21", ""))
        self.assertRaises(NotFloatError, lambda: self.expense_service.add_expense("shopping", "a1b2c3", "abc", "groceries"))
        self.assertRaises(CatNotSelectedError, lambda: self.expense_service.add_expense("shopping", "a1b2c3", "10.21", "select an option"))