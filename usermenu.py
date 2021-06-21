import os

def clearscreen():
    os.system('cls')


def do_user_menu(user):

    selection = "0"

    while(selection != "5"):
        clearscreen()
        selection = show_user_menu(user)

        if(selection not in ["1", "2", "3", "4", "5"]):
            clearscreen()
            print(f"Invalid menu option [{selection}]. Press return to try again.")
            input()


def show_user_menu(user):

    print(f"Welcome {user['username']}!")
    print(f"High score = {user['highscore']}, Admin = {str(user['admin'])}\n")
    print("Menu options:")
    print("1. Update High Score")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")        
    print("5. Exit\n")

    selection = input("Please choose an option (1-5): ")

    if(selection == "1"):
        clearscreen()
        print("Update high-score")
        print("=================\n")        
        print(f"Current high-score = {user['highscore']}")
        user['highscore'] = int(input("New high-score: "))
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

def login(userdata):
    print("User login\n")
    username = input("Username: ")
    password = input("Password: ")

    logged_in_user = None

    for user in userdata:
        if(user["username"] == username):
            if(user["password"] == password):
                logged_in_user = user
                break

    if(logged_in_user is not None):
        # user's credentials are valid, so show user menu
        # user will stay in this menu until they logout
        do_user_menu(logged_in_user)
    else:
        print("Invalid username or password. Press return to continue...")
        input()

def register(userdata):
    print("Register\n")
    username = input("Username: ")
    password = input("Password: ")        
    input("Return to continue...")        

def show_login_menu(userdata):

    print("Menu options:")
    print("1. Login")
    print("2. Register")
    print("3. Exit\n")

    selection = input("Please choose an option (1-3): ")

    if(selection == "1"):
        login(userdata)
    elif(selection == "2"):
        register(userdata)

    return selection

def do_login_menu(userdata):

    selection = "0"

    while(selection != "3"):
        clearscreen()
        selection = show_login_menu(userdata)

        # handle the case of invalid menu option selected
        if(selection not in ["1", "2", "3"]):
            clearscreen()
            print(f"Invalid menu option [{selection}]. Press return to try again.")
            input()

    print("Thank you and goodbye")