from init_database import init_users_database, init_trips_database, init_expenses_database


def build():
    init_users_database()
    init_trips_database()
    init_expenses_database()


# Allows to call the function using command line
if __name__ == "__main__":
    build()
