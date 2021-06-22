from user import User

class AdminUser(User):

    # see comments in user.py on initialisers
    def __init__(self, username, password, employee_number, email_address, id):
        #super(AdminUser, self).__init__(username, password, email_address, id)

        self.username = username
        self.password = password
        self.employee_number = employee_number
        self.email_address = email_address
        self.id = id

    def description(self):
        desc = f"Admin user: {str(self.id).ljust(4)} {self.username.ljust(20)} "
        desc = desc + f"{self.email_address.ljust(25)} {self.employee_number.ljust(10)}"
        return desc
