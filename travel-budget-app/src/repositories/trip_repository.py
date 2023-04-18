# from entities.trip import Trip
# from database_connection import get_trips_connection


class TripRepository:
    def __init__(self, connection):
        self.connection = connection
