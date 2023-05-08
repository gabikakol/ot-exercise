import uuid


class Expense:
    """Class representing an expense.

    Attributes:
        expense_id: unique id of the expense
        description: description of the expense
        trip_id: id of the trip to which the expense belongs
        amount: cost of the expense (in EUR)
        category: category of the expense
    """

    def __init__(self, expense_id, description, trip_id, amount, category):
        self.expense_id = expense_id or str(uuid.uuid4())
        self.description = description
        self.trip_id = trip_id
        self.amount = amount
        self.category = category
