import uuid

class Trip:

    def __init__(self, trip, user=None, trip_id=None):
        self.trip = trip
        self.user = user
        self.trip_id = trip_id or str(uuid.uuid4())