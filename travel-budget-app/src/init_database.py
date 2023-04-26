from database_connection import get_database_connection


def drop_users_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""drop table if exists users;""")
    connection.commit()


def drop_trips_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""drop table if exists trips;""")
    connection.commit()


def drop_expenses_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""drop table if exists expenses;""")
    connection.commit()


def create_user_tables(connection):
    cursor = connection.cursor()
    cursor.execute(
        """create table users (username text primary key,password text);""")
    connection.commit()


def create_trips_tables(connection):
    cursor = connection.cursor()
    cursor.execute(
        """create table trips (trip_id text primary key, trip_name text, username text, duration text);""")
    connection.commit()


def create_expenses_tables(connection):
    cursor = connection.cursor()
    cursor.execute(
        """create table expenses (expense_id text primary key,expense_description text, trip_id text, amount text, category text);""")
    connection.commit()


def init_users_database():
    connection = get_database_connection()
    drop_users_tables(connection)
    create_user_tables(connection)


def init_trips_database():
    connection = get_database_connection()
    drop_trips_tables(connection)
    create_trips_tables(connection)


def init_expenses_database():
    connection = get_database_connection()
    drop_expenses_tables(connection)
    create_expenses_tables(connection)

