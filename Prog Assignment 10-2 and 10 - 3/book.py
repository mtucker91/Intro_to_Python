class Book:

    # FIXME 1: define and complete the __init__ method.
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year

    # FIXME 2: define and complete the Getter methods
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_isbn(self):
        return self.isbn
    def get_year(self):
        return self.year

    # FIXME 3: define and complete the Setter methods.
    def set_title(self, value):
        self.title = value
    def set_author(self, value):
        self.author = value
    def set_isbn(self, value):
        self.isbn = value
    def set_year(self, value):
        self.year = value

    # FIXME 4: define and complete the __str__ method.
    def __str__(self):
        ret_str = 'Book Title    : ' + self.title + '\n'
        ret_str += 'The Author    : ' + self.author + '\n'
        ret_str += 'Book ISBN     : ' + self.isbn + '\n'
        ret_str += 'Year Published: ' + self.year
        return ret_str