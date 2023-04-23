import sqlite3
from config import DATABASE_FILEPATH


def get_database_connection():
    connection_database = sqlite3.connect(DATABASE_FILEPATH)
    connection_database.row_factory = sqlite3.Row
    return connection_database
