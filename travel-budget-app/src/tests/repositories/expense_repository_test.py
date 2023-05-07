import unittest
from entities.expense import Expense
from tests.testing_env.test_repository import test_expense_repository
from tests.testing_env.test_init_database import init_expenses_database

class TestExpenseRepository(unittest.TestCase):
    def setUp(self):
        init_expenses_database()
        self.expense1 = Expense("a1b2c3", "expense1", "123", "34.32", "other")
        self.expense2 = Expense("421nme", "expense2", "748", "7.00", "groceries")


    def test_create_expense(self):
        test_expense_repository.create_expense(self.expense1)
        all_expenses = test_expense_repository.find_all_expenses()

        self.assertEqual(len(all_expenses), 1)
        self.assertEqual(all_expenses[0].expense_id, "a1b2c3")
        self.assertEqual(all_expenses[0].description, "expense1")
        self.assertEqual(all_expenses[0].trip_id, "123")
        self.assertEqual(all_expenses[0].amount, "34.32")
        self.assertEqual(all_expenses[0].category, "other")

    def test_find_expense(self):
        expense = test_expense_repository.find_expense("a1b2c3")
        self.assertEqual(expense, None)

        test_expense_repository.create_expense(self.expense1)
        expense = test_expense_repository.find_expense("a1b2c3")

        self.assertEqual(expense.expense_id, "a1b2c3")

    def test_find_all_expenses(self):
        test_expense_repository.create_expense(self.expense1)
        test_expense_repository.create_expense(self.expense2)
        all_expenses = test_expense_repository.find_all_expenses()

        self.assertEqual(len(all_expenses), 2)
        self.assertEqual(all_expenses[0].expense_id, "a1b2c3")
        self.assertEqual(all_expenses[1].expense_id, "421nme")