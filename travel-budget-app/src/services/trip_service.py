from entities.trip import Trip
from repositories.trip_repository import trip_repository


class TripService:
    def __init__(self, trip_rep=trip_repository):
        self.trip_rep = trip_rep
        self.trip = None
        """
        self.username = None
        self.trip_name = None
        self.trip_duration = None
        self.category = None
        """

    def new_trip(self, username, trip_name, duration, category):
        if trip_name and duration and category != "select an option":
            self.trip_rep.create_trip(
                Trip(username, trip_name, duration, category))
            print("trip added successfully")
        else:
            print("new trip error")

    def get_trip_name(self):
        return None


trip_service = TripService()
