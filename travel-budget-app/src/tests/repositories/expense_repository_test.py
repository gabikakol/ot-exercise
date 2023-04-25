import unittest
from repositories.expense_repository import expense_repository
from entities.expense import Expense


class TestExpenseRepository(unittest.TestCase):
    def setUp(self):
        expense_repository.delete()
        self.exp1 = Expense("n213fs", "exp1", "123", "45", "cafes")
        self.exp2 = Expense("38021ndsam", "exp2", "123",
                            "532", "transportation")

    def test_create_expense(self):
        expense_repository.create_expense(self.exp1)
        expenses_list = expense_repository.find_all_expenses()
        self.assertEqual(expenses_list[-1].expense_id, self.exp1.expense_id)
        expense_repository.delete()

    def test_find_expense(self):
        expense_repository.create_expense(self.exp2)
        expense_found = expense_repository.find_expense("38021ndsam")
        self.assertEqual(expense_found.expense_id, self.exp2.expense_id)
        expense_repository.delete()

    def test_find_all_expenses(self):
        expense_repository.create_expense(self.exp1)
        expense_repository.create_expense(self.exp2)
        expenses_all = expense_repository.find_all_expenses()
        self.assertEqual(expenses_all[-2].expense_id, self.exp1.expense_id)
        self.assertEqual(expenses_all[-1].expense_id, self.exp2.expense_id)
        expense_repository.delete()
