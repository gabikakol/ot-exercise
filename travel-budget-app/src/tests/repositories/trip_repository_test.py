import unittest
from entities.trip import Trip
from tests.testing_env.test_repository import test_trip_repository
from tests.testing_env.test_init_database import init_trips_database

class TestTripRepository(unittest.TestCase):
    def setUp(self):
        init_trips_database()
        self.trip1 = Trip("123", "trip1", "gaby", "4")
        self.trip2 = Trip("345", "trip2", "gaby", "7")

    def test_create_new_trip(self):
        test_trip_repository.create_trip(self.trip1)
        all_trips = test_trip_repository.find_all_trips()

        self.assertEqual(len(all_trips), 1)
        self.assertEqual(all_trips[0].trip_id, "123")
        self.assertEqual(all_trips[0].trip_name, "trip1")
        self.assertEqual(all_trips[0].username, "gaby")
        self.assertEqual(all_trips[0].duration, "4")

    def test_find_trip(self):
        trip = test_trip_repository.find_trip("123")
        self.assertEqual(trip, None)

        test_trip_repository.create_trip(self.trip1)
        trip = test_trip_repository.find_trip("123")

        self.assertEqual(trip.trip_id, "123")

    def test_find_all_trips(self):
        test_trip_repository.create_trip(self.trip1)
        test_trip_repository.create_trip(self.trip2)
        all_trips = test_trip_repository.find_all_trips()

        self.assertEqual(len(all_trips), 2)
        self.assertEqual(all_trips[0].trip_id, "123")
        self.assertEqual(all_trips[1].trip_id, "345")