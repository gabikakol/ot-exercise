from ui.login import Login
from ui.create_user import CreateUser
from ui.user_menu import UserMenu
from ui.trips_list import TripsList
from ui.new_trip import NewTrip
from ui.trip_view import TripView
from ui.add_expense import AddExpense
from ui.trip_statistics import TripStats
from ui.user_statistics import UserStats


class UI:
    """
    Class responsible for the user interface of the application. 
    """

    def __init__(self, root):
        """
        Class constructor. 

        Args: 
            root: tkinter element, used for passing the created ui
        """
        self._root = root
        self.window = None
        self.login_view()

    def hide_current_window(self):
        """
        Resets the current view (if it exists).
        """
        if self.window:
            self.window.destroy()
            self.window = None

    def login_view(self):
        """"
        Initializes the login ui window.
        """

        self.hide_current_window()
        self.window = Login(self._root, self.user_menu, self.create_user_view)
        self.window.pack()

    def create_user_view(self):
        """"
        Initializes the ui window for creating new user.
        """

        self.hide_current_window()
        self.window = CreateUser(self._root, self.user_menu, self.login_view)
        self.window.pack()

    def user_menu(self):
        """
        Initializes the ui window for the main user menu.
        """

        self.hide_current_window()
        self.window = UserMenu(self._root, self.login_view,
                               self.trips_list, self.new_trip, self.user_stats)
        self.window.pack()

    def trips_list(self):
        """
        Initializes the ui window for viewing the user's trips.
        """

        self.hide_current_window()
        self.window = TripsList(
            self._root, self.user_menu, self.new_trip, self.trip_view)
        self.window.pack()

    def new_trip(self):
        """
        Initializes the ui window for creating new trip.
        """

        self.hide_current_window()
        self.window = NewTrip(self._root, self.trips_list)
        self.window.pack()

    def trip_view(self):
        """
        Initializes the ui window for viewing trip's expenses.
        """

        self.hide_current_window()
        self.window = TripView(self._root, self.trips_list,
                               self.add_expense, self.trip_stats)
        self.window.pack()

    def add_expense(self):
        """
        Initializes the ui window for adding new expense.
        """

        self.hide_current_window()
        self.window = AddExpense(self._root, self.trip_view)
        self.window.pack()

    def trip_stats(self):
        """
        Initializes the ui window for viewing trip's statistics.
        """

        self.hide_current_window()
        self.window = TripStats(self._root, self.trip_view)
        self.window.pack()

    def user_stats(self):
        """
        Initializes the ui window for viewing user's statistics.
        """

        self.hide_current_window()
        self.window = UserStats(self._root, self.user_menu)
        self.window.pack()
