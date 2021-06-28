# dynamic member variables are the variety of member variables 
# we've been using up to now. Each instance, or object of a 
# particular class has it's own specific value.

class DynamicTest:

    def __init__(self, number="zero"):
        self.number = number


a = DynamicTest()
b = DynamicTest()
c = DynamicTest()

print("Test 1:")
print()
print(f"a: number = {a.number}")
print(f"b: number = {b.number}")
print(f"c: number = {c.number}")

# updating one instance only updates that instance
print()
print("Test 2:")
print()
a.number = "one"

print(f"a: number = {a.number}")
print(f"b: number = {b.number}")
print(f"c: number = {c.number}")
