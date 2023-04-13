from tkinter import ttk
from services.user_service import user_service


class Login:
    def __init__(self, root, user_menu, create_user_view):
        self._root = root
        self.user_menu = user_menu
        self.create_user = create_user_view
        self._username_entry = None
        self._password_entry = None
        self.widnow = None
        self.start()

    def start(self):
        self.window = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self.window, text="Login:")
        heading_label.grid(padx=5, pady=5)

        username_label = ttk.Label(master=self.window, text="Username")
        username_label.grid(padx=5, pady=5)
        self._username_entry = ttk.Entry(master=self.window)
        self._username_entry.grid(padx=5, pady=5)

        password_label = ttk.Label(master=self.window, text="Password")
        password_label.grid(padx=5, pady=5)
        self._password_entry = ttk.Entry(master=self.window)
        self._password_entry.grid(padx=5, pady=5)

        login_button = ttk.Button(
            master=self.window, text="Login", command=self.handle_login)
        login_button.grid(padx=5, pady=5)

        create_user_button = ttk.Button(
            master=self.window, text="Create user", command=self.create_user)
        create_user_button.grid(padx=5, pady=5)

    def handle_login(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        x = user_service.login(username, password)
        if x:
            self.user_menu()

    def destroy(self):
        self.window.destroy()

    def pack(self):
        self.window.pack()
