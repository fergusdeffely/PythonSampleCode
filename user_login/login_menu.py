from menu import Menu

class LoginMenu(Menu):

    def show(self):
        selection = "0"

        while(selection != "3"):
            self.clearscreen()
            selection = self.get_selection()

            # handle the case of invalid menu option selected
            if(selection not in ["1", "2", "3"]):
                self.clearscreen()
                print(f"Invalid menu option [{selection}]. Press return to try again.")
                input()


    def get_selection(self):
        print("Menu options:")
        print("1. Login")
        print("2. Register")
        print("3. Exit\n")

        selection = input("Please choose an option (1-3): ")

        if(selection == "1"):
            self.login()
        elif(selection == "2"):
            self.register_user()

        return selection

    def login(self):
        print("login")
        phone_number = input("Please enter your phone number: ")
        self.validate_phone_number(phone_number)
        self.check_phone_number(phone_number)
        input("Return to continue:")

    def register_user(self):
        print("register user")

    def validate_phone_number(self, phone_number):
        print(f"validate phone number: {phone_number}")

    def check_phone_number(self, phone_number):
        print(f"check phone number: {phone_number}")
