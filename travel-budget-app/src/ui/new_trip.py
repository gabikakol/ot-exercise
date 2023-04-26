from tkinter import ttk, StringVar
from services.trip_service import trip_service
from services.user_service import user_service
from errors.errors_handling import EmptyInputError, NotIntegerError

class NewTrip:
    def __init__(self, root, trips_list):
        self._root = root
        self.trips_list_handle = trips_list
        self._window = None
        self.name_entry = None
        self.duration_entry = None
        self.error_variable = None
        self.error_label = None
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

        self.error_variable = StringVar(self._window)
        self.error_label = ttk.Label(master=self._window, textvariable=self.error_variable, foreground="red")
        self.error_label.grid(padx=5,pady=5)

        save_button = ttk.Button(
            master=self._window, text="Save", command=self.handle_new_trip)
        save_button.grid(padx=5, pady=5)

        cancel_button = ttk.Button(
            master=self._window, text="Cancel", command=self.trips_list_handle)
        cancel_button.grid(padx=5, pady=5)

        self.hide_error()

    def pack(self):
        self._window.pack()

    def destroy(self):
        self._window.destroy()

    def handle_new_trip(self):
        username = user_service.get_username()
        trip_name = self.name_entry.get()
        duration = self.duration_entry.get()
        
        self.hide_error()
        try:
            trip_service.new_trip(trip_name, username, duration)
            self.trips_list_handle()
        except EmptyInputError:
            self.show_error("Trip name and duration cannot be empty")
        except NotIntegerError:
            self.show_error("Trip duration has to be an integer")

    def show_error(self,text):
        self.error_variable.set(text)
        self.error_label.grid()

    def hide_error(self):
        self.error_label.grid_remove()
