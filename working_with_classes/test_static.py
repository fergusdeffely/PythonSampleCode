# static, or class-level variables exist at the class level

class StaticTest:

    # static variable
    number = "zero"

    def get_number_class(self):
        return StaticTest.number

    def get_number_instance(self):
        return self.number


a = StaticTest()
b = StaticTest()
c = StaticTest()

print("Test 1:")
print()
print(f"a: number = {a.number}")
print(f"b: number = {b.number}")
print(f"c: number = {c.number}")

# updating a class-level variable changes that value for all instances
print()
print("Test 2:")
print()
StaticTest.number = "one"

d = StaticTest()

print(f"a: number = {a.number}")
print(f"b: number = {b.number}")
print(f"c: number = {c.number}")
print(f"d: number = {d.number}")

# An individual instance or object can 'break away' from a class-level variable by assigning
# its own particular value (essentially changing the class-level variable to a 
# dynamic variable for that particular instance)

print()
print("Test 3:")
print()
a.number = "two"

print(f"a: number = {a.number}")
print(f"b: number = {b.number}")
print(f"c: number = {c.number}")
print(f"d: number = {d.number}")

# two ways of getting an objects current value of a member variable
# first is class level

print()
print("Test 4:")
print()
StaticTest.number = "three"

print("get_number_class:")
print(f"a: {a.get_number_class()}")
print(f"b: {b.get_number_class()}")
print(f"c: {c.get_number_class()}")
print(f"d: {d.get_number_class()}")

# second is instance level
print()
print("get_number_instance")
print(f"a: {a.get_number_instance()}")
print(f"b: {b.get_number_instance()}")
print(f"c: {c.get_number_instance()}")
print(f"d: {d.get_number_instance()}")
