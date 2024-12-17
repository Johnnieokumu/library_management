# Book class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  # Book is available by default

    def borrow(self):
        if self.available:
            self.available = False
            print(f"The book '{self.title}' has been borrowed.")
        else:
            print(f"The book '{self.title}' is already borrowed.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' was not borrowed.")

# Member class
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # List to track borrowed books

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"Sorry, '{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"You have not borrowed '{book.title}'.")

# Library class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' registered.")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"Title: {book.title}, Author: {book.author}, Status: {status}")

    def borrow_book(self, member, book):
        if book in self.books:
            member.borrow_book(book)
        else:
            print(f"The book '{book.title}' is not in the library.")

    def return_book(self, member, book):
        if book in self.books:
            member.return_book(book)
        else:
            print(f"The book '{book.title}' does not belong to this library.")

# Example usage
library = Library()

# Adding books
book1 = Book("1984", "George Orwell", "12345")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "67890")
library.add_book(book1)
library.add_book(book2)

# Adding members
member1 = Member("Alice", "M001")
library.add_member(member1)

# Display books
library.display_books()

# Borrow and return books
library.borrow_book(member1, book1)
library.display_books()

library.return_book(member1, book1)
library.display_books()
