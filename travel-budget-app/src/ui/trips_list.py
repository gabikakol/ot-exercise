from tkinter import ttk, constants
from services.user_service import user_service
from repositories.trip_repository import trip_repository
from services.trip_service import trip_service


class TripsList:
    """Class for user's trips ui"""

    def __init__(self, root, user_menu, new_trip, trip_view):
        """class constructor"""

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
        header_label.grid(padx=5, pady=5)

        trips = trip_repository.find_all_trips()
        row = 1
        for trip in trips:
            if trip.username == self.username:
                self.init_trip(trip, row, style)
                row += 1
        if row == 1:
            none_label = ttk.Label(
                master=self._window, text="No trips yet", font=('consolas', 10, "italic"))
            none_label.grid(padx=5, pady=5)

        new_trip_button = ttk.Button(
            master=self._window, text="Create new trip", command=self.new_trip_handle, style="new.TButton")
        new_trip_button.grid(padx=5, pady=5)
        style.configure('new.TButton', font=('consolas', 10))

        back_button = ttk.Button(
            master=self._window, text="Back to menu", command=self.back_handle, style='back.TButton')
        back_button.grid(padx=5, pady=5)
        style.configure('back.TButton', font=('consolas', 10))

    def pack(self):
        """displays the current view"""
        self._window.pack()

    def destroy(self):
        """resets the current view"""
        self._window.destroy()

    def init_trip(self, trip, row, style):

        trip_name_label = ttk.Label(
            master=self._window, text=trip.trip_name, font=('consolas', 10))
        trip_name_label.grid(row=row, column=0, padx=5, pady=5)

        show_more_button = ttk.Button(
            master=self._window, text="show more", command=lambda: self.show_more_handle(trip), style='show.TButton')
        show_more_button.grid(row=row, column=1, padx=5, pady=5)
        style.configure('show.TButton', font=('consolas', 10))

    def show_more_handle(self, trip):
        trip_service.trip_login(trip.trip_id, trip.trip_name)
        self.trip_view_handle()
