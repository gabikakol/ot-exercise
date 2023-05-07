from tkinter import ttk, StringVar
from services.user_service import user_service
from errors.errors_handling import UserExistsError, PasswordsDontMatchError, EmptyInputError


class CreateUser:
    """Class for creating a new user ui"""

    def __init__(self, root, user_menu, login_view):
        """class constructor"""

        self._root = root
        self.user_menu = user_menu
        self.login_view = login_view
        self._window = None
        self._username_entry = None
        self._password_entry1 = None
        self._password_entry2 = None
        self.error_variable = None
        self.error_label = None

        self.start()

    def start(self):

        self._window = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._window, text="CREATE A NEW USER", font=('consolas', 13, "bold"))
        heading_label.grid(padx=5, pady=5)

        username_label = ttk.Label(
            master=self._window, text="Username:", font=('consolas', 10, "bold"))
        username_label.grid(padx=5, pady=5)
        self._username_entry = ttk.Entry(master=self._window)
        self._username_entry.grid(padx=5, pady=5)

        password_label1 = ttk.Label(
            master=self._window, text="Password:", font=('consolas', 10, "bold"))
        password_label1.grid(padx=5, pady=5)
        self._password_entry1 = ttk.Entry(master=self._window, show="*")
        self._password_entry1.grid(padx=5, pady=5)

        password_label2 = ttk.Label(
            master=self._window, text="Repeat password:", font=('consolas', 10, "bold"))
        password_label2.grid(padx=5, pady=5)
        self._password_entry2 = ttk.Entry(master=self._window, show="*")
        self._password_entry2.grid(padx=5, pady=5)

        save_button = ttk.Button(
            master=self._window, text="Save and log in", command=self.handle_create_user)
        save_button.grid(padx=5, pady=5)

        self.error_variable = StringVar(self._window)
        self.error_label = ttk.Label(
            master=self._window, textvariable=self.error_variable, foreground="red", font=('consolas', 10, "bold"))
        self.error_label.grid(padx=5, pady=5)

        cancel_button = ttk.Button(
            master=self._window, text="Cancel", command=self.login_view)
        cancel_button.grid(padx=5, pady=5)

        self.hide_error()

    def handle_create_user(self):
        username = self._username_entry.get()
        password1 = self._password_entry1.get()
        password2 = self._password_entry2.get()

        self.hide_error()

        try:
            user_service.new_user(username, password1, password2)
            self.user_menu()
        except EmptyInputError:
            self.show_error("Username and password cannot be empty.")
        except UserExistsError:
            self.show_error(f"Username {username} already exists.")
        except PasswordsDontMatchError:
            self.show_error("Passwords don't match.")

    def show_error(self, text):
        self.error_variable.set(text)
        self.error_label.grid()

    def hide_error(self):
        self.error_label.grid_remove()

    def destroy(self):
        """resets the current view"""
        self._window.destroy()

    def pack(self):
        """displays the current view"""
        self._window.pack()
