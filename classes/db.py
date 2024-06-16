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
    "user": "(id_ integer primary key asc, created_at text, username text, password_hash text, role integer, fullname text)",
    "member": "(id_ integer UNIQUE, registration_date text, fullname text, age integer, gender integer, weight integer, street text, house text, zip text, city text, email text, phone text)", # do the same for clients
}

for table_name, table_def in tables.items():
    cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} {table_def}")

class Role(enum.Enum):
    CONSULTANT = 1
    SYSTEM_ADMIN = 2
    SUPER_ADMIN = 3

class Gender(enum.Enum):
    Male = 1
    Female = 2
    Other = 3

class Entry:
    def save(self):
        cur.execute(f"INSERT INTO {self.table_name} VALUES ({self.serialize()})")

    def delete(self):
        if not self.id:
            raise ApplicationError("Cannot delete object that's not saved.")
        else:
            cur.execute(f"DELETE FROM {self.table_name} WHERE id_ = {self.id_}")

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
        fullname=None,
    ):
        self.id = id_
        self.created_at = created_at or datetime.datetime.now().isoformat()
        self.username = username  # with some hashing and make sure this one is unique
        self.fullname = fullname
        self.password_hash = password_hash
        self.role = role


class Member(Entry):
    table_name = "member"
    columns = [
        "id_",
        "registration_date", 
        "fullname", 
        "age", 
        "gender", 
        "weight", 
        "street", 
        "house", 
        "zip", 
        "city", 
        "email", 
        "phone"
    ]

    def __init__(
        self,
        id_=None,
        fullname=None,
        address=None,
        registration_date=None,
        phone=None,
        email=None,
        street=None, 
        house=None, 
        zip=None, 
        city=None,
        age=None, 
        gender=None, 
        weight=None,
    ):
        self.id = id_
        self.created_at = registration_date or datetime.datetime.now().isoformat()
        self.fullname = fullname
        self.address = address
        self.email = email
        self.phone = phone
        self.street = street
        self.house = house
        self.zip = zip
        self.city = city
        self.age = age
        self.gender = gender
        self.weight = weight
        
    def validateZipCode(zc: str):
        if len(zc) == 6:
            number = zc[:5]
            letters = zc[5:]
            return number.isdigit() and letters.isalpha()
        else:
            return False


# Username:
# must have a length of at least 8 characters
# must be no longer than 10 characters
# must be started with a letter or underscores
# can contain letters (a-z), numbers (0-9), underscores (_), apostrophes ('), and periods (.)
# no distinguish between lowercase or uppercase letters

# Password:
# must have a length of at least 12 characters
# must be no longer than 30 characters
# can contain letters (a-z), (A-Z), numbers (0-9), Special characters such as ~!@#$%^&*_-+=`|\(){}[]:;'<>,.?/
# must have a combination of at least one lowercase letter, one uppercase letter, one digit, and one special character
