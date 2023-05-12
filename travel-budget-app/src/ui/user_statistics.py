from tkinter import ttk, constants
from services.user_service import user_service
from repositories.trip_repository import trip_repository
from repositories.expense_repository import expense_repository
import datetime


class UserStats:
    """Class for user's statistics ui."""

    def __init__(self, root, user_menu):
        """
        Class constructor.

        Args:
            root: tkinter root
            user_menu: user menu window
        """

        self._root = root
        self._window = None
        self.username = user_service.get_username()
        self.user_menu_handle = user_menu
        self.trips = trip_repository.find_all_trips()
        self.expenses = expense_repository.find_all_expenses()
        self.current_time = datetime.datetime.now()

        self.start()

    def start(self):
        self._window = ttk.Frame(master=self._root)
        style = ttk.Style()

        current_date_label = ttk.Label(master=self._window, text=self.current_time.strftime(
            '%H:%M, %A, %dth %B %Y'), foreground="#5A5A5A", font=('consolas', 10))
        current_date_label.grid(padx=5, pady=5, column=0)

        stats_label = ttk.Label(master=self._window,
                                text=f"Statistics for {self.username}", font=('consolas', 15, "bold"))
        stats_label.grid(padx=5, pady=5, column=0)

        counters = self.user_trips_counters()
        """
        Counters is a list with following:
        - total number of trips at index 0 
        - total number of travel days at index 1
        - total amount (EUR) spent during all trips at index 2
        """

        if counters[0] > 0:
            self.stats_display(counters)
        else:
            no_data_label = ttk.Label(master=self._window,
                                      text=f"No data available. Add a trip with expenses to see statistics.", foreground="red", font=('consolas', 10, "italic"))
            no_data_label.grid(padx=5, pady=5, column=0)

        back_button = ttk.Button(
            master=self._window, text="Back", command=self.user_menu_handle, style='back.TButton')
        back_button.grid(padx=5, pady=5, column=0, sticky=constants.EW)
        style.configure('back.TButton', font=('consolas', 10),
                        background="#5A5A5A", foreground="white")

        self._window.grid_columnconfigure(0, minsize=700)

    def pack(self):
        """Displays the current view."""
        self._window.pack(fill=constants.X)

    def destroy(self):
        """Resets the current view."""
        self._window.destroy()

    def user_trips_counters(self):
        trips_counter = 0
        days_counter = 0
        total_spent_counter = 0
        for trip in self.trips:
            if self.username == trip.username:
                trips_counter += 1
                days_counter += int(trip.duration)
                total_spent_counter += self.trip_expenses_counter(trip.trip_id)

        return [trips_counter, days_counter, total_spent_counter]

    def trip_expenses_counter(self, trip_id):
        id = trip_id
        counter = 0
        for exp in self.expenses:
            if exp.trip_id == id:
                counter += float(exp.amount)
        return counter

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

    def stats_display(self, counters):

        trips_number_label = ttk.Label(
            master=self._window, text=f"Total number of trips: {counters[0]}", font=('consolas', 10))
        trips_number_label.grid(padx=5, pady=5, column=0)

        travel_days_label = ttk.Label(
            master=self._window, text=f"Total number of travel days: {counters[1]}", font=('consolas', 10))
        travel_days_label.grid(padx=5, pady=5, column=0)

        spent_total_label = ttk.Label(
            master=self._window, text=f"Spent in total: €{(counters[2]):.2f}", font=('consolas', 10))
        spent_total_label.grid(padx=5, pady=5, column=0)

        average_trip_label = ttk.Label(
            master=self._window, text=f"Spent per trip on average: €{(counters[2]/counters[0]):.2f}", font=('consolas', 10))
        average_trip_label.grid(padx=5, pady=5, column=0)

        average_day_label = ttk.Label(
            master=self._window, text=f"Spent per day on average: €{(counters[2]/counters[1]):.2f}", font=('consolas', 10))
        average_day_label.grid(padx=5, pady=5, column=0)

        stats = self.stats_sorting()
        """
        stats is a list with following:
        - the cheapest category at index 0
        - the most expensive category at index 1
        - the cheapest expense at index 2
        - the most expensive expense at index 3
        at each index: a tuple with category name at index 0 and cost (as a float number) at index 1
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
