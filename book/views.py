from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from .models import Book
from library.utils import search_books, sort_by, pagination_objects


def home_page(request):
    return TemplateResponse(request, 'base.html')


def book_list(request):
    books = Book.objects.all()
    sorted_books = sort_by(request, search_books(request, books))
    books_pages = pagination_objects(request, sorted_books, 2)
    return render(request, 'book_list.html', {'books': books_pages,
                                              'title': 'Books'})


def unordered_books(request):
    books = Book.objects.filter(orders=None)
    sorted_books = sort_by(request, search_books(request, books))
    books_pages = pagination_objects(request, sorted_books, 2)
    return render(request, 'book_list.html', {'books': books_pages,
                                              'title': 'Unordered books'})


def book(request, id):
    return render(request, 'book.html', {'book': get_object_or_404(Book, id=id)})
