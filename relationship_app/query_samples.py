import os
import django

# This should match your project directory name (django_models)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')

django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Create an author
author = Author.objects.create(name="J.K. Rowling")

# Create a book
book = Book.objects.create(title="Harry Potter", author=author)

# Create a library
library = Library.objects.create(name="Central Library")
library.books.add(book)

# Create a librarian
librarian = Librarian.objects.create(name="John Doe", library=library)

# Query all books by a specific author
author_books = Book.objects.filter(author=author)
print(f"Books by {author.name}: {list(author_books)}")

# List all books in a library
library_books = library.books.all()
print(f"Books in {library.name}: {list(library_books)}")

# Retrieve the librarian for a library
lib = Librarian.objects.get(library=library)
print(f"Librarian of {library.name}: {lib.name}")