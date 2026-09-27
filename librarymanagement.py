class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.isAvailable = True

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)

        if self.isAvailable:
            print("Status: Available")
        else:
            print("Status: Borrowed")

    def borrowBook(self):
        if self.isAvailable:
            self.isAvailable = False
            print(self.title, "borrowed successfully")
        else:
            print(self.title, "is already borrowed")

    def returnBook(self):
        if not self.isAvailable:
            self.isAvailable = True
            print(self.title, "returned successfully")
        else:
            print(self.title, "was not borrowed")


def searchBook(books, title):

    for book in books:
        if book.title.lower() == title.lower():
            return book

    return None


def startprogram():

    book1 = Book("Python Programming", "James")
    book2 = Book("Java Programming", "Robert")
    book3 = Book("Data Structures", "Mark")

    books = [book1, book2, book3]

    print("---- ALL BOOKS ----")

    for book in books:
        book.display()
        print()

    print("---- BORROW BOOK ----")

    book = searchBook(books, "Python Programming")

    if book is not None:
        book.borrowBook()

    print()

    print("---- AFTER BORROWING ----")

    for book in books:
        book.display()
        print()

    print("---- RETURN BOOK ----")

    book = searchBook(books, "Python Programming")

    if book is not None:
        book.returnBook()


startprogram()