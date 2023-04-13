from pathlib import Path
from entities.trip import Trip
#from repositories.user_repository import user_repository
from config import TRIPS_FILEPATH

class TripRepository:

    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        trips = []
        Path(self.filepath).touch()
        with open(self.filepath, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                contents = row.split(";")
                id = contents[0]
                name = contents[1]
                user = contents[2]
                trips.append(Trip(name, user, id))

    def all_trips(self):
        self.read()

    def write(self, trips):
        Path(self.filepath).touch()
        with open(self.filepath, "w", encoding="utf-8") as file:
            for trip in trips:
                user = trip.user.username 
                row = f"{trip.id}{trip.name}{user}"
                file.write(row+"\n")

    def find_username(self, username):
        trips = self.all_trips()
        user = filter(
            lambda x: x.user and x.user.username == username, trips)
        return list(user)
    
    def create_trip(self, trip):
        trips = self.all_trips()
        trips.append(trip)
        self.write(trips)
        return trip
    
    def delete(self):
        self.write([])

trip_repository = TripRepository(TRIPS_FILEPATH)