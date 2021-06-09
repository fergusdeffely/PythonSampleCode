
def camel2Pascal(camelText):

    pascalText = camelText[0].upper() + camelText[1:]
    return pascalText

def test_camel2Pascal(test_number, inputText):
    print(f"{test_number}. Camel case = {inputText}")
    print(f"{test_number}. Pascal case = {camel2Pascal(inputText)}")
   
test_camel2Pascal(1, "oneTwoThree")
test_camel2Pascal(2, "1TwoThree")
test_camel2Pascal(3, "_TwoThree")
test_camel2Pascal(4, "'TwoThree")
test_camel2Pascal(5, "\nTwoThree")
test_camel2Pascal(6, "OneTwoThree")