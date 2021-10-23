import random
import string
import enum
import sqlite3
import datetime

con = sqlite3.connect("my_db.db")
cur = con.cursor()


class ApplicationError(Exception):
    pass


def token(prefix, length=10):
    allowed_chars = string.ascii_letters + string.digits
    random_chars = [random.choice(allowed_chars) for x in range(length)]

    return f"{prefix}_{''.join(random_chars)}"


tables = {
    "user": "(id_ text, created_at text, username text, password_hash text, role integer, firstname text, lastname text)",
    "client": "()", # do the same for clients
}



def table_exists(name):
    cur.execute(f"SELECT Count() FROM {name}")
    return bool(cur.fetchone()[0])


for table_name, table_def in tables.items():
    if not table_exists(table_name):
        cur.execute(f"CREATE TABLE {table_name} {table_def}")


class Role(enum):
    ADVISOR = 1
    SYSTEM_ADMIN = 2
    SUPER_ADMIN = 3


class Entry:
    def save(self):
        if self.id:
            # update the object
            pass
        else:
            self.id = token(self.table_name)
            # insert an object into self.table_name values self.serialise()
        pass

    def delete(self):
        if not self.id:
            raise ApplicationError("Cannot delete object that's not saved.")
        else:
            pass
            # delete from self.table_name where id == self.id

    def serialize(self):
        ret = []
        for col_name in self.columns:
            ret.append(getattr(self, col_name))

        return tuple(ret)

    @classmethod
    def load(cls, id_) -> tuple:
        # select * from cls.table_name where id_ == id_ --> row
        return cls.from_row(row)

    @classmethod
    def from_row(cls, row): # returns an instance of a class
        if row:
            obj = cls()
            for i, col_name in enumerate(cls.columns):
                setattr(obj, col_name, row[i])
            return obj
        else:
            raise ApplicationError("Object does not exist")

# row = ("jordan@gmail.com", "2021-09-09", ...)
# - user = User.from_row(row)
# - user = User(username="blah")

class User(Entry):
    table_name = "user"
    columns = [
        "id_",
        "created_at",
        "username",
        "password_hash",
        "role",
        "firstname",
        "lastname",
    ]

    def __init__(
        self,
        id_=None,
        created_at=None,
        username=None,
        password_hash=None,
        role=None,  # Role instance
        firstname=None,
        lastname=None,
    ) -> None:
        self.id = id_
        self.created_at = created_at or datetime.datetime.now().isoformat()
        self.username = username  # with some hashing and make sure this one is unique
        self.firstname = firstname
        self.lastname = lastname
        self.password_hash = password_hash
        self.role = role


class Client(Entry):
    table_name = "client"

    def __init__(
        self,
        id_=None,
        full_name=None,
        address=None,
        created_at=None,
        phone=None,
        email=None,
    ):
        self.id = id_
        self.created_at = created_at or datetime.datetime.now().isoformat()
        self.full_name = full_name
        self.address = address
        self.email = email
        self.phone = phone


class Address:
    def __init__(self, street_name=None, house_number=None, zip_code=None, city=None):
        self.street_name = street_name
        self.house_number = house_number
        self.zip_code = zip_code
        self.city = city

    def validateZipCode(zc: str):
        if len(zc) == 6:
            number = zc[:5]
            letters = zc[5:]
            return number.isdigit() and letters.isalpha()
        else:
            return False


# Username:
# must have a length of at least 5 characters
# must be no longer than 20 characters
# must be started with a letter
# can contain letters (a-z), numbers (0-9), dashes (-), underscores (_), apostrophes ('), and periods (.)
# no distinguish between lowercase or uppercase letters

# Password:
# must have a length of at least 8 characters
# must be no longer than 30 characters
# can contain letters (a-z), (A-Z), numbers (0-9), Special characters such as ~!@#$%^&*_-+=`|\(){}[]:;'<>,.?/
# must have a combination of at least one lowercase letter, one uppercase letter, one digit, and one special characte
