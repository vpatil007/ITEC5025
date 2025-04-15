# This program simulates a basic library system to demonstrate the fundamentals of Python programming.
# It includes examples of functions, classes, error handling, and program flow organization.

# Function to display a welcome message
def display_welcome_message():
    """
    Function to display a welcome message for the library system.
    This function is called at the start of the program to greet the user.
    """
    print("Hello World!")
    print("Welcome to the Library System!")

# Function to search for books
def search_books(library, keyword):
    """
    Function to search for books in the library based on a keyword.
    This function performs a case-insensitive search for books that contain the keyword.

    Args:
    - library (list): A list of book titles available in the library.
    - keyword (str): The keyword to search for in the book titles.

    Returns:
    - list: A list of book titles that match the keyword.
    """
    matching_books = [book for book in library if keyword.lower() in book.lower()]
    return matching_books

# Class to demonstrate object-oriented programming
class Library:
    """
    A Library class that represents a collection of books.
    This class provides methods to add books to the collection and display the current collection.

    Attributes:
    - books (list): A list to store the titles of books in the library.
    """
    def __init__(self):
        """
        Constructor method to initialize the Library object.
        Initializes an empty list to store book titles.
        """
        self.books = []

    def add_book(self, book_title):
        """
        Method to add a book to the library's collection.

        Args:
        - book_title (str): The title of the book to be added.

        Returns:
        - None
        """
        self.books.append(book_title)
        print(f'Book "{book_title}" has been added to the library.')

    def display_books(self):
        """
        Method to display the current collection of books in the library.
        If the library is empty, it notifies the user.

        Returns:
        - None
        """
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("The library is empty!")

# Function to demonstrate error handling
def error_handling_demo(library):
    """
    Function to demonstrate error handling in the program.
    Prompts the user to enter a keyword to search for books and handles invalid input gracefully.

    Args:
    - library (list): A list of book titles available in the library.

    Returns:
    - None
    """
    try:
        # Prompt the user to enter a keyword for searching books
        keyword = input("Enter a keyword to search for books: ")
        
        # Perform the search using the search_books function
        results = search_books(library, keyword)
        
        # Display the search results
        if results:
            print("Matching books:")
            for book in results:
                print(f"- {book}")
        else:
            print("No books matched your search!")
    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"An error occurred: {e}")

# Main function to organize the program flow
def main():
    """
    Main function to organize the program flow.
    This function serves as the entry point for the program and coordinates the execution of various components.
    """
    # Display a welcome message to the user
    display_welcome_message()
    
    # Create a Library object to manage the collection of books
    library = Library()
    
    # Add some predefined books to the library
    library.add_book("Python Programming 101")
    library.add_book("Introduction to Machine Learning")
    library.add_book("Data Science Essentials")
    library.add_book("Python Object Oriented Programing")
    library.add_book("Python Data Structures")
    
    # Display the current collection of books in the library
    print("\nDisplaying library books:")
    library.display_books()
    
    # Demonstrate error handling by allowing the user to search for books
    print("\nDemonstrating error handling:")
    error_handling_demo(library.books)

# Ensuring the program runs only when executed directly
if __name__ == "__main__":
    """
    This block ensures that the program runs only when executed directly.
    If the script is imported as a module, the main() function will not be executed.
    """
    main()