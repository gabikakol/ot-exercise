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

    def new_trip(self, username, trip_name, duration):
        if trip_name and duration:
            self.trip_rep.create_trip(
                Trip(None, username, trip_name, duration))
            print("trip added successfully")
        else:
            print("new trip error")




trip_service = TripService()
