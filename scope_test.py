from datetime import date

def do_local():
    spam = "2"
    print("do_local: " + spam)

def do_global():
    global spam
    spam = "3"
    print("do_global: " + spam)

def pass_by_value(person):
    person = person * 2
    print("pass_by_value: " + person)

def pass_by_reference(person):
    person['name'] = person['name'] * 2
    print("pass_by_reference: " + person['name'])

print()
print("Passing arguments")
print("=================\n")

print("Pass by value")
print("-------------")
person1 = "Alice"
pass_by_value(person1)
print("Program: " + person1)

print()
print("Pass by reference")
print("-----------------")
person2 = {"name": "Alice"}
pass_by_reference(person2)
print("Program: " + person2['name'])

print("\n")


def make_admin(person, count):
    print("Inside: Hello " + person['name'])
    print(f"Inside: The count is : {count}")
    print(f"Inside: The date is {person['date']}")

    person['name'] = person['name'] + " (admin)"
    count = count + 1
    person['date'] = date(person['date'].year, person['date'].month, person['date'].day + 1)

    print()
    print("Inside: ")
    print(f"Inside: {person['name']}: You are now admin")
    print(f"Inside: You have counted {count} sheep!")
    print(f"Inside: The new date is: {person['date']}")

print()
print("Make admin")
print("----------")

person = {"name": "Alice", "date": date.today()}
count = 25

make_admin(person, count)

print()
print("Outside: ")
print(f"Outside: {person['name']}")
print(f"Outside: You have counted {count} sheep!")
print(f"Outside: The date is {person['date']}")

# print()
# print("Pass by reference")
# print("-----------------")
# person2 = {"name": "Alice"}
# pass_by_reference(person2)
# print("Program: " + person2['name'])

# print("\n")


# print("Scope rules")
# print("===========\n")
# spam = "1"
# print("Program: " + spam)

# do_local()
# print("Program: " + spam)

# do_global()
# print("Program: " + spam)

