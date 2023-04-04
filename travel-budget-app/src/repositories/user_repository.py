from entities.user import User
from database_connection import get_database_connection

class UserRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_user(self, user):
        cursor = self.connection.cursor()
        cursor.execute("insert into users (username, password) values (?, ?);", (user.username, user.password))
        self.connection.commit()
        return user
    
    def find_user(self, username):
        cursor = self.connection.cursor()
        cursor.execute("select * from users where username = ?;", (username,))
        row = cursor.fetchone()
        if row:
            return User(row["username"], row["password"]) 
        else:
            return None
    
    def find_all_users(self):
        cursor = self.connection.cursor()
        rows = cursor.execute("select * from users;").fetchall()
        return [User(row["username"], row["password"]) for row in rows]
    
    def delete(self):
        cursor = self.connection.cursor()
        cursor.execute("delete from users")
        self.connection.commit()

user_repository = UserRepository(get_database_connection())
