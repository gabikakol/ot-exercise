from tkinter import ttk, constants
from services.trip_service import trip_service
from repositories.expense_repository import expense_repository
from repositories.trip_repository import trip_repository


class TripStats:
    """Class for trip's statistics ui."""

    def __init__(self, root, trip_view):
        """
        Class contructor.

        Args:
            root: tkinter root
            trip_view: trip's details (expenses) view window
        """

        self._root = root
        self.trip_view_handle = trip_view
        self._window = None
        self.trip_name = trip_service.get_trip_name()
        self.trip_id = trip_service.get_trip_id()
        self.expenses = self.find_trip_expenses()
        self.current_trip = trip_repository.find_trip(self.trip_id)
        self.start()

    def start(self):
        self._window = ttk.Frame(master=self._root)
        style = ttk.Style()

        stats_label = ttk.Label(
            master=self._window, text=f"Statistics of the {self.trip_name} trip", font=('consolas', 15, "bold"))
        stats_label.grid(padx=5, pady=5, column=0)

        if len(self.expenses) > 0:
            self.display_stats()
        else:
            no_data_label = ttk.Label(master=self._window,
                                      text=f"No data available. Add an expense to see statistics.", foreground="red", font=('consolas', 10, "italic"))
            no_data_label.grid(padx=5, pady=5, column=0)

        back_button = ttk.Button(
            master=self._window, text="Back", command=self.trip_view_handle, style='back.TButton')
        back_button.grid(padx=5, pady=5, column=0, sticky=constants.EW)
        style.configure('back.TButton', font=('consolas', 10))

        self._window.grid_columnconfigure(0,minsize=700)

    def pack(self):
        """Displays the current view."""
        self._window.pack(fill=constants.X)

    def destroy(self):
        """Resets the current view."""
        self._window.destroy()

    def spent_total(self):
        sum = 0
        for exp in self.expenses:
            sum += float(exp.amount)
        return sum

    def stats_sorting(self):
        dic = {}

        for exp in self.expenses:
            if exp.category in dic:
                dic[exp.category] += float(exp.amount)
            else:
                dic[exp.category] = float(exp.amount)

        cheapest_cat = min(dic.items(), key=lambda item: item[1])
        expensive_cat = max(dic.items(), key=lambda item: item[1])

        cheapest_exp = min(self.expenses, key=lambda exp: exp.amount)
        expensive_exp = max(self.expenses, key=lambda exp: exp.amount)

        return [cheapest_cat, expensive_cat, (cheapest_exp.description, float(cheapest_exp.amount)), (expensive_exp.description, float(expensive_exp.amount))]

    def find_trip_expenses(self):
        all_expenses = expense_repository.find_all_expenses()
        trip_expenses = []
        for exp in all_expenses:
            if exp.trip_id == self.trip_id:
                trip_expenses.append(exp)

        return trip_expenses

    def display_stats(self):
        sum = self.spent_total()

        spent_total_label = ttk.Label(
            master=self._window, text=f"Spent in total: €{sum:.2f}", font=('consolas', 10))
        spent_total_label.grid(padx=5, pady=5, column=0)

        duration_label = ttk.Label(
            master=self._window, text=f"Duration of the trip: {self.current_trip.duration} days", font=('consolas', 10))
        duration_label.grid(padx=5, pady=5, column=0)

        average = sum/int(self.current_trip.duration)
        average_day_label = ttk.Label(
            master=self._window, text=f"Spent per day on average: €{average:.2f}", font=('consolas', 10))
        average_day_label.grid(padx=5, pady=5, column=0)

        stats = self.stats_sorting()
        """
        Stats is a list with following:
        - the cheapest category at index 0
        - the most expensive category at index 1
        - the cheapest expense at index 2
        - the most expensive expense at index 3
        At each index: a tuple with category name at index 0 and cost (as a float number) at index 1.
        """

        cheapest_category_label = ttk.Label(
            master=self._window, text=f"The cheapest category: {stats[0][0]} (€{(stats[0][1]):.2f})", font=('consolas', 10))
        cheapest_category_label.grid(padx=5, pady=5, column=0)

        expensive_category_label = ttk.Label(
            master=self._window, text=f"The most expensive category: {stats[1][0]} (€{(stats[1][1]):.2f})", font=('consolas', 10))
        expensive_category_label.grid(padx=5, pady=5, column=0)

        cheapest_label = ttk.Label(
            master=self._window, text=f"The cheapest item: {stats[2][0]} (€{(stats[2][1]):.2f})", font=('consolas', 10))
        cheapest_label.grid(padx=5, pady=5, column=0)

        expensive_label = ttk.Label(
            master=self._window, text=f"The most expensive item: {stats[3][0]} (€{(stats[3][1]):.2f})", font=('consolas', 10))
        expensive_label.grid(padx=5, pady=5, column=0)
