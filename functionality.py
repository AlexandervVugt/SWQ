from classes.userAccount import UserAccount

def change_pw(user: UserAccount) -> None:
    pass

def check_users(user: UserAccount) -> None:
    pass

def add_advisor(user: UserAccount) -> None:
    pass

def update_advisor(user: UserAccount) -> None:
    pass

def delete_advisor(user: UserAccount) -> None:
    pass

def reset_advisor_password(user: UserAccount) -> None:
    pass

def add_admin(user: UserAccount) -> None:
    pass

def update_admin(user: UserAccount) -> None:
    pass

def delete_admin(user: UserAccount) -> None:
    pass

def reset_admin_password(user: UserAccount) -> None:
    pass

def backup(user: UserAccount) -> None:
    pass

def logs(user: UserAccount) -> None:
    pass

def add_client(user: UserAccount) -> None:
    pass

def update_client(user: UserAccount) -> None:
    pass

def delete_client(user: UserAccount) -> None:
    pass

def search_client(user: UserAccount) -> None:
    pass

advisor_func = {
    0: (change_pw, "Change my password."),
    1: (add_client, "Add a new client to the system."),
    2: (update_client, "Modify or update the information of a client in the system."),
    3: (search_client, "Search and retrieve the information of a client")
}

admin_func = {
    0: (change_pw, "Change my password."),
    1: (check_users, "Check the list of users and their roles."),
    2: (add_advisor, "Define and add a new advisor to the system."),
    3: (update_advisor, "Modify or update an existing advisor's account and profile."),
    4: (delete_advisor, "Delete an existing advisor's account."),
    5: (reset_advisor_password, "Reset an existing advisor's password (a temporary password)."),
    6: (backup, "Make a backup of the system."),
    7: (logs, "View the logs file."),
    8: (add_client, "Add a new client to the system."),
    9: (update_client, "Modify or update the information of a client in the system."),
    10: (search_client, "Search and retrieve the information of a client"),
    11: (delete_client, "Delete a client's record from the database.")
}

root_func = {
    1: (check_users, "Check the list of users and their roles."),
    2: (add_advisor, "Define and add a new advisor to the system."),
    3: (update_advisor, "Modify or update an existing advisor's account and profile."),
    4: (delete_advisor, "Delete an existing advisor's account."),
    5: (reset_advisor_password, "Reset an existing advisor's password (a temporary password)."),
    6: (add_admin, "Define and add a new admin to the system."),
    7: (update_admin, "Modify or update an existing admin's account and profile."),
    8: (delete_admin, "Delete an existing admin's account."),
    9: (reset_admin_password, "Reset an existing admin's password (a temporary password)."),
    10: (backup, "Make a backup of the system."),
    11: (logs, "View the logs file."),
    12: (add_client, "Add a new client to the system."),
    13: (update_client, "Modify or update the information of a client in the system."),
    14: (search_client, "Search and retrieve the information of a client"),
    15: (delete_client, "Delete a client's record from the database.")
}