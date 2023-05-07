from entities.trip import Trip
from database_connection import get_database_connection


class TripRepository:
    """Class responsible for database operations related to trips"""

    def __init__(self, connection):
        """class constructor"""

        self.connection = connection

    def create_trip(self, trip):
        """
        Saves a new trips to the 'trips' database.

        Args:
            trip: Trip object to be stored in the database
        """

        cursor = self.connection.cursor()
        cursor.execute(
            "insert into trips (trip_id, trip_name, username, duration) values (?, ?, ?, ?);",
            (trip.trip_id, trip.trip_name, trip.username, trip.duration))
        self.connection.commit()

    def find_all_trips(self):
        """
        Function finds and returns all trips from the 'trips' database.

        Returns:
            list of Trip objects
        """

        cursor = self.connection.cursor()
        rows = cursor.execute("select * from trips").fetchall()
        return [Trip(row["trip_id"], row["trip_name"],
                     row["username"], row["duration"]) for row in rows]

    def find_trip(self, trip_id):
        """
        Searches and returns a particular trip based on its id.

        Args:
            trip_id: unique id number of the trip

        Returns:
            Particular Trip object if there exists such trip in the database with the given id. 
            Otherwise None
        """

        cursor = self.connection.cursor()
        cursor.execute("select * from trips where trip_id = ?", (trip_id,))
        row = cursor.fetchone()
        if row:
            return Trip(row["trip_id"], row["trip_name"], row["username"], row["duration"])
        return None

    """
    def delete(self):
        
        #Deletes all trips from the 'trips' database.
        

        cursor = self.connection.cursor()
        cursor.execute("delete from trips")
        self.connection.commit()
    """


trip_repository = TripRepository(get_database_connection())
