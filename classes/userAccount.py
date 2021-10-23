import enum

class Role(enum):
    Advisor = 1
    SystemAdmin = 2
    SuperAdmin = 3

class UserAccount:
    def __init__(self, userName, passWord, role) -> None:
        self._userName = userName #with some hashing and make sure this one is unique 
        self._passWord = passWord #with some hashing
        #if role != 1 or 2 return false or so
        self._role = Role(role)
