from tkinter import ttk

class Login:
    def __init__(self, root):
        self._root = root
        self.start()
        

    def start(self):
        heading_label = ttk.Label(master=self._root, text="Login")

        username_label = ttk.Label(master=self._root, text="Username")
        username_entry = ttk.Entry(master=self._root)

        password_label = ttk.Label(master=self._root, text="Password")
        password_entry = ttk.Entry(master=self._root)

        button_login = ttk.Button(master=self._root, text="Login")
        button_create_user = ttk.Button(master=self.__root, text="Create a new user")

        heading_label.grid(row=0, column=0, columnspan=2)

        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1)

        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1)

        button_login.grid(row=3, column=0, columnspan=2)
        button_create_user.grid(row=3, column=0, columnspan=2)
