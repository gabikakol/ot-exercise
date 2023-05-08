from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    """Class responsible for database operations related to users"""

    def __init__(self, connection):
        """
        Class constructor.

        Args:
            connection: database connection object
        """

        self.connection = connection

    def create_user(self, user):
        """
        Saves a new user to the 'users' database.

        Args:
            user: User object to be stored in the database
        """

        cursor = self.connection.cursor()
        cursor.execute("insert into users (username, password) values (?, ?);",
                       (user.username, user.password))
        self.connection.commit()
        return user

    def find_user(self, username):
        """
        Searches and returns a particular user based on its username.

        Args:
            username: unique username of the user

        Returns:
            Particular User object if there exists such 
            user in the database with the given username. 
            Otherwise None
        """

        cursor = self.connection.cursor()
        cursor.execute("select * from users where username = ?;", (username,))
        row = cursor.fetchone()
        if row:
            return User(row["username"], row["password"])
        return None

    def find_all_users(self):
        """
        Function finds and returns all users from the 'users' database.

        Returns:
            list of User objects
        """

        cursor = self.connection.cursor()
        rows = cursor.execute("select * from users;").fetchall()
        return [User(row["username"], row["password"]) for row in rows]


user_repository = UserRepository(get_database_connection())
