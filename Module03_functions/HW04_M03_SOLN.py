### CS 22B Module 03 - Homework 4
### Name: <Your Name>

##### Homework to practice writing Functional Code #####

#### Library Management System:
### In this homework we will use a list of dictionaries, where each dictionary has 2 fields {"name": book_name, "author": author}
# Your task is to:
# A. A function add_book(library, book_name, author) that adds a book (represented by a dictionary with name and author) to a list (the library).
# B. A function remove_book(library, book_name) that removes a book from the library by its name.

library = [{"name": "Of Mice and Men", "author": "John Steinbeck"},
           {"name": "To Kill a Mockingbird", "author": "Harper Lee"},
           {"name": "1984", "author": "George Orwell"}, 
           {"name": "Animal Farm", "author": "George Orwell"}
           ]    

### Part A. A function add_book(library, book_name, author) that adds a book (represented by a dictionary with name and author) to a list (the library).
def add_book(library, book_name, author):
    # Create a new book dictionary
    new_book = {"name": book_name, "author": author}
    # Add the new book to the library
    library.append(new_book)
    
add_book(library, "The Hunger Games", "Suzanne Collins")

### Part B. A function remove_book(library, book_name) that removes a book from the library by its name.
def remove_book(library, book_name):
    # Find the book to remove
    for book in library:
        if book["name"] == book_name:
            # Remove the book from the library
            library.remove(book)
            break  # Exit the loop after removing the book

remove_book(library, "Of Mice and Men")       
    
### Part C: Write a lambda function filter_books_by_author(library, author) that filters
## and returns all books written by a given author from the library.
books_by_aurthor = lambda library, author: [book for book in library if book["author"]== author]
# print(books_by_aurthor(library, "George Orwell"))


### Part D: Create a generator function book_generator(library) that yields books one by one from the library.
def book_generator(library):
    for book in library:
        yield book

book_gen = book_generator(library)
for book in book_gen:
    print(book)

    
### Part E: Write a decorator log_operation(func) that logs/prints the operation (i.e., function name) whenever a book is added or removed.

##### Other functions you can write to practice functional programming:
# A function list_books(library) that lists all books in the library.
list_books = []
for book in library:
    list_books.append(book["name"])
# print(list_books)

## Rewrite as a lambda function
list_books_lambda = lambda library: [book["name"] for book in library]
# print(list_books_lambda(library))

# Write a lambda function filter_books_by_author(library, author) that filters and returns all books written by a given author from the library.
# Write a decorator log_operation(func) that logs/prints the operation (i.e., function name) whenever a book is added or removed.
# Create a generator function book_generator(library) that yields books one by one from the library.
# Organize the package as follows:
# library.py contains the functions add_book(), remove_book(), and list_books().
# utils.py contains filter_books_by_author(), log_operation(), and book_generator().
# The main file is given, build your code such that the main file executes without any error and as expected. **You will need to add some lines to the main file for it to work correctly. Hints are provided in form of comments. **