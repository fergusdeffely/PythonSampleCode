from login_menu import LoginMenu
from admin_user import AdminUser
from user import User

users = []

users.append(AdminUser("Alice", "password", "1234", "alice@test.org", 1))
users.append(User("Bob", "password", "bob@test.org", 2))
users.append(User("Charles", "password", "charles@test.org", 3))

print("\n")
for user in users:
    print(f"{user.description()}")

users[0].update_email_address("alice@admin.org")
users[1].update_id(9)

print()
for user in users:
    print(f"{user.description()}")

print()

loginMenu = LoginMenu()
loginMenu.show()