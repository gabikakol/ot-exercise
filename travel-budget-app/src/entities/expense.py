import uuid


class Expense:
    def __init__(self, expense_id, description, trip_id, amount, category):
        self.expense_id = expense_id or str(uuid.uuid4())
        self.description = description
        self.trip_id = trip_id
        self.amount = amount
        self.category = category
