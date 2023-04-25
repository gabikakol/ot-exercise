from tkinter import ttk
from services.user_service import user_service


class UserMenu:
    def __init__(self, root, logout_view, trips_list, new_trip, user_stats):
        self._root = root
        self.logout_handle = logout_view
        self.my_trips_handle = trips_list
        self._window = None
        self.create_trip = None
        self.username = user_service.get_username()
        self.new_trip_handle = new_trip
        self.user_stats_handle = user_stats

        self.start()

    def start(self):
        self._window = ttk.Frame(master=self._root)

        user_label = ttk.Label(master=self._window,
                               text=f"Hello {self.username}!")
        user_label.grid(padx=5, pady=5)

        my_trips_button = ttk.Button(
            master=self._window, text="My trips", command=self.my_trips_handle)
        my_trips_button.grid(padx=5, pady=5)

        new_trip_button = ttk.Button(
            master=self._window, text="Create new trip", command=self.new_trip_handle)
        new_trip_button.grid(padx=5, pady=5)

        stats_button = ttk.Button(master=self._window, text="User statistics", command=self.user_stats_handle)
        stats_button.grid(padx=5,pady=5)

        logout_button = ttk.Button(
            master=self._window, text="Log out", command=self.logout_handle)
        logout_button.grid(padx=5, pady=5)

        self._window.grid_columnconfigure(0, weight=1, minsize=400)

    def pack(self):
        self._window.pack()

    def destroy(self):
        self._window.destroy()
