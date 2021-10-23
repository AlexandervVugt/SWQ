from db import Client

class AccessError(Exception):
    pass

class AccessManager:
    """ Used to perform actions that require check of permissions """

    def update_password(user, obj, new_pass):
# - [ ] To update their own password
# Manager.update_password(initiating_user, other_user, "some_pass")
        if user == obj or user.role == Role.SUPER_ADMIN:
            pass
        elif user.role == Role.SYSTEM_ADMIN and obj.role == Role.ADVISOR:
            pass
        else:
            raise AccessError("Insufficient rights to do this action.")

    def add_new_client(full_name):
        new_client = Client(full_name=full_name)
        new_client.save()



## Advisor set + sys admin + super admin
# - [ ] To add a new client to the system
# - [ ] To modify or update the information of a client in the system
# - [ ] To search and retrieve the information of a client


# System Administrators + super admin
# - [ ] To check the list of users and their roles
# - [ ] To define and add a new advisor to the system
# - [ ] To modify or update an existing advisor’s account and profile
# - [ ] To delete an existing advisor’s account
# - [ ] To reset an existing advisor’s password (a temporary password)
# - [ ] To make a backup of the system (clients information and users’ data)
# - [ ] To see the logs file(s) of the system
# - [ ] To delete a client's record from the database (note that an advisor can not delete a record, but can only modify or update a client’s information)

# Super Admin
# - [ ] To define and add a new admin to the system
# - [ ] To modify or update an existing admin’s account and profile
# - [ ] To delete an existing admin’s account
# - [ ] To reset an existing admin’s password (a temporary password)