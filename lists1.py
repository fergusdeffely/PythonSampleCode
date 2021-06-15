numberList = [1, 2, 3, 4, 5]

# print list
print ("Printing list...")
print (f"number of items = {len(numberList)}: {numberList}")

# print contents of list one item at a time
print ("Printing items...")
for number in numberList:
    print(number)

# print an item by index 
print("Printing 3rd item...")
print(numberList[2])

# add an item to the list
numberList.append(6)
print("Add item...")
print(numberList)

# add another list
print("Add list...")
numberList.extend([7, 8, 9])
print(numberList)

# insert an item
print("Insert item...")
numberList.insert(0, 10)
print(numberList)

# pop items from the list
print("Pop last item...")
print(numberList.pop())
print(numberList)

print("Pop third item...")
print(numberList.pop(2))
print(numberList)
