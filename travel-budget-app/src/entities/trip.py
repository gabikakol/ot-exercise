import uuid


class Trip:
    """
    Class representing a trip.

    Attributes:
        trip_id: unique id of the trip 
        trip_name: name of the trip
        username: username of the user who created the trip
        duration: duration of the trip in days
    """

    def __init__(self, trip_id, trip_name, username, duration):
        self.trip_name = trip_name
        self.username = username
        self.duration = duration
        self.trip_id = trip_id or str(uuid.uuid4())
