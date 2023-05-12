from tkinter import ttk, constants
from services.user_service import user_service
import datetime


class UserMenu:
    """Class for user's main menu ui."""

    def __init__(self, root, logout_view, trips_list, new_trip, user_stats):
        """
        Class constructor.

        Args:
            root: tkinter root
            logout_view: login window
            trips_list: trips list view window
            new_trip: creating new trip window
            user_stats: user's statistics window
        """

        self._root = root
        self.logout_handle = logout_view
        self.my_trips_handle = trips_list
        self._window = None
        self.create_trip = None
        self.username = user_service.get_username()
        self.new_trip_handle = new_trip
        self.user_stats_handle = user_stats
        self.current_time = datetime.datetime.now()

        self.start()

    def start(self):

        self._window = ttk.Frame(master=self._root)
        style = ttk.Style()

        current_date_label = ttk.Label(master=self._window, text=self.current_time.strftime('%H:%M, %A, %dth %B %Y'), foreground="#5A5A5A", font=('consolas', 10))
        current_date_label.grid(padx=5, pady=5, column=1)

        user_label = ttk.Label(master=self._window,
                               text=f"Hello {self.username}!", font=('consolas', 15, "bold"))
        user_label.grid(padx=5, pady=5, column=1)

        my_trips_button = ttk.Button(
            master=self._window, text="My trips", command=self.my_trips_handle, style="my.TButton")
        my_trips_button.grid(padx=5, pady=5, column=1, sticky=constants.EW)
        style.configure('my.TButton', font=('consolas', 10),
                        background="#5A5A5A", foreground="white")

        new_trip_button = ttk.Button(
            master=self._window, text="Create new trip", command=self.new_trip_handle, style="new.TButton")
        new_trip_button.grid(padx=5, pady=5, column=1, sticky=constants.EW)
        style.configure('new.TButton', font=('consolas', 10),
                        background="#5A5A5A", foreground="white")

        stats_button = ttk.Button(
            master=self._window, text="User statistics", command=self.user_stats_handle, style="stats.TButton")
        stats_button.grid(padx=5, pady=5, column=1, sticky=constants.EW)
        style.configure('stats.TButton', font=('consolas', 10),
                        background="#5A5A5A", foreground="white")

        logout_button = ttk.Button(
            master=self._window, text="Log out", command=self.logout_handle, style='logout.TButton')
        logout_button.grid(padx=5, pady=5, column=1, sticky=constants.EW)
        style.configure('logout.TButton', font=('consolas', 10),
                        background="#5A5A5A", foreground="white")

        self._window.grid_columnconfigure(0, minsize=200)
        self._window.grid_columnconfigure(1, minsize=300)

    def pack(self):
        """Displays the current view."""
        self._window.pack(fill=constants.X)

    def destroy(self):
        """Resets the current view."""
        self._window.destroy()
