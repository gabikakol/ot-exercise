from tkinter import ttk
from services.trip_service import trip_service
from repositories.expense_repository import expense_repository


class TripView:
    """Class for trip's data ui"""

    def __init__(self, root, trips_list, add_expense, trip_stats):
        """class constructor"""

        self._root = root
        self.trips_list_handle = trips_list
        self._window = None
        self.add_expense = add_expense
        self.trip_name = trip_service.get_trip_name()
        self.trip_id = trip_service.get_trip_id()
        self.trip_stats_handle = trip_stats

        self.start()

    def start(self):

        self._window = ttk.Frame(master=self._root)
        header_label = ttk.Label(
            master=self._window, text=f"Expenses of the {self.trip_name} trip",font=('consolas', 13, "bold"))
        header_label.grid(padx=5, pady=5)

        expenses = expense_repository.find_all_expenses()
        empty = True
        for exp in expenses:
            if exp.trip_id == self.trip_id:
                self.init_expense(exp)
                empty = False
        if empty:
            none_label = ttk.Label(master=self._window, text="No expenses yet", font=('consolas', 10, "italic"))
            none_label.grid(padx=5, pady=5)

        add_button = ttk.Button(master=self._window,
                                text="Add expense", command=self.add_expense)
        add_button.grid(padx=5, pady=5)

        stats_button = ttk.Button(
            master=self._window, text="Trip statistics", command=self.trip_stats_handle)
        stats_button.grid(padx=5, pady=5)

        back_button = ttk.Button(
            master=self._window, text="Back to trips menu", command=self.trips_list_handle)
        back_button.grid(padx=5, pady=5)

    def pack(self):
        """displays the current view"""
        self._window.pack()

    def destroy(self):
        """resets the current view"""
        self._window.destroy()

    def init_expense(self, exp):
        exp_label = ttk.Label(
            master=self._window, text=f"{exp.description}: €{float(exp.amount):.2f}, cat: {exp.category}", font=('consolas', 10))
        exp_label.grid(padx=5, pady=5, column=0)
