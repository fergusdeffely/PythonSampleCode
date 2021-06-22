from login_menu import LoginMenu
from admin_user import AdminUser
from user import User

# create an empty list of users
users = []

# create some example users - notice the first user is an AdminUser
users.append(AdminUser("Alice", "password", "1234", "alice@test.org", 1))
users.append(User("Bob", "password", "bob@test.org", 2))
users.append(User("Charles", "password", "charles@test.org", 3))

# print out a description of each user
print("\n")
for user in users:
    print(f"{user.description()}")

# update some of the attributes of our users
users[0].update_email_address("alice@admin.org")
users[1].update_id(9)

# print out the descriptions a second time 
# you will notice the updates from the previous two lines of code will be shown
print()
for user in users:
    print(f"{user.description()}")

input("Return to continue: ")

loginMenu = LoginMenu()
loginMenu.show()

# TODO Add datastore
# TODO File access for datastore?