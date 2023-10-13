# Problem: Library Management System - 1.25 hr (Want to expand complexity)
# Finished on Oct 8, 2023

"""
Things to remember:

- We define attributese that are essential to an object being meaningfully defined and used. What does a class need to be initialized?
- Which operations am I going to use most frequently and how can I choose a data structure that is good at these operations?
"""

# defined to represent a single book so defining a dictionary wouldn't make sense here
class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
    
    def __str__(self):
        return f"{self.title}, {self.author}, {self.ISBN} is the book I checked out"

# designed to represent multiple books perhaps, based on ISBN number
class User:
    def __init__(self, user_name):
        self.user_name = user_name
        self.borrowed_books = {}

# designed to represent multiple books, based on ISBN number
class Library:
    def __init__(self):
        self.books_available = {}

    def add_book(self, ISBN):
        self.books_available[ISBN]
    
    # Don't use `self.isbn` because a user inputs an ISBN for removal
    def remove_book(self, ISBN):
        del self.books_available[ISBN]
    
    def lend_book(self, user, ISBN):
        # I could check in the opposite way, right? If I try to search and get a KeyError, I can let them know it's being borrowed or doesn't exist in our library
        if ISBN not in self.books_available:
            raise KeyError 
        else:
            save = self.books_available[ISBN] # save it in a temporary variable so I can use it later
            del self.books_available[ISBN] # delete the book from the available points
            user.borrowed_books[ISBN] = save # we want to update the user specific books, not the libraries books
  

    def return_book(self, user, ISBN):
        if ISBN in user.borrowed_books:
            save = user.borrowed_books[ISBN] # store the book in a variable before passing it 
            del user.borrowed_books[ISBN] # since user is already passed, no need to use self again
            self.books_available[ISBN] = save # add the book back to the library books