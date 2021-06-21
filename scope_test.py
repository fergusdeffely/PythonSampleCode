

def do_local():
    spam = "2"
    print("do_local: " + spam)

def do_global():
    global spam
    spam = "3"
    print("do_global: " + spam)


spam = "1"
print("Program: " + spam)

do_local()
print("Program: " + spam)

do_global()
print("Program: " + spam)
