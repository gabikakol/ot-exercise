from tkinter import ttk
from services.trip_service import trip_service
from repositories.expense_repository import expense_repository
from repositories.trip_repository import trip_repository


class TripStats:
    def __init__(self, root, trip_view):
        self._root = root
        self.trip_view_handle = trip_view
        self._window = None
        self.trip_name = trip_service.get_trip_name()
        self.trip_id = trip_service.get_trip_id()
        self.expenses = expense_repository.find_all_expenses()
        self.current_trip = trip_repository.find_trip(self.trip_id)
        self.start()

    def start(self):
        self._window = ttk.Frame(master=self._root)

        stats_label = ttk.Label(
            master=self._window, text=f"Statistics of the {self.trip_name} trip:")
        stats_label.grid(padx=5, pady=5)

        sum = self.spent_total()
        self.trip_duration()
        self.spent_per_day(sum)

        cheapest_label = ttk.Label(
            master=self._window, text="The cheapest item:")
        cheapest_label.grid(padx=5, pady=5)

        expensive_label = ttk.Label(
            master=self._window, text="The most expensive item:")
        expensive_label.grid(padx=5, pady=5)

        cheapest_category_label = ttk.Label(
            master=self._window, text="The cheapest category: ")
        cheapest_category_label.grid(padx=5, pady=5)

        expensive_category_label = ttk.Label(
            master=self._window, text="The most expensive category:")
        expensive_category_label.grid(padx=5, pady=5)

        # spent in total
        # days (length of the trip)
        # spent per day on average
        # spent per category
        # cheapest item
        # most expensive item
        # most expensive category

        # table?:
        # groceries', 'restaurants', 'cafes', 'bars', 'laundry','transportation', 'accommodation', 'tickets', 'currency exchange commissions', 'activities', 'other

        back_button = ttk.Button(
            master=self._window, text="Back", command=self.trip_view_handle)
        back_button.grid(padx=5, pady=5)

    def pack(self):
        self._window.pack()

    def destroy(self):
        self._window.destroy()

    def spent_total(self):
        sum = 0
        for exp in self.expenses:
            if exp.trip_id == self.trip_id:
                sum += float(exp.amount)

        spent_total_label = ttk.Label(
            master=self._window, text=f"Spent in total: €{sum}")
        spent_total_label.grid(padx=5, pady=5)
        return sum

    def trip_duration(self):
        duration_label = ttk.Label(
            master=self._window, text=f"Duration of the trip: {self.current_trip.duration} days")
        duration_label.grid(padx=5, pady=5)

    def spent_per_day(self, sum):
        average = sum/int(self.current_trip.duration)
        average_day_label = ttk.Label(
            master=self._window, text=f"Spent per day on average: €{average}")
        average_day_label.grid(padx=5, pady=5)
