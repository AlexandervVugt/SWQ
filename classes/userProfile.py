import datetime
from CeasarCypher import cypher

class userProfile:
    def __init__(self, firstname, lastname, username, time = datetime.datetime.now()) -> None:
        self._registrationDate = time
        self.firstName = firstname
        self.lastName = lastname
        self.userName = username
        self.encrypted = False

    def encrypt(self) -> None:
        if not self.encrypted:
            self.firstName = cypher(self.firstName)
            self.lastName = cypher(self.lastName)
            self.userName = cypher(self.userName)
            self.encrypted = True