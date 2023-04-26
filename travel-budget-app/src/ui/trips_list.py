from tkinter import ttk
from services.user_service import user_service
from repositories.trip_repository import trip_repository
from services.trip_service import trip_service


class TripsList:
    def __init__(self, root, user_menu, new_trip, trip_view):
        self._root = root
        self._window = None
        self.username = user_service.get_username()
        self.back_handle = user_menu
        self.new_trip_handle = new_trip
        self.trip_view_handle = trip_view
        self.start()

    def start(self):
        self._window = ttk.Frame(master=self._root)

        header_label = ttk.Label(
            master=self._window, text=f"{self.username}'s trips:")
        header_label.grid(padx=5, pady=5)

        trips = trip_repository.find_all_trips()
        for trip in trips:
            if trip.username == self.username:
                self.init_trip(trip)
            """
            if trip.username == self.username:
                name_label = ttk.Label(master=self._window, text=trip.trip_name)
                name_label.grid(padx=5, pady=5, row=i,column=0)
                more_button = ttk.Button(master=self._window, text="show more", command=self.trip_view_handle)
                more_button.grid(padx=5,pady=5, row=i,column=1)
                i += 1
            """

        new_trip_button = ttk.Button(
            master=self._window, text="Create new trip", command=self.new_trip_handle)
        new_trip_button.grid(padx=5, pady=5)

        back_button = ttk.Button(
            master=self._window, text="Back to menu", command=self.back_handle)
        back_button.grid(padx=5, pady=5)

        self._window.grid_columnconfigure(0, weight=1, minsize=400)

    def pack(self):
        self._window.pack()

    def destroy(self):
        self._window.destroy()

    def init_trip(self, trip):
        trip_name_label = ttk.Label(master=self._window, text=trip.trip_name)
        trip_name_label.grid(padx=5, pady=5)

        show_more_button = ttk.Button(
            master=self._window, text="show more", command=lambda: self.show_more_handle(trip))
        show_more_button.grid(padx=5, pady=5)
        
    def show_more_handle(self, trip):
        trip_service.trip_login(trip.trip_id, trip.trip_name)
        self.trip_view_handle()
