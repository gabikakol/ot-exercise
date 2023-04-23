from database_connection import get_database_connection


def drop_users_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""drop table if exists users;""")
    connection.commit()


def drop_trips_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""drop table if exists trips;""")
    connection.commit()


def create_user_tables(connection):
    cursor = connection.cursor()
    cursor.execute(
        """create table users (username text primary key,password text);""")
    connection.commit()


def create_trips_tables(connection):
    cursor = connection.cursor()
    cursor.execute(
        """create table trips (trip_name text primary key,username text, duration text, category text);""")
    # add later: duration text, category text
    connection.commit()


def init_users_database():
    connection = get_database_connection()
    drop_users_tables(connection)
    create_user_tables(connection)


def init_trips_database():
    connection = get_database_connection()
    drop_trips_tables(connection)
    create_trips_tables(connection)


if __name__ == "__main__":
    init_users_database()
    init_trips_database()
