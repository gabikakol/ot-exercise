import unittest
from repositories.user_repository import user_repository
from entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user1 = User('gabi', 'whatever')
        self.user2 = User('billie', 'abc123')

    def test_create_user(self):
        pass

    def test_find_user(self):
        pass

    def test_find_all_users(self):
        pass