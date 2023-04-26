class InvalidCridentialsError(Exception):
    pass

class UserExistsError(Exception):
    pass

class PasswordsDontMatchError(Exception):
    pass

class EmptyInputError(Exception):
    pass

class NotIntegerError(Exception):
    pass

class NotFloatError(Exception):
    pass

class CatNotSelectedError(Exception):
    pass

#trip duration ha to be an integer
#expense has to be float
#category has to be selected ie cannot be 'select an option'