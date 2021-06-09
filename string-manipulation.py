
def camel2Pascal(camelText):

    pascalText = camelText[0].upper() + camelText[1:]
    return pascalText

name_camel = "oneTwoThree"

print("1. Camel case = " + name_camel)
print("1. Pascal case = " + camel2Pascal(name_camel))

name_camel = "1TwoThree"

print("2. Camel case = " + name_camel)
print("2. Pascal case = " + camel2Pascal(name_camel))

name_camel = '_TwoThree'

print("3. Camel case = " + name_camel)
print("3. Pascal case = " + camel2Pascal(name_camel))

name_camel = "'TwoThree"

print("4. Camel case = " + name_camel)
print("4. Pascal case = " + camel2Pascal(name_camel))

name_camel = "\nTwoThree"

print("5. Camel case = " + name_camel)
print("5. Pascal case = " + camel2Pascal(name_camel))

name_camel = "OneTwoThree"

print("6. Camel case = " + name_camel)
print("6. Pascal case = " + camel2Pascal(name_camel))