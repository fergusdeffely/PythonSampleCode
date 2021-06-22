
class User:

    # __init__ method is the class 'initialiser'
    #   a general purpose method for initialising a class
    #   in this case, it sets the values of our class attributes (username, password,
    #   email_address and id) to the values passed as parameters of the same names

    def __init__(self, username, password, email_address, id):
        # set username attribute to the value of the username parameter
        #   self.username refers to the attribute
        #   username refers to the parameter
        # the attribute variable will be retained by the object
        # the parameter will no longer exist after the method (init) completes
        self.username = username
        # same pattern as username for password, email_address and id
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
