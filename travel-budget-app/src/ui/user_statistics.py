from tkinter import ttk
from services.user_service import user_service
from repositories.trip_repository import trip_repository
from repositories.expense_repository import expense_repository


class UserStats:
    def __init__(self, root, user_menu):
        self._root = root
        self._window = None
        self.username = user_service.get_username()
        self.user_menu_handle = user_menu
        self.start()

    def start(self):
        self._window = ttk.Frame(master=self._root)

        stats_label = ttk.Label(master=self._window,
                                text=f"Statistics for {self.username}")
        stats_label.grid(padx=5, pady=5)

        counters = self.user_trips_counters()
        # counters is a list, [0] is number of trips, index [1] is total number of days, index [2] is total spent by user

        trips_number_label = ttk.Label(
            master=self._window, text=f"Total number of trips: {counters[0]}")
        trips_number_label.grid(padx=5, pady=5)

        travel_days_label = ttk.Label(
            master=self._window, text=f"Total number of travel days: {counters[1]}")
        travel_days_label.grid(padx=5, pady=5)

        spent_total_label = ttk.Label(
            master=self._window, text=f"Spent in total: €{(counters[2]):.2f}")
        spent_total_label.grid(padx=5, pady=5)

        average_trip_label = ttk.Label(
            master=self._window, text=f"Spent per trip on average: €{(counters[2]/counters[0]):.2f}")
        average_trip_label.grid(padx=5, pady=5)

        average_day_label = ttk.Label(
            master=self._window, text=f"Spent per day on average: €{(counters[2]/counters[1]):.2f}")
        average_day_label.grid(padx=5, pady=5)

        cheapest_category_label = ttk.Label(
            master=self._window, text="The cheapest category: ")
        cheapest_category_label.grid(padx=5, pady=5)

        expensive_category_label = ttk.Label(
            master=self._window, text="The most expensive category:")
        expensive_category_label.grid(padx=5, pady=5)

        cheapest_label = ttk.Label(
            master=self._window, text="The cheapest item:")
        cheapest_label.grid(padx=5, pady=5)

        expensive_label = ttk.Label(
            master=self._window, text="The most expensive item:")
        expensive_label.grid(padx=5, pady=5)

        back_button = ttk.Button(master=self._window, text="Back to menu")

        back_button = ttk.Button(
            master=self._window, text="Back", command=self.user_menu_handle)
        back_button.grid(padx=5, pady=5)

    def pack(self):
        self._window.pack()

    def destroy(self):
        self._window.destroy()

    def user_trips_counters(self):
        trips = trip_repository.find_all_trips()
        trips_counter = 0
        days_counter = 0
        total_spent_counter = 0
        for trip in trips:
            if self.username == trip.username:
                trips_counter += 1
                days_counter += int(trip.duration)
                total_spent_counter += self.trip_expenses_counter(trip.trip_id)

        return [trips_counter, days_counter, total_spent_counter]

    def trip_expenses_counter(self, trip_id):
        id = trip_id
        expenses = expense_repository.find_all_expenses()
        counter = 0
        for exp in expenses:
            if exp.trip_id == id:
                counter += float(exp.amount)
        return counter
