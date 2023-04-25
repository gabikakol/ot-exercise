import uuid


class Trip:
    def __init__(self, trip_id, trip_name, username, duration):
        self.trip_name = trip_name
        self.username = username
        self.duration = duration
        self.trip_id = trip_id or str(uuid.uuid4())
