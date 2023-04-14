from ui.login import Login
from ui.create_user import CreateUser
from ui.user_menu import UserMenu
from ui.trips_list import TripsList
from ui.new_trip import NewTrip


class UI:
    def __init__(self, root):
        self._root = root
        self.window = None
        self.login_view()

    def hide_current_window(self):
        if self.window:
            self.window.destroy()
            # ?
            self.window = None

    def login_view(self):
        self.hide_current_window()
        self.window = Login(self._root, self.user_menu, self.create_user_view)
        self.window.pack()

    def create_user_view(self):
        self.hide_current_window()
        self.window = CreateUser(self._root, self.user_menu, self.login_view)
        self.window.pack()

    def user_menu(self):
        self.hide_current_window()
        self.window = UserMenu(self._root, self.login_view,
                               self.trips_list, self.new_trip)
        self.window.pack()

    def trips_list(self):
        self.hide_current_window()
        self.window = TripsList(self._root, self.user_menu, self.new_trip)
        self.window.pack()

    def new_trip(self):
        self.hide_current_window()
        self.window = NewTrip(self._root, self.trips_list)
        self.window.pack()
