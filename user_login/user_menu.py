from menu import Menu

class UserMenu(Menu):
    
    # show method provides the logic for displaying the menu options, 
    # getting the user's selection and verifying that selections are valid

    def show(self, user):
        selection = "0"

        while(selection != "5"):
            self.clearscreen()
            selection = self.get_selection(user)

            if(selection not in ["1", "2", "3", "4", "5"]):
                self.clearscreen()
                print(f"Invalid menu option [{selection}]. Press return to try again.")
                input()

    # print the menu and retrieve the users selection and taking the appropriate 
    # action if the selection is one of the supported options

    def get_selection(self, user):
        print(f"Welcome {user.username}!")
        print(f"Email address: {user.email_address}\n")
        print("Menu options:")
        print("1. Update Email Address")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Option 4")        
        print("5. Exit\n")

        selection = input("Please choose an option (1-5): ")

        if(selection == "1"):
            self.clearscreen()
            print("Update email address")
            print("====================\n")        
            print(f"Current email address = {user.email_address}")
            
            new_email = input("New email address: ")
            user.update_email_address(new_email)

        elif(selection == "2"):
            print("User option 2\n")
            input("Return to continue...")
        elif(selection == "3"):
            print("User option 3\n")
            input("Return to continue...")
        elif(selection == "4"):
            print("User option 4\n")
            input("Return to continue...")

        return selection
