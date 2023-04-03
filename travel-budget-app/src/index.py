from tkinter import Tk
from ui.ui import UI

def main():
    window = Tk()
    window.title("Travel budget app")
    window.geometry("540x400")

    ui = UI(window)
    ui.login_start()
    
    window.mainloop()



from initialize_database import initialize_database

def draft():
    initialize_database()
    print("initialize_database works")

if __name__ == "__main__":
    #main()
    draft()
