from entities.user import User
from repositories.user_repository import user_repository
from errors.errors_handling import InvalidCridentialsError, UserExistsError, PasswordsDontMatchError, EmptyInputError  # pylint: disable=line-too-long


class UserService:
    """Class responsible for the application logic related to users."""

    def __init__(self, user_rep=user_repository):
        """
        Class constructor.

        Args:
            user_rep: UserRepository object (default value is user_repository)
        """

        self.user_rep = user_rep
        self.user = None

    def new_user(self, username, password1, password2):
        """
        Creates a new user to the database if the cridentials are valid, and logs it in.

        Args:
            username: unique username of the user
            password1: password of the user
            password2: repeated password of the user (has to be the same as password1)

        Raises:
            UserExistsError: if the username already exists in the database
            EmptyInputError: if the username or password inputs are empty
            PasswordsDontMatchError: if the password1 and password2 don't match
        """

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
        """
        Logs in a user if the cridentials (username and password) are valid.

        Args:
            username: unique username of the user
            password: password of the user

        Returns: 
            User object if the username and password are valid

        Raises:
            InvalidCridentialsError: if the username or password are not valid
        """

        user = self.user_rep.find_user(username)

        if not user or password != user.password:
            raise InvalidCridentialsError("Invalid username or password")
        self.user = user
        return user

    def logout(self):
        """Logs out the user."""

        self.user = None

    def get_username(self):
        """Returns the username of the logged in user."""

        return self.user.username


# This variable will be used by the application and services to avoid making multiple instances of UserService
user_service = UserService()
