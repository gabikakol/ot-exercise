from tests.testing_env.test_database_connection import get_database_connection

def drop_users_tables(connection):
    """
    Deletes 'users' tables. 

    Args: 
        connection: Connection object for connecting with the database
    """

    cursor = connection.cursor()
    cursor.execute("""drop table if exists users;""")
    connection.commit()


def drop_trips_tables(connection):
    """
    Deletes 'trips' tables. 

    Args: 
        connection: Connection object for connecting with the database
    """

    cursor = connection.cursor()
    cursor.execute("""drop table if exists trips;""")
    connection.commit()


def drop_expenses_tables(connection):
    """
    Deletes 'expenses' tables. 

    Args: 
        connection: Connection object for connecting with the database
    """

    cursor = connection.cursor()
    cursor.execute("""drop table if exists expenses;""")
    connection.commit()


def create_user_tables(connection):
    """
    Creates 'users' tables for storing usernames and corresponding passwords. 

    Args: 
        connection: Connection object for connecting with the database
    """

    cursor = connection.cursor()
    cursor.execute(
        """create table users (
            username text primary key,
            password text
            );""")
    connection.commit()


def create_trips_tables(connection):
    """
    Creates 'trips' tables for storing user's trips. 
    For each trip, the following are stored: unique trip id, 
    name of the trip, user's username, duration of the trip.  

    Args: 
        connection: Connection object for connecting with the database
    """

    cursor = connection.cursor()
    cursor.execute(
        """create table trips (
            trip_id text primary key, 
            trip_name text, 
            username text, 
            duration text
            );""")
    connection.commit()


def create_expenses_tables(connection):
    """
    Creates 'expenses' tables for storing trips' expenses. 
    For each expense, the following are stored: unique expense id, 
    description of the expense, corresponding trip id, amount paid, category of the expense.  

    Args: 
        connection: Connection object for connecting with the database
    """

    cursor = connection.cursor()
    cursor.execute(
        """create table expenses (
            expense_id text primary key,
            expense_description text, 
            trip_id text, 
            amount text, 
            category text
            );""")
    connection.commit()


def init_users_database():
    """
    Initializes 'users' tables. 
    """

    connection = get_database_connection()
    drop_users_tables(connection)
    create_user_tables(connection)


def init_trips_database():
    """
    Initializes 'trips' tables. 
    """

    connection = get_database_connection()
    drop_trips_tables(connection)
    create_trips_tables(connection)


def init_expenses_database():
    """
    Initializes 'expenses' tables. 
    """

    connection = get_database_connection()
    drop_expenses_tables(connection)
    create_expenses_tables(connection)

if __name__ == "__main__":
    init_users_database()
    init_trips_database()
    init_expenses_database()