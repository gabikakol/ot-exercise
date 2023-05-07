from tkinter import ttk, StringVar
from services.user_service import user_service
from errors.errors_handling import InvalidCridentialsError


class Login:
    """Class for login ui"""

    def __init__(self, root, user_menu, create_user_view):
        """class contructor"""

        self._root = root
        self.user_menu_handle = user_menu
        self.create_user = create_user_view
        self._username_entry = None
        self._password_entry = None
        self._window = None
        self.error_variable = None
        self.error_label = None

        self.start()

    def start(self):
        self._window = ttk.Frame(master=self._root)
        style = ttk.Style()

        heading_label = ttk.Label(
            master=self._window, text="LOGIN", font=('consolas', 15, "bold"))
        heading_label.grid(padx=5, pady=5)

        username_label = ttk.Label(
            master=self._window, text="Username:", font=('consolas', 10, "bold"))
        username_label.grid(padx=5, pady=5)
        self._username_entry = ttk.Entry(master=self._window)
        self._username_entry.grid(padx=5, pady=5)

        password_label = ttk.Label(
            master=self._window, text="Password:", font=('consolas', 10, "bold"))
        password_label.grid(padx=5, pady=5)
        self._password_entry = ttk.Entry(master=self._window, show="*")
        self._password_entry.grid(padx=5, pady=5)

        self.error_variable = StringVar(self._window)
        self.error_label = ttk.Label(
            master=self._window, textvariable=self.error_variable, foreground="red", font=('consolas', 10, "bold"))
        self.error_label.grid(padx=5, pady=5)

        login_button = ttk.Button(
            master=self._window, text="Login", command=self.handle_login, style="login.TButton")
        login_button.grid(padx=5, pady=5)
        style.configure("login.TButton", font=('consolas', 10))

        create_user_button = ttk.Button(
            master=self._window, text="Create user", command=self.create_user, style="create.TButton")
        create_user_button.grid(padx=5, pady=5)
        style.configure("create.TButton", font=('consolas', 10))

        self.hide_error()

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
        """displays the current view"""
        self._window.destroy()

    def pack(self):
        """resets the current view"""
        self._window.pack()
