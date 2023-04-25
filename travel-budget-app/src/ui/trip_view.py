from tkinter import ttk
from services.trip_service import trip_service
from repositories.expense_repository import expense_repository


class TripView:
    def __init__(self, root, trips_list, add_expense, trip_stats):
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
            master=self._window, text=f"Expenses of the {self.trip_name} trip:")
        header_label.grid(padx=5, pady=5)

        expenses = expense_repository.find_all_expenses()
        for exp in expenses:
            self.init_expense(exp)

        add_button = ttk.Button(master=self._window,
                                text="Add expense", command=self.add_expense)
        add_button.grid(padx=5, pady=5)

        stats_button = ttk.Button(
            master=self._window, text="Trip statistics", command=self.trip_stats_handle)
        stats_button.grid(padx=5, pady=5)

        back_button = ttk.Button(
            master=self._window, text="Back to trips menu", command=self.trips_list_handle)
        back_button.grid(padx=5, pady=5)

        # add expense
        # statistics

    def pack(self):
        self._window.pack()

    def destroy(self):
        self._window.destroy()

    def init_expense(self, exp):
        if exp.trip_id == self.trip_id:
            exp_label = ttk.Label(
                master=self._window, text=f"{exp.description}: €{exp.amount}, category: {exp.category}")
            exp_label.grid(padx=5, pady=5, column=0)
