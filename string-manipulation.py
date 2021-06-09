
def camel2Pascal(camelText):

    pascalText = camelText[0].upper() + camelText[1:]
    return pascalText

def test_camel2Pascal(test_number, inputText, expectedOutput):
    print(f"{test_number}. Input = {inputText}")
    print(f"{test_number}. Expected Output = {expectedOutput}")
    actualOutput = camel2Pascal(inputText)
    print(f"{test_number}. Actual Output = {actualOutput}")

    if actualOutput == expectedOutput:
        print("Output correct")
        return True
    else:
        print("OUTPUT INCORRECT")
        return False
   
test_camel2Pascal(1, "oneTwoThree", "OneTwoThree")
test_camel2Pascal(2, "1TwoThree", "1TwoThree")
test_camel2Pascal(3, "_TwoThree", "_TwoThree")
test_camel2Pascal(4, "'TwoThree", "'TwoThree")
test_camel2Pascal(5, "\nTwoThree", "\nTwoThree")
test_camel2Pascal(6, "OneTwoThree", "OneTwoThree")