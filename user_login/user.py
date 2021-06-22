
class User:

    def __init__(self, username, password, email_address, id):
        self.username = username
        self.password = password
        self.email_address = email_address
        self.id = id

    def description(self):
        return f"{str(self.id).ljust(4)} {self.username.ljust(20)} {self.email_address.ljust(25)}"

    def update_email_address(self, new_email):
        self.email_address = new_email

    def update_id(self, new_id):
        self.id = new_id    

users = []

users.append(User("Alice", "password", "alice@test.org", 1))
users.append(User("Bob", "password", "bob@test.org", 2))
users.append(User("Charles", "password", "charles@test.org", 3))

print("\n")
for user in users:
    print(f"{user.description()}")

users[0].update_email_address("alice@domain.org")
users[1].update_id(9)

print()
for user in users:
    print(f"{user.description()}")

# TODO: auto-generate id