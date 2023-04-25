from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title("Travel budget app")
    window.geometry("700x700")

    UI(window)
    window.mainloop()


if __name__ == "__main__":
    main()
