
class User:

    # __init__ method is the class 'initialiser'
    #   a general purpose method for initialising a class
    #   in this case, it sets the values of our class attributes (username, password,
    #   email_address and id) to the values passed as parameters of the same names

    def __init__(self, username, password, email_address, id):
        # set username attribute to the value of the username parameter
        #   - self.username refers to the attribute
        #   - username refers to the parameter
        # the attribute variable will be retained by the object
        # the parameter will no longer exist after the method (init) completes
        self._username = username
        
        # same pattern as username for password, email_address and id
        self._password = password
        self._email_address = email_address
        self._id = id

    # Property getter for username attribute
    @property
    def username(self):
        return self._username

    # Property setter for username attribute
    @username.setter
    def username(self, new_username):
        self._username = new_username

    # Property getter for id attribute
    @property
    def id(self):
        return self._id

    # Property setter for id attribute
    @id.setter
    def id(self, new_id):
        self._id = new_id

    # Property getter for email_address attribute
    @property
    def email_address(self):
        return self._email_address

    # Property setter for email_address attribute
    @email_address.setter
    def email_address(self, new_email_address):
        self._email_address = new_email_address

    def __str__(self):
        return f"User:       {str(self._id).ljust(4)} {self._username.ljust(20)} {self._email_address.ljust(25)}"

    def __repr__(self):
        return f"__repr__:\nUsername: {self._username}\nEmail address: {self._email_address}\nId: {self._id}"
    

user = User("testuser", "password", "test@test.org", 1234)

print("String description of user")
print(user)
print(f"Username: {user.username}")

print("Updating username...")
user.username = "newname"
print("String description of updated user")
print(user)

# Note: I haven't added a property for the password attribute. 
# Consider if a verify_password() method would be sufficient.