from tkinter import Tk
from ui.ui import UI

def main():
    window = Tk()
    window.title("Travel budget app")
    window.geometry("540x400")

    ui = UI(window)    
    window.mainloop()

"""
from init_database import init_database

def draft():
    init_database()
    print("init_database works")
"""

if __name__ == "__main__":
    main()
    #draft()
