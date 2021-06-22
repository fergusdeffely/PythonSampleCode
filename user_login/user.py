
class User:

    def __init__(self, username, password, email_address, id):
        self.username = username
        self.password = password
        self.email_address = email_address
        self.id = id

    def description(self):
        return f"User:       {str(self.id).ljust(4)} {self.username.ljust(20)} {self.email_address.ljust(25)}"

    def update_email_address(self, new_email):
        self.email_address = new_email

    def update_id(self, new_id):
        self.id = new_id

# TODO: add method(s) to update username? and password
