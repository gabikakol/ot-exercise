from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""drop table if exists users;""")
    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute(
        """create table users (username text primary key,password text);""")
    connection.commit()


def init_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)
