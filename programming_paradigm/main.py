import sys
from library_management import Library, Book
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)
    
    #Setup a small library
    library = Library()
    library.add_book(Book("Brave New World","Aldous Huxley"))
    library.add_book(Book("1984","George Orwell"))
    
    #Initial list of available books
    print("Available books after setup:")
    library.library_list()
    
    #Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.library_list()
    
    #Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.library_list()
    
    

if __name__ == "__main__":
    main()