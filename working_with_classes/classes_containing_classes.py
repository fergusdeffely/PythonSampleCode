
# simple class definition
class A:

    def __init__(self, message):
        self.message = message

    def __repr__(self):
        rep = f"Class A:\n"
        rep = rep + f"  message = {self.message}\n"

        return rep

# second simple class definition - contains two instances of class A

class B:

    def __init__(self, message, a1, a2):
        self.message = message
        self.a1 = a1
        self.a2 = a2

    def __repr__(self):
        rep = f"Class B:\n"
        rep = rep + f"  message = {self.message}\n"
        rep = rep + f"  a1 = {self.a1}\n"
        rep = rep + f"  a2 = {self.a2}\n"

        return rep

# create first instance of class A
a1 = A("Is this the BEGINNING?")
print(a1)
print()

# create second instance of class A
a2 = A("Or maybe this is the Beginning?")
print(a2)
print()

# create instance of class B, passing both A objects as parameters
b = B("Is this the MIDDLE?", a1, a2)
print(b)
print()

# another class definition - this one contains an instance of class B

class C:

    def __init__(self, message, b):
        self.message = message
        self.b = b

    def __repr__(self):
        rep = f"Class C:\n"
        rep = rep + f"  message = {self.message}\n"
        rep = rep + f"  b = {self.b}\n"

        return rep


# create instance of class C and print description

c = C("Is this the END?", b)
print(c)
print()

