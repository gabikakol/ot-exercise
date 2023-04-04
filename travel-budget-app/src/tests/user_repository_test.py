import unittest
from repositories.user_repository import user_repository
from entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete()
        self.user1 = User('gabi', 'whatever')
        self.user2 = User('billie', 'abc123')

    def test_create_user(self):
        user_repository.create_user(self.user1)
        users_list = user_repository.find_all_users()
        self.assertEqual(users_list[-1].username, self.user1.username)

    def test_find_user(self):
        user_repository.create_user(self.user2)
        user_found = user_repository.find_user(self.user2.username)
        self.assertEqual(user_found.username, self.user2.username)

    def test_find_all_users(self):
        user_repository.create_user(self.user1)
        user_repository.create_user(self.user2)
        users_all = user_repository.find_all_users()
        self.assertEqual(users_all[-2].username, self.user1.username)
        self.assertEqual(users_all[-1].username, self.user2.username)
