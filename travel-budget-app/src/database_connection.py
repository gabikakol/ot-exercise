import sqlite3
from config import DATABASE_FILEPATH

connection = sqlite3.connect(DATABASE_FILEPATH)
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
