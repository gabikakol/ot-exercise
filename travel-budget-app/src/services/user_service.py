from entities.user import User
# from entities.trip import Trip
from repositories.user_repository import user_repository
# from repositories.trip_repository import trip_repository


class UserService:
    def __init__(self, user_rep=user_repository):
        self.user_rep = user_rep
        # self.trip_rep = trip_rep
        self.user = None

    def new_user(self, username, password):
        exists = self.user_rep.find_user(username)
        if exists:
            print('error username is not unique')
            return None
            # change this
        self.user_rep.create_user(User(username, password))
        print('user created successfully')
        self.login(username, password)

    def login(self, username, password):
        user = self.user_rep.find_user(username)

        if not user:
            print('error user doesnt exist')
            return None
        if password != user.password:
            print('error incorrect password')
            return None
        self.user = user
        print('login successfull')
        # case sensitive or not?
        return user

    def logout(self):
        self.user = None

    """
    def create_trip(self, trip):
        trip = Trip(trip=trip, user=self.user)
        return self.trip_rep.create_trip(trip)
    """

    def get_username(self):
        return self.user.username


user_service = UserService()
