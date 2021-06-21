import os

def clearScreen():
    os.system('cls')

def showMenu(inputError = False):
    clearScreen()
    print("Menu options:")
    print("1. Option one")
    print("2. Option two")
    print("3. Option three")
    print("4. Option four")
    print("5. Exit\n")
    
    if inputError:
        print("*** Please enter a digit between 1 and 5 ***")
    else:
        print("")

    return input("Please choose an option (1-5): ")

inputError = False
selection = "0"

while(selection != "5"):
    
    selection = showMenu(inputError)
    inputError = False

    clearScreen()
    
    if(selection == "1"):
        print("You selected Option one!\n")
        input("Return to continue...")
    elif(selection == "2"):
        print("You selected Option two!\n")
        input("Return to continue...")
    elif(selection == "3"):
        print("You selected Option three!\n")
        input("Return to continue...")
    elif(selection == "4"):
        print("You selected Option four!\n")
        input("Return to continue...")
    elif(selection != "5"):
        inputError = True    

print("Bye!")