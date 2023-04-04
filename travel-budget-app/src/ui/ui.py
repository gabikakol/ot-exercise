from ui.login import Login
from ui.create_user import CreateUser

class UI:
    def __init__(self, root):
        self._root = root
        self.window = None
        self.login_view()

    def hide_current_window(self):
        if self.window:
            self.window.destroy()
            #?
            self.window = None

    def login_view(self):
        self.hide_current_window()
        self.window = Login(self._root, self.create_user_view)
        self.window.pack()

    def create_user_view(self):
        self.hide_current_window()
        self.window = CreateUser(self._root, self.login_view)
        self.window.pack()