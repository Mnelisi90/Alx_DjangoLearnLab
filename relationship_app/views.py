from django.shortcuts import render
from .models import Book

def list_books(request):
    # Fetch all books with their authors
    books = Book.objects.select_related('author').all()
    
    # Create a list of strings representing each book and its author
    book_list = [f"{book.title} by {book.author.name}" for book in books]
    
    # Join the list into a single string with line breaks
    book_list_text = "\n".join(book_list)
    return render(request, 'relationship_app/list_books.html', {'books': books})
