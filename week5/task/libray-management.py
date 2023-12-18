class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability_status = True

    def display_details(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nAvailability: {'Available' if self.availability_status else 'Not Available'}\n")


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.books_borrowed = []

    def display_details(self):
        print(f"User ID: {self.user_id}\nName: {self.name}\nBooks Borrowed: {', '.join(self.books_borrowed)}\n")

    def borrow_book(self, book):
        if book.availability_status:
            self.books_borrowed.append(book.title)
            book.availability_status = False
            print(f"{self.name} has successfully borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is not available for borrowing.")

    def return_book(self, book):
        if book.title in self.books_borrowed:
            self.books_borrowed.remove(book.title)
            book.availability_status = True
            print(f"{self.name} has successfully returned '{book.title}'.")
        else:
            print(f"You haven't borrowed '{book.title}'. Cannot return.")

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.transactions = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def register_user(self, user):
        self.users.append(user)
        print(f"User '{user.name}' registered in the library.")

    def borrow_book(self, user, book):
        transaction = Transaction(user, book, "Borrowed")
        self.transactions.append(transaction)
        user.borrow_book(book)

    def return_book(self, user, book):
        transaction = Transaction(user, book, "Returned")
        self.transactions.append(transaction)
        user.return_book(book)

    def display_books(self):
        print("Library Books:")
        for book in self.books:
            book.display_details()

    def display_users(self):
        print("Library Users:")
        for user in self.users:
            user.display_details()


class Transaction:
    def __init__(self, user, book, transaction_type):
        self.user = user
        self.book = book
        self.transaction_type = transaction_type

