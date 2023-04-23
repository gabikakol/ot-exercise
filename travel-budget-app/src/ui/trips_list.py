from tkinter import ttk
from services.user_service import user_service
from repositories.trip_repository import trip_repository


class TripsList:
    def __init__(self, root, user_menu, new_trip):
        self._root = root
        self._window = None
        self.username = user_service.get_username()
        self.back_handle = user_menu
        self.new_trip_handle = new_trip
        self.start()

    def start(self):
        self._window = ttk.Frame(master=self._root)

        header_label = ttk.Label(
            master=self._window, text=f"{self.username}'s trips:")
        header_label.grid(padx=5, pady=5)

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
