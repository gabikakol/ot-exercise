import unittest
from entities.user import User
from services.user_service import UserService
from errors.errors_handling import InvalidCridentialsError, UserExistsError, PasswordsDontMatchError, EmptyInputError

"""
class FakeUserRepo:
    def __init__(self, users=None):
        self.users = users or []

    def create_user(self, user):
        self.users.append(user)

    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None
            
    def find_all(self):
        return self.users
    
    
class TestUserService(unittest.TestCase):
    def setUp(self): 
        self.user_service = UserService(FakeUserRepo())
        self.user1 = User("gabby", "123")

    def test_create_user(self):
        pass

    def test_login(self):
        pass

    def test_logout(self):
        pass

    def test_get_username(self):
        pass
"""