import sqlite3
from config import DATABASE_FILEPATH, TRIPS_FILEPATH

connection_database = sqlite3.connect(DATABASE_FILEPATH)
connection_database.row_factory = sqlite3.Row

connection_trips = sqlite3.connect(TRIPS_FILEPATH)
connection_trips.row_factory = sqlite3.Row

def get_database_connection():
    return connection_database

def get_trips_connection():
    return connection_trips