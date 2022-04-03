from django.shortcuts import render, get_object_or_404
from .models import Book
from library.utils import search_sort_paginate_books


def home_page(request):
    return render(request, 'base.html')


def book_list(request):
    books = Book.objects.all()
    return search_sort_paginate_books(request, books, 'Books', 12)


def book(request, id):
    return render(request, 'book.html', {'book': get_object_or_404(Book, id=id)})


def unordered_books(request):
    books = Book.objects.filter(orders=None)
    return search_sort_paginate_books(request, books, 'Unordered books', 12)


def book(request, id):
    return render(request, 'book.html', {'book': get_object_or_404(Book, id=id)})
