class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False


class Library :
    def __init__(self):
        self._book = []
    def add_book(self,book):
        if  isinstance(book,Book):
            self._book.append(book)
        else:
            raise TypeError("Only Book objects can added to the library")
    def check_out_book(self,title):
        for book in self._book:
            if book.title == title and not book.is_checked_out:
                book.is_checked_out = True
                return True
            else :
                return False
    def return_book(self, title):
        for book in self._book:
            if book.title == title and book.is_checked_out:
                book.is_checked_out = False
                return True
            else: return False
    def list_available_books(self):
        return [book for book in self._book if not book._is_checked_out]
    
            
            