import unittest
from entities.user import User
from tests.testing_env.test_repository import test_user_repository
from tests.testing_env.test_init_database import init_users_database

class TestTripRepository(unittest.TestCase):
    def setUp(self):
        init_users_database()
        self.trip1 = User("gabby", "123")
        self.trip2 = User("fedorka", "abc12")

    def test_create_new_user(self):
        test_user_repository.create_user(self.trip1)
        all_users = test_user_repository.find_all_users()

        self.assertEqual(len(all_users), 1)
        self.assertEqual(all_users[0].username, "gabby")
        self.assertEqual(all_users[0].password, "123")

    def test_find_user(self):
        user = test_user_repository.find_user("gabby")
        self.assertEqual(user, None)

        test_user_repository.create_user(self.trip1)
        user = test_user_repository.find_user("gabby")

        self.assertEqual(user.username, "gabby")

    def test_find_all_users(self):
        test_user_repository.create_user(self.trip1)
        test_user_repository.create_user(self.trip2)
        all_users = test_user_repository.find_all_users()

        self.assertEqual(len(all_users), 2)
        self.assertEqual(all_users[0].username, "gabby")
        self.assertEqual(all_users[1].username, "fedorka")