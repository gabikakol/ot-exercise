from tkinter import ttk

class UI:
    def __init__(self, root):
        self._root = root
        self.login_start()
        #self.create_user_start()

    def login_start(self):
        heading_label = ttk.Label(master=self._root, text="Login")

        username_label = ttk.Label(master=self._root, text="Username")
        username_entry = ttk.Entry(master=self._root)

        password_label = ttk.Label(master=self._root, text="Password")
        password_entry = ttk.Entry(master=self._root)

        button_login = ttk.Button(master=self._root, text="Login")
        button_create_user = ttk.Button(master=self._root, text="Create a new user")

        heading_label.grid(row=0, column=0, columnspan=2)

        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1)

        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1)

        button_login.grid(row=3, column=0, columnspan=2)
        button_create_user.grid(row=4, column=0, columnspan=2)

    def create_user_start(self):
        pass
        