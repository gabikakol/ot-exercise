import unittest
from services.user_service import UserService
from errors.errors_handling import InvalidCridentialsError, UserExistsError, PasswordsDontMatchError, EmptyInputError
from tests.testing_env.test_repository import test_user_repository


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService(test_user_repository)

    def test_create_user(self):
        self.user_service.new_user("gabi", "123", "123")
        self.assertEqual(self.user_service.user.username, "gabi")
        self.assertEqual(self.user_service.user.password, "123")

        self.assertRaises(
            UserExistsError, lambda: self.user_service.new_user("gabi", "123", "123"))
        self.assertRaises(
            EmptyInputError, lambda: self.user_service.new_user("", "123", "123"))
        self.assertRaises(
            EmptyInputError, lambda: self.user_service.new_user("gabi2", "", "123"))
        self.assertRaises(PasswordsDontMatchError, lambda: self.user_service.new_user(
            "gabi2", "123", "456"))

    def test_login(self):
        self.user_service.login("gabi", "123")
        self.assertEqual(self.user_service.user.username, "gabi")
        self.assertEqual(self.user_service.user.password, "123")

        self.assertRaises(InvalidCridentialsError,
                          lambda: self.user_service.login("gabi", "456"))
        self.assertRaises(InvalidCridentialsError,
                          lambda: self.user_service.login("gabi2", "123"))

    def test_logout(self):
        self.user_service.login("gabi", "123")
        self.user_service.logout()
        self.assertEqual(self.user_service.user, None)

    def test_get_username(self):
        self.user_service.login("gabi", "123")
        self.assertEqual(self.user_service.get_username(), "gabi")
