from tkinter import ttk, StringVar

class NewTrip:
    def __init__(self, root, trips_list):
        self._root = root
        self.trips_list_handle = trips_list
        self._window = None
        self.start()

    def start(self):
        self._window = ttk.Frame(master=self._root)

        header_label = ttk.Label(master=self._window, text="New trip")
        header_label.grid(padx=5, pady=5)

        name_label = ttk.Label(master=self._window, text="Name")
        name_label.grid(padx=5, pady=5)
        self.name_entry = ttk.Entry(master=self._window)
        self.name_entry.grid(padx=5, pady=5)

        duration_label = ttk.Label(master=self._window, text="Duration (days)")
        duration_label.grid(padx=5, pady=5)
        self.duration_entry = ttk.Entry(master=self._window)
        self.duration_entry.grid(padx=5, pady=5)

        cathegory_label = ttk.Label(master=self._window, text="Cathegory")
        cathegory_label.grid(padx=5, pady=5)

        cathegories = ['select an option','groceries', 'restaurants', 'cafes', 'bars', 'laundry', 'transportation', 'accommodation', 'tickets', 'currency exchange commissions', 'activities', 'other']
        tkvar = StringVar(self._root)
        #tkvar.set('Select an option')
        cathegory_menu = ttk.OptionMenu(self._window, tkvar, *cathegories)
        cathegory_menu.grid(padx=5,pady=5)
        

        save_button = ttk.Button(
            master=self._window, text="Save", command=self.trips_list_handle)
        save_button.grid(padx=5, pady=5)

        self._window.grid_columnconfigure(0, weight=1, minsize=400)

    def pack(self):
        self._window.pack()

    def destroy(self):
        self._window.destroy()