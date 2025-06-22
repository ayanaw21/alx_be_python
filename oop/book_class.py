# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor method to initialize Book instance"""
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """Destructor method called when instance is deleted"""
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """String representation of the Book instance"""
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Official string representation that can recreate the instance"""
        return f"Book('{self.title}', '{self.author}', {self.year})"