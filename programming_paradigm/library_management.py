class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Only Book objects can be added to the library")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False

    def list_available_books(self):
        return [book for book in self._books if not book._is_checked_out]
    
            
            