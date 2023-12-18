class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability_status = True

    def display_details(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nAvailability: {'Available' if self.availability_status else 'Borrowed'}")


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.books_borrowed = []

    def display_details(self):
        print(f"User ID: {self.user_id}\nName: {self.name}\nBooks Borrowed: {', '.join(self.books_borrowed)}")


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
        print(f"User '{user.name}' registered.")

    def borrow_book(self, user, book):
        if book.availability_status:
            book.availability_status = False
            user.books_borrowed.append(book.title)
            self.transactions.append({'user': user.name, 'book': book.title, 'action': 'Borrowed'})
            print(f"{user.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is not available for borrowing.")

    def return_book(self, user, book):
        if book.availability_status:
            print(f"Error: '{book.title}' is already available in the library.")
        elif book.title in user.books_borrowed:
            book.availability_status = True
            user.books_borrowed.remove(book.title)
            self.transactions.append({'user': user.name, 'book': book.title, 'action': 'Returned'})
            print(f"{user.name} returned '{book.title}'.")
        else:
            print(f"Error: '{user.name}' did not borrow '{book.title}'.")

    def generate_transaction_report(self):
        print("\nTransaction Report:")
        for transaction in self.transactions:
            print(f"{transaction['user']} {transaction['action']} '{transaction['book']}'")

    def display_books(self):
        print("\nBook Details:")
        for book in self.books:
            book.display_details()

    def display_users(self):
        print("\nUser Details:")
        for user in self.users:
            user.display_details()

    def display_menu(self):
        print("\nMenu:")
        print("1. Add Book")
        print("2. Register User")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display Books")
        print("6. Display Users")
        print("7. Generate Transaction Report")
        print("8. Exit")

    def run_menu(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-8): ")

            if choice == "1":
                title = input("Enter book title: ")
                author = input("Enter author name: ")
                isbn = input("Enter ISBN: ")
                new_book = Book(title, author, isbn)
                self.add_book(new_book)

            elif choice == "2":
                user_id = input("Enter user ID: ")
                name = input("Enter user name: ")
                new_user = User(user_id, name)
                self.register_user(new_user)

            elif choice == "3":
                user_id = input("Enter user ID: ")
                book_title = input("Enter book title: ")
                user = next((u for u in self.users if str(u.user_id) == user_id), None)
                book = next((b for b in self.books if b.title == book_title), None)

                if user and book:
                    self.borrow_book(user, book)
                else:
                    print("User or book not found.")

            elif choice == "4":
                user_id = input("Enter user ID: ")
                book_title = input("Enter book title: ")
                user = next((u for u in self.users if str(u.user_id) == user_id), None)
                book = next((b for b in self.books if b.title == book_title), None)

                if user and book:
                    self.return_book(user, book)
                else:
                    print("User or book not found.")

            elif choice == "5":
                self.display_books()

            elif choice == "6":
                self.display_users()

            elif choice == "7":
                self.generate_transaction_report()

            elif choice == "8":
                print("Exiting the Library Management System. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 8.")


def main():
    library = Library()
    library.run_menu()


main()
