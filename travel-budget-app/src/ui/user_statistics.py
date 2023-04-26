from tkinter import ttk
from services.user_service import user_service


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
                                text=f"Statistics for {self.username}:")
        stats_label.grid(padx=5, pady=5)

        trips_number_label = ttk.Label(
            master=self._window, text=f"Total number of trips:")
        trips_number_label.grid(padx=5, pady=5)

        travel_days_label = ttk.Label(
            master=self._window, text=f"Total number of travel days:")
        travel_days_label.grid(padx=5, pady=5)

        spent_total_label = ttk.Label(
            master=self._window, text=f"Spent in total: €")
        spent_total_label.grid(padx=5, pady=5)

        average_trip_label = ttk.Label(
            master=self._window, text=f"Spent per trip on average:")
        average_trip_label.grid(padx=5, pady=5)

        average_day_label = ttk.Label(
            master=self._window, text=f"Spent per day on average: €X")
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
