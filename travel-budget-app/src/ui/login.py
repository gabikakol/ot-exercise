from tkinter import ttk, StringVar, constants
from services.user_service import user_service
from errors.errors_handling import InvalidCridentialsError
import datetime


class Login:
    """Class for login ui."""

    def __init__(self, root, user_menu, create_user_view):
        """
        Class contructor.

        Args:
            root: tkinter root
            user_menu: user menu window
            create_user_view: create user window
        """

        self._root = root
        self.user_menu_handle = user_menu
        self.create_user = create_user_view
        self._username_entry = None
        self._password_entry = None
        self._window = None
        self.error_variable = None
        self.error_label = None
        self.current_time = datetime.datetime.now()

        self.start()

    def start(self):
        self._window = ttk.Frame(master=self._root)
        style = ttk.Style()

        current_date_label = ttk.Label(master=self._window, text=self.current_time.strftime(
            '%H:%M, %A, %dth %B %Y'), foreground="#5A5A5A", font=('consolas', 10))
        current_date_label.grid(padx=5, pady=5, column=1)

        heading_label = ttk.Label(
            master=self._window, text="LOGIN", font=('consolas', 15, "bold"))
        heading_label.grid(padx=5, pady=5, column=1)

        username_label = ttk.Label(
            master=self._window, text="Username:", font=('consolas', 10, "bold"))
        username_label.grid(padx=5, pady=5, column=1)
        self._username_entry = ttk.Entry(
            master=self._window, style="username.TEntry")
        self._username_entry.grid(
            padx=5, pady=5, column=1, sticky=constants.EW)

        password_label = ttk.Label(
            master=self._window, text="Password:", font=('consolas', 10, "bold"))
        password_label.grid(padx=5, pady=5, column=1)
        self._password_entry = ttk.Entry(master=self._window, show="*")
        self._password_entry.grid(
            padx=5, pady=5, column=1, sticky=constants.EW)

        self.error_variable = StringVar(self._window)
        self.error_label = ttk.Label(
            master=self._window, textvariable=self.error_variable, foreground="red", font=('consolas', 10, "bold"))
        self.error_label.grid(padx=5, pady=5, column=1)

        login_button = ttk.Button(
            master=self._window, text="Login", command=self.handle_login, style="login.TButton")
        login_button.grid(padx=5, pady=5, column=1, sticky=constants.EW)
        style.configure("login.TButton", font=('consolas', 10),
                        background="#5A5A5A", foreground="white")

        create_user_button = ttk.Button(
            master=self._window, text="Create a new user", command=self.create_user, style="create.TButton")
        create_user_button.grid(padx=5, pady=5, column=1, sticky=constants.EW)
        style.configure("create.TButton", font=('consolas', 10),
                        background="#5A5A5A", foreground="white")

        self.hide_error()

        self._window.grid_columnconfigure(0, minsize=200)
        self._window.grid_columnconfigure(1, minsize=300)

    def handle_login(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            user_service.login(username, password)
            self.user_menu_handle()
        except InvalidCridentialsError:
            self.show_error("Invalid username or password.")

    def show_error(self, text):
        self.error_variable.set(text)
        self.error_label.grid()

    def hide_error(self):
        self.error_label.grid_remove()

    def destroy(self):
        """Displays the current view."""
        self._window.destroy()

    def pack(self):
        """Resets the current view."""
        self._window.pack(fill=constants.X)
