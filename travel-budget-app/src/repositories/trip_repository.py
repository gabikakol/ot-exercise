from entities.trip import Trip
from database_connection import get_database_connection


class TripRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_trip(self, username, trip_name, duration, category):
        cursor = self.connection.cursor()
        cursor.execute("insert into trips (trip_name, username, duration, category) values (?, ?, ?, ?);", (trip_name, username, duration, category))
        self.connection.commit()

    def find_all_trips(self):
        cursor = self.connection.cursor()
        rows = cursor.execute("select * from trips").fetchall()
        return [Trip(row["trip_name"], row["username"], row["trip_duration"], row["category"]) for row in rows]
    
    def find_trip(self, trip_name):
        cursor = self.connection.cursor()
        cursor.execute("select * from trips where trip_name = ?", (trip_name))
        row = cursor.fetchone()
        if row:
            return Trip(row["trip_name"], row["username"], row["trip_duration"], row["category"])
        return None
        
trip_repository = TripRepository(get_database_connection())
