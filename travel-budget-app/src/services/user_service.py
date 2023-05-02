from entities.user import User
from repositories.user_repository import user_repository
from errors.errors_handling import InvalidCridentialsError, UserExistsError, PasswordsDontMatchError, EmptyInputError  # pylint: disable=line-too-long


class UserService:
    """Class responsible for the application logic related to users"""

    def __init__(self, user_rep=user_repository):
        """class constructor"""

        self.user_rep = user_rep
        self.user = None

    def new_user(self, username, password1, password2):
        exists = self.user_rep.find_user(username)
        if exists:
            raise UserExistsError(f"Username {username} already exists")
        if not username:
            raise EmptyInputError("Username input cannot be empty")
        if not password1 or not password2:
            raise EmptyInputError("Password input cannot be empty")
        if password1 != password2:
            raise PasswordsDontMatchError("Passwords don't match")
        self.user_rep.create_user(User(username, password1))
        self.login(username, password1)

    def login(self, username, password):
        user = self.user_rep.find_user(username)

        if not user or password != user.password:
            raise InvalidCridentialsError("Invalid username or password")
        self.user = user
        return user

    def logout(self):
        self.user = None

    def get_username(self):
        return self.user.username


user_service = UserService()
