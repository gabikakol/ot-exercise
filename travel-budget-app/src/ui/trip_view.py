from tkinter import ttk
from services.trip_service import trip_service

class TripView:
    def __init__(self, root, trips_list, add_expense):
        self._root = root
        self.trips_list_handle = trips_list
        self._window = None
        self.add_expense = add_expense
        self.start()


    def start(self):
        self._window = ttk.Frame(master=self._root)
        header_label = ttk.Label(master=self._window, text=f"Expenses of the X trip")
        header_label.grid(padx=5, pady=5)

        add_button = ttk.Button(master=self._window, text="Add expense", command = self.add_expense)
        add_button.grid(padx=5,pady=5)

        stats_button = ttk.Button(master=self._window, text="Statistics")
        stats_button.grid(padx=5,pady=5)

        back_button = ttk.Button(master=self._window, text="Back to trips menu", command=self.trips_list_handle)
        back_button.grid(padx=5,pady=5)

        #add expense
        #statistics

    def pack(self):
        self._window.pack()

    def destroy(self):
        self._window.destroy()
