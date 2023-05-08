import unittest
from entities.trip import Trip
from services.trip_service import TripService
from errors.errors_handling import EmptyInputError, NotIntegerError
from tests.testing_env.test_repository import test_trip_repository

class TestTripService(unittest.TestCase):
    def setUp(self):
        self.trip_serivce = TripService(test_trip_repository)
        self.trip1 = Trip("a1b2c3", "trip1", "gabi", "15")

    def test_new_trip(self):
        self.trip_serivce.new_trip("zoe", "trip2", "10")
        
        self.assertRaises(EmptyInputError, lambda: self.trip_serivce.new_trip("", "", "10"))
        self.assertRaises(EmptyInputError, lambda: self.trip_serivce.new_trip("gabi", "", ""))
        self.assertRaises(NotIntegerError, lambda: self.trip_serivce.new_trip("gabi", "trip1", "abc"))
        self.assertRaises(NotIntegerError, lambda: self.trip_serivce.new_trip("gabi", "trip1", "10.99"))

    def test_trip_login(self):
        self.trip_serivce.trip_login(self.trip1.trip_id, self.trip1.trip_name)
        self.assertEqual(self.trip_serivce.get_trip_id(), "a1b2c3")
        self.assertEqual(self.trip_serivce.get_trip_name(), "trip1")