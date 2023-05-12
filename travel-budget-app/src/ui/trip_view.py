from tkinter import ttk, constants
from services.trip_service import trip_service
from repositories.expense_repository import expense_repository


class TripView:
    """Class for trip's data ui."""

    def __init__(self, root, trips_list, add_expense, trip_stats):
        """
        Class constructor.

        Args:
            root: tkinter root
            trips_list: trips list view window
            add_expense: add expense window
            trip_stats: trip statistics window
        """

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
        style = ttk.Style()

        header_label = ttk.Label(
            master=self._window, text=f"Expenses of the {self.trip_name} trip", font=('consolas', 15, "bold"))
        header_label.grid(padx=5, pady=5, column=1)

        expenses = expense_repository.find_all_expenses()
        empty = True
        for exp in expenses:
            if exp.trip_id == self.trip_id:
                self.init_expense(exp)
                empty = False
        if empty:
            none_label = ttk.Label(
                master=self._window, text="No expenses yet", foreground = "red", font=('consolas', 10, "italic"))
            none_label.grid(padx=5, pady=5, column=1)

        add_button = ttk.Button(master=self._window,
                                text="Add expense", command=self.add_expense, style="add.TButton")
        add_button.grid(padx=5, pady=5, column=1, sticky=constants.EW)
        style.configure('add.TButton', font=('consolas', 10))

        stats_button = ttk.Button(
            master=self._window, text="Trip statistics", command=self.trip_stats_handle, style="stats.TButton")
        stats_button.grid(padx=5, pady=5, column=1, sticky=constants.EW)
        style.configure('stats.TButton', font=('consolas', 10))

        back_button = ttk.Button(
            master=self._window, text="Back to trips menu", command=self.trips_list_handle, style='back.TButton')
        back_button.grid(padx=5, pady=5, column=1, sticky=constants.EW)
        style.configure('back.TButton', font=('consolas', 10))

        self._window.grid_columnconfigure(0,minsize=0)
        self._window.grid_columnconfigure(1,minsize=700)

    def pack(self):
        """Displays the current view."""
        self._window.pack(fill=constants.X)

    def destroy(self):
        """Resets the current view."""
        self._window.destroy()

    def init_expense(self, exp):
        exp_label = ttk.Label(
            master=self._window, text=f"{exp.description}: €{float(exp.amount):.2f}, cat: {exp.category}", font=('consolas', 10))
        exp_label.grid(padx=5, pady=5, column=1)
