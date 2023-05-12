from entities.trip import Trip
from repositories.trip_repository import trip_repository
from errors.errors_handling import EmptyInputError, NotIntegerError


class TripService:
    """Class responsible for the application logic related to trips."""

    def __init__(self, trip_rep=trip_repository):
        """
        Class constructor.

        Args:
            trip_rep: TripRepository object (default value is trip_repository)
        """

        self.trip_rep = trip_rep
        self.trip_id = None
        self.trip_name = None

    def new_trip(self, trip_name, username, duration):
        """
        Creates a new trip to the database if the inputs are valid.

        Args:
            username: username of the user who created the trip
            trip_name: name of the trip
            duration: duration of the trip in days

        Raises:
            EmptyInputError: if the trip name or duration inputs are empty
            NotIntegerError: if the duration input is not an integer value
        """

        if not trip_name or not duration:
            raise EmptyInputError("Trip name and duration cannot be empty")

        if not duration.isdigit():
            raise NotIntegerError("Trip duration input has to be an integer")

        self.trip_rep.create_trip(
            Trip(None, trip_name, username, duration))

    def trip_login(self, trip_id, name):
        """
        Saves the trip id and name of the currently accessed trip,
        such that they can be accessed using functions get_trip_id() and get_trip_name().
        """

        self.trip_id = trip_id
        self.trip_name = name

    def get_trip_id(self):
        return self.trip_id

    def get_trip_name(self):
        return self.trip_name


# This variable will be used by the application and services
# to avoid making multiple instances of TripService
trip_service = TripService()
