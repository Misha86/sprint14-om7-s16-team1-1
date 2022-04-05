from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import BookForm
from library.utils import search_sort_paginate_books, search_sort_paginate_books1


def home_page(request):
    return render(request, 'base.html')


def book_list(request):
    books = search_sort_paginate_books(request, Book.objects.all(), 12)
    form = BookForm()
    context = {'title': 'Books',
               'books': books,
               'form': form}
    return render(request, 'book_list.html', context)


def book(request, id):
    return render(request, 'book.html', {'book': get_object_or_404(Book, id=id)})


def unordered_books(request):
    books = Book.objects.filter(orders=None)
    return search_sort_paginate_books1(request, books, 'Unordered books', 12)


def book_form(request, id=0):
    print('hello')
    return render(request, 'book.html', {'book': get_object_or_404(Book, id=id)})
