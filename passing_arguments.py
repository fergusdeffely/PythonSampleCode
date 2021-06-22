def update_number(number):

    # make changes to the number
    number = number + 10

    # print the updated number
    print("In update_number:")
    print(number)


def update_list(items):

    # make changes to items (passed by reference)
    items[0] = "ONE!"
    items[1] = "not two!"

    # print the updated list
    print("In update_list:")
    print(items)


#
# main (global) code begins here
#

print("Pass by value")
print("=============")

# create a variable and assign a number to it
num = 0

# print out the current value
print("Initial number: ")
print(num)

# call function to update the number
update_number(num)

# after updating, print the current value of the number
print("After updating:")
print(num)

# Notice the updates to the number within the function update_number()
# are not retained after the function exits. This is because when integers
# are passed as arguments to functions, they are 'passed by value'. 
# This means that any changes to that variable remain local to the 
# function are are discarded once the function exits. 


print("Pass by reference")
print("=================")

# create a list
mylist = ["one", "two", "three", "four"]

# print the contents of the list
print("Initial list:")
print(mylist)

# call function to update the list
update_list(mylist)

# after updating, print the contents of the list one more time
print("After updating:")
print(mylist)

# Notice the updates to the list within the function update_list ()
# are retained by the list. This is because when lists are passed as
# arguments to functions, they are 'passed by reference'.
# This means any changes to the object that happen within the 
# function directly update the object itself. 