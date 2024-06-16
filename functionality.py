from classes.db import User

def change_pw(user: User) -> None:
    pass

def check_users(user: User) -> None:
    pass

def add_consultant(user: User) -> None:
    pass

def update_consultant(user: User) -> None:
    pass

def delete_consultant(user: User) -> None:
    pass

def reset_consultant_password(user: User) -> None:
    pass

def add_admin(user: User) -> None:
    pass

def update_admin(user: User) -> None:
    pass

def delete_admin(user: User) -> None:
    pass

def reset_admin_password(user: User) -> None:
    pass

def backup(user: User) -> None:
    pass

def logs(user: User) -> None:
    pass

def add_member(user: User) -> None:
    pass

def update_member(user: User) -> None:
    pass

def delete_member(user: User) -> None:
    pass

def search_member(user: User) -> None:
    pass

consultant_func = {
    0: (change_pw, "Change my password."),
    1: (add_member, "Add a new member to the system."),
    2: (update_member, "Modify or update the information of a member in the system."),
    3: (search_member, "Search and retrieve the information of a member")
}

admin_func = {
    0: (change_pw, "Change my password."),
    1: (check_users, "Check the list of users and their roles."),
    2: (add_consultant, "Define and add a new consultant to the system."),
    3: (update_consultant, "Modify or update an existing consultant's account and profile."),
    4: (delete_consultant, "Delete an existing consultant's account."),
    5: (reset_consultant_password, "Reset an existing consultant's password (a temporary password)."),
    6: (backup, "Make a backup of the system."),
    7: (logs, "View the logs file."),
    8: (add_member, "Add a new member to the system."),
    9: (update_member, "Modify or update the information of a member in the system."),
    10: (search_member, "Search and retrieve the information of a member"),
    11: (delete_member, "Delete a member's record from the database.")
}

root_func = {
    1: (check_users, "Check the list of users and their roles."),
    2: (add_consultant, "Define and add a new consultant to the system."),
    3: (update_consultant, "Modify or update an existing consultant's account and profile."),
    4: (delete_consultant, "Delete an existing consultant's account."),
    5: (reset_consultant_password, "Reset an existing consultant's password (a temporary password)."),
    6: (add_admin, "Define and add a new admin to the system."),
    7: (update_admin, "Modify or update an existing admin's account and profile."),
    8: (delete_admin, "Delete an existing admin's account."),
    9: (reset_admin_password, "Reset an existing admin's password (a temporary password)."),
    10: (backup, "Make a backup of the system."),
    11: (logs, "View the logs file."),
    12: (add_member, "Add a new member to the system."),
    13: (update_member, "Modify or update the information of a member in the system."),
    14: (search_member, "Search and retrieve the information of a member"),
    15: (delete_member, "Delete a member's record from the database.")
}