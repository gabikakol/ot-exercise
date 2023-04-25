from entities.trip import Trip
from repositories.trip_repository import trip_repository


class TripService:
    def __init__(self, trip_rep=trip_repository):
        self.trip_rep = trip_rep
        self.trip_id = None
        self.trip_name = None
        """
        self.username = None
        self.trip_name = None
        self.trip_duration = None
        self.category = None
        """

    def new_trip(self, username, trip_name, duration):
        if trip_name and duration:
            self.trip_rep.create_trip(
                Trip(None, username, trip_name, duration))
            print("trip added successfully")
        else:
            print("new trip error")

    def trip_login(self, id, name):
        self.trip_id = id
        self.trip_name = name

    def get_trip_id(self):
        return self.trip_id

    def get_trip_name(self):
        return self.trip_name


trip_service = TripService()
