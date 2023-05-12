from tkinter import ttk, constants
from services.user_service import user_service
from repositories.trip_repository import trip_repository
from services.trip_service import trip_service


class TripsList:
    """Class for user's trips ui."""

    def __init__(self, root, user_menu, new_trip, trip_view):
        """
        Class constructor.

        Args:
            root: tkinter root
            user_menu: user menu window
            new_trip: adding new trip window
            trip_view: trip's details (expenses) view window
        """

        self._root = root
        self._window = None
        self.username = user_service.get_username()
        self.back_handle = user_menu
        self.new_trip_handle = new_trip
        self.trip_view_handle = trip_view

        self.start()

    def start(self):
        self._window = ttk.Frame(master=self._root)
        style = ttk.Style()

        header_label = ttk.Label(
            master=self._window, text=f"{self.username}'s trips", font=('consolas', 15, "bold"))
        header_label.grid(padx=5, pady=5, column=1)

        trips = trip_repository.find_all_trips()
        row = 1
        empty = True
        for trip in trips:
            if trip.username == self.username:
                empty = False
                self.init_trip(trip, row, style)
                row += 1
        if empty:
            none_label = ttk.Label(
                master=self._window, text="No trips yet", foreground="red", font=('consolas', 10, "italic"))
            none_label.grid(padx=5, pady=5, column=1)

        new_trip_button = ttk.Button(
            master=self._window, text="Create new trip", command=self.new_trip_handle, style="new.TButton")
        new_trip_button.grid(padx=5, pady=5, column=1, sticky=constants.EW)
        style.configure('new.TButton', font=('consolas', 10))

        back_button = ttk.Button(
            master=self._window, text="Back to menu", command=self.back_handle, style='back.TButton')
        back_button.grid(padx=5, pady=5, column=1, sticky=constants.EW)
        style.configure('back.TButton', font=('consolas', 10))

        self._window.grid_columnconfigure(0,minsize=150)
        self._window.grid_columnconfigure(1,minsize=400)
        self._window.grid_columnconfigure(3,minsize=150)

    def pack(self):
        """Displays the current view."""
        self._window.pack(fill=constants.X)

    def destroy(self):
        """Resets the current view."""
        self._window.destroy()

    def init_trip(self, trip, row, style):

        trip_name_label = ttk.Label(
            master=self._window, text=trip.trip_name, font=('consolas', 10))
        trip_name_label.grid(row=row, column=1, padx=5, pady=5)

        show_more_button = ttk.Button(
            master=self._window, text="show more", command=lambda: self.show_more_handle(trip), style='show.TButton')
        show_more_button.grid(row=row, column=2, padx=5, pady=5, sticky=constants.EW)
        style.configure('show.TButton', font=('consolas', 10))

    def show_more_handle(self, trip):
        trip_service.trip_login(trip.trip_id, trip.trip_name)
        self.trip_view_handle()
