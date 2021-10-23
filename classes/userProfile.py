import datetime

class userProfile:
    def __init__(self, firstname, lastname, username, time = datetime.datetime.now()) -> None:
        self._registrationDate = time
        self.firstName = firstname
        self.lastName = lastname
        self.userName = username