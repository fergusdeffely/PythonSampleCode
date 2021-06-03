index = int(input("Enter the index: "))

mylist = [1, 2, 3, 4]
try:
    print(mylist[index])
except IndexError as e:
    print(f"{e}")
    print("Your index is out of range - try again.")
