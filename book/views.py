from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from .models import Book
from library.utils import search_books, sort_by


def home_page(request):
    return TemplateResponse(request, 'base.html')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': sort_by(request, search_books(request, books)),
                                              'title': 'Books'})


def book(request, id):
    return render(request, 'book.html', {'book': get_object_or_404(Book, id=id)})


def unordered_books(request):
    books = Book.objects.filter(orders=None)
    return render(request, 'book_list.html', {'books': sort_by(request, search_books(request, books)),
                                              'title': 'Unordered books'})



