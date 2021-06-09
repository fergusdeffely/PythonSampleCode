# Open a file
print("Opening foo.txt for writing...")

fo = open("foo.txt", "w")
fo.write( "1. write:\nHere is some text.\nAnd here is some more text!!\n\n")
fo.writelines(["2. writelines\n", "Here is some text\n", "And here is some more text!!!\n"])
fo.close()

print("Opening foo.txt for reading...")
fo = open("foo.txt", "r")
# store the file contents as a list of strings
lines = fo.readlines()
fo.close()

print("File contents:")
for line in lines:
    print(line, end='')
