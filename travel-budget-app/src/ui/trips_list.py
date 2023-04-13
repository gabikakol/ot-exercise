from tkinter import ttk, constants

class TripsList:
    def __init__(self, root, trips):
        self._root = root
        self.trips = trips
        self.window = None

        self.start()

    def start(self):
        self.window = ttk.Frame(master=self._root)
        for trip in self.trips:
            trip_window = ttk.Frame(master=self.window)
            trip_label = ttk.Label(master=trip_window, text=trip.name)

    def pack(self):
        self.window.pack(fill=constants.X)

    def destroy(self):
        self.window.destroy()