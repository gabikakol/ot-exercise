from tkinter import ttk, constants
from services.user_service import user_service

class TripsView:
    def __init__(self, root, logout_view):
        self._root = root
        self.logout_handle = logout_view
        self._window = None
        self.create_trip = None
        self.username = user_service.get_username()

        self.start()

    def start(self):
        self._window = ttk.Frame(master=self._root)
        
        #only header for now and logout button
        user_label = ttk.Label(master=self._window, text=f"Hello {self.username}!")
        user_label.grid(row=0,column=0,padx=5,pady=5)
        logout_button = ttk.Button(master=self._window, text="Log out", command=self.logout_handle)
        logout_button.grid(row=1,column=0,padx=5,pady=5)

        self._window.grid_columnconfigure(0, weight=1, minsize=400)


    def pack(self):
        self._window.pack(fill=constants.X)

    def destroy(self):
        self._window.destroy()