from entities.trip import Trip
from database_connection import get_database_connection


class TripRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_trip(self, trip):
        cursor = self.connection.cursor()
        cursor.execute("insert into trips (trip_id, trip_name, username, duration) values (?, ?, ?, ?);", #pylint: disable=line-too-long
                       (trip.trip_id, trip.trip_name, trip.username, trip.duration))
        self.connection.commit()

    def find_all_trips(self):
        cursor = self.connection.cursor()
        rows = cursor.execute("select * from trips").fetchall()
        return [Trip(row["trip_id"], row["trip_name"], row["username"], row["duration"]) for row in rows] #pylint: disable=line-too-long

    def find_trip(self, trip_id):
        cursor = self.connection.cursor()
        cursor.execute("select * from trips where trip_id = ?", (trip_id,))
        row = cursor.fetchone()
        if row:
            return Trip(row["trip_id"], row["trip_name"], row["username"], row["duration"])
        return None

    def delete(self):
        cursor = self.connection.cursor()
        cursor.execute("delete from trips")
        self.connection.commit()


trip_repository = TripRepository(get_database_connection())
