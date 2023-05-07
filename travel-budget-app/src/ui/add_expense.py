from tkinter import ttk, StringVar
from services.expense_service import expense_service
from services.trip_service import trip_service
from errors.errors_handling import EmptyInputError, NotFloatError, CatNotSelectedError


class AddExpense:
    """Class for adding new expense ui"""

    def __init__(self, root, trip_view):
        """class constructor"""

        self._root = root
        self._window = None
        self.trip_view_handle = trip_view
        self.description_entry = None
        self.amount_entry = None
        self.cat_var = None
        self.error_variable = None
        self.error_label = None

        self.start()

    def start(self):

        self._window = ttk.Frame(master=self._root)

        header_label = ttk.Label(
            master=self._window, text="ADD AN EXPENSE", font=('consolas', 13, "bold"))
        header_label.grid(padx=5, pady=5)

        description_label = ttk.Label(
            master=self._window, text="Description:", font=('consolas', 10, "bold"))
        description_label.grid(padx=5, pady=5)

        self.description_entry = ttk.Entry(master=self._window)
        self.description_entry.grid(padx=5, pady=5)

        amount_label = ttk.Label(
            master=self._window, text="Cost (EUR):", font=('consolas', 10, "bold"))
        amount_label.grid(padx=5, pady=5)

        self.amount_entry = ttk.Entry(master=self._window)
        self.amount_entry.grid(padx=5, pady=5)

        category_label = ttk.Label(
            master=self._window, text="Category:", font=('consolas', 10, "bold"))
        category_label.grid(padx=5, pady=5)

        categories = ['select an option', 'groceries', 'restaurants', 'cafes', 'bars', 'laundry',
                      'transportation', 'accommodation', 'tickets', 'currency exchange commissions', 'activities', 'other']
        self.cat_var = StringVar(self._root)
        category_menu = ttk.OptionMenu(self._window, self.cat_var, *categories)
        category_menu.grid(padx=5, pady=5)

        self.error_variable = StringVar(self._window)
        self.error_label = ttk.Label(
            master=self._window, textvariable=self.error_variable, foreground="red", font=('consolas', 10, "bold"))
        self.error_label.grid(padx=5, pady=5)

        save_button = ttk.Button(
            master=self._window, text="Save", command=self.handle_add_expense)
        save_button.grid(padx=5, pady=5)

        cancel_button = ttk.Button(
            master=self._window, text="Cancel", command=self.trip_view_handle)
        cancel_button.grid(padx=5, pady=5)

        self.hide_error()

    def pack(self):
        """displays the current view"""
        self._window.pack()

    def destroy(self):
        """resets the current view"""
        self._window.destroy()

    def handle_add_expense(self):

        description = self.description_entry.get()
        amount = self.amount_entry.get()
        category = self.cat_var.get()
        trip_id = trip_service.get_trip_id()

        try:
            expense_service.add_expense(description, trip_id, amount, category)
            self.trip_view_handle()
        except EmptyInputError:
            self.show_error("Expense description and cost cannot be empty.")
        except NotFloatError:
            self.show_error(
                "Expense cost has to be a numeric value (use '.' if input is a fraction).")
        except CatNotSelectedError:
            self.show_error("Category has to be selected.")

    def show_error(self, text):

        self.error_variable.set(text)
        self.error_label.grid()

    def hide_error(self):
        self.error_label.grid_remove()
