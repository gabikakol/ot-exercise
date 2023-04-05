from entities.user import User
from repositories.user_repository import user_repository as x

class UserService:
    def __init__(self, user_rep = x):
        self.user_rep = user_rep
        self.user = None

    def new_user(self, username, password):
        exists = self.user_rep.find_user(username)
        if exists:
            print('error username is not unique')
        else:
            user = self.user_rep.create_user(User(username, password))
            print('user created successfully')
            return user
    
    def login(self, username, password):
        user = self.user_rep.find_user(username)

        if not user:
            print('error user doesnt exist')
        
        elif password != user.password:
            print('error incorrect password')

        else:
            self.user = user
            print('login successfull')
            return user
        
    def logout(self):
        self.user = None

user_service = UserService()