from tkinter import ttk
from services.user_service import user_service


class CreateUser:
    def __init__(self, root, trips_view, login_view):
        self._root = root
        self.trips_view = trips_view
        self.login_view = login_view
        self.window = None
        self._username_entry = None
        self._password_entry1 = None
        self._password_entry2 = None
        self.start()

    def start(self):
        self.window = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self.window, text="Create a new user:")
        heading_label.grid(padx=5, pady=5)

        username_label = ttk.Label(master=self.window, text="Username")
        username_label.grid(padx=5, pady=5)
        self._username_entry = ttk.Entry(master=self.window)
        self._username_entry.grid(padx=5, pady=5)

        password_label1 = ttk.Label(master=self.window, text="Password")
        password_label1.grid(padx=5, pady=5)
        self._password_entry1 = ttk.Entry(master=self.window)
        self._password_entry1.grid(padx=5, pady=5)

        password_label2 = ttk.Label(master=self.window, text="Repeat password")
        password_label2.grid(padx=5, pady=5)
        self._password_entry2 = ttk.Entry(master=self.window)
        self._password_entry2.grid(padx=5, pady=5)

        save_button = ttk.Button(
            master=self.window, text="Save and log in", command=self.handle_create_user)
        save_button.grid(padx=5, pady=5)

        login_menu_button = ttk.Button(
            master=self.window, text="Login menu", command=self.login_view)
        login_menu_button.grid(padx=5, pady=5)

    def handle_create_user(self):
        username = self._username_entry.get()
        password1 = self._password_entry1.get()
        password2 = self._password_entry2.get()
        password_final = None
        if password1 == password2:
            password_final = password1
        else:
            print('error passwords dont match')
        if password_final:
            user_service.new_user(username, password_final)
            self.trips_view()

    def destroy(self):
        self.window.destroy()

    def pack(self):
        self.window.pack()
