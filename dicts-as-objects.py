booklist = []

book = {"id": 1, "title": "Where The Wild Things Are", "author": "Maurice Sendak", "onloan": False}
booklist.append(book)
booklist.append({"id": 2, "title": "The Very Hungry Caterpillar", "author": "Eric Carle", "onloan": False})
booklist.append({"id": 3, "title": "The Giving Tree", "author": "Shel Silverstein", "onloan": False})
booklist.append({"id": 4, "title": "Green Eggs and Ham", "author": "Dr. Suess", "onloan": False})
booklist.append({"id": 5, "title": "Goodnight Moon", "author": "Margaret Wise Brown", "onloan": False})
booklist.append({"id": 6, "title": "Charlotte's Web", "author": "E.B. White", "onloan": False})

searchTerm = "Are"

for book in booklist:
    print(f"{book['title'].ljust(30)} {book['author'].ljust(20)} {str(book['onloan'])}")
    if(book['title'].find(searchTerm) != -1):
        print(f"    Contains '{searchTerm}'")

user = {"username": "testuser", "type": "libraryuser", "borrowedBooks": [2, 3]}

