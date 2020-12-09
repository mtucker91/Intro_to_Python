from book import Book
# Make sure the class file in the same folder as this program

# FIXME 1: This function takes in nothing and returns nothing. It just output the menu items,
# so the user can see the options
def menu():
    print('MENU\na - Add a book\np - Print all books information\nq - Quit\nChoose an option:')
    pass

# FIXME 2: This function takes in a list. and prompt the user for a new book information (title, author, ISBN, and year)
#  then creates an object from the `Book` class.
def add_book(book_list):
    print('Adding a book')

    title = str(input('Enter the title:\n'))
    author = str(input('Enter the author:\n'))
    isbn = str(input('Enter the ISBN:\n'))
    year = str(input('Enter the year of publication:\n'))
    new_book = Book(title, author, isbn, year)
    book_list.append(new_book)

# FIXME 3: This function to print all the books in list
def print_books(book_list):
    if book_list == []:
        print('There is no books')
    else:
        for book in book_list:
            print(book.__str__())

    pass

if __name__ == "__main__":
    book_list = []
    choice = ''
    # FIXME 4-a: Print the program name.
    print('Bookstore program')
    # FIXME 4-b: make a while loop that makes the program runs as long as the menu item picked is not q
    while choice != 'q':
        # Call menu() inside the loop
        menu()
        choice = str(input(''))
        # for each choice, call the function that will perform the user choice. use if-elif-else
        if choice == 'a':
            add_book(book_list)
        elif choice == 'p':
            print_books(book_list)
        elif choice == 'q':
            pass