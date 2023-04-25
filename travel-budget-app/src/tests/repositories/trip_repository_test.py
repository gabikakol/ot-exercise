import unittest
from repositories.trip_repository import trip_repository
from entities.trip import Trip


class TestTripRepository(unittest.TestCase):
    def setUp(self):
        trip_repository.delete()
        self.trip1 = Trip("123", "trip1", "gaby", "4")
        self.trip2 = Trip("345", "trip2", "gaby", "7")

    def test_create_new_trip(self):
        trip_repository.create_trip(self.trip1)
        trips_list = trip_repository.find_all_trips()
        self.assertEqual(trips_list[-1].trip_id, self.trip1.trip_id)
        trip_repository.delete()

    def test_find_trip(self):
        trip_repository.create_trip(self.trip2)
        trip_found = trip_repository.find_trip("345")
        self.assertEqual(trip_found.trip_id, self.trip2.trip_id)
        trip_repository.delete()

    def test_find_all_trips(self):
        trip_repository.create_trip(self.trip1)
        trip_repository.create_trip(self.trip2)
        trips_all = trip_repository.find_all_trips()
        self.assertEqual(trips_all[-2].trip_id, self.trip1.trip_id)
        self.assertEqual(trips_all[-1].trip_id, self.trip2.trip_id)
        trip_repository.delete()
