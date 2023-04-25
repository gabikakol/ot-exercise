from init_database import init_users_database, init_trips_database, init_expenses_database

def build():
    init_users_database()
    init_trips_database()
    init_expenses_database()

if __name__ == "__main__":
    build()