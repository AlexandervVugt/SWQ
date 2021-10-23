from typing import Tuple
from classes.db import User, Role
from functionality import *

user = None

def Main():
    welcome()
    login()
    quit = False
    while not quit:
        quit = action_prompt()

def welcome():
    print("Welcome to the Clients Data Management System!")

def login():
    global user
    while user is None:
        creds = credentials_prompt()
        if creds[0] == "superadmin" and creds[1] == "Admin!23":
            user = User(username="superadmin", password_hash="Admin!23", role=Role.SuperAdmin)
        else:
            pass #TODO: Implement creds checking in db

def credentials_prompt() -> Tuple:
    print("Please login to proceed.")
    uname = input("username: ")
    pw = input("password: ")
    return (uname, pw)

def action_prompt() -> bool:
    func = get_func()
    print("Please indicate the number of the action you want to perform, or 'q' to quit.")
    for key, value in func.items():
        print(str(key), ":\t", value[1])
    choice = input("Number:\t")
    if choice == 'q':
        return True
    else:
        try:
            choice = int(choice)
            func[choice][0](user)   #Executes the chosen function
        except:
            print("An error occured, please try again.")
        finally:
            return False


def get_func() -> dict:
    if user == None:
        raise PermissionError("This action is only allowed for logged in users.")
    elif user._role == Role.Advisor:
        return advisor_func
    elif user._role == Role.SystemAdmin:
        return admin_func
    elif user._role == Role.SuperAdmin:
        return root_func
    else:
        raise RuntimeError("Unknown user role.")

if __name__=="__main__":
    Main()