from entities.trip import Trip
from repositories.trip_repository import trip_repository
from errors.errors_handling import EmptyInputError, NotIntegerError


class TripService:
    def __init__(self, trip_rep=trip_repository):
        self.trip_rep = trip_rep
        self.trip_id = None
        self.trip_name = None

    def new_trip(self, username, trip_name, duration):
        if not trip_name or not duration:
            raise EmptyInputError("Trip name and duration cannot be empty")

        if not duration.isdigit():
            raise NotIntegerError("Trip duration input has to be an integer")

        self.trip_rep.create_trip(
            Trip(None, username, trip_name, duration))

    def trip_login(self, trip_id, name):
        self.trip_id = trip_id
        self.trip_name = name

    def get_trip_id(self):
        return self.trip_id

    def get_trip_name(self):
        return self.trip_name


trip_service = TripService()
