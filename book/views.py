from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from .models import Book


def home_page(request):
    return TemplateResponse(request, 'base.html')


def book_list(request):
    return render(request, 'book_list.html', {'books': Book.get_all(),
                                              'title': 'Books'})


def book(request, id):
    return render(request, 'book.html', {'book': get_object_or_404(Book, id=id)})


def unordered_books(request):
    books = Book.objects.filter(orders=None)
    return render(request, 'book_list.html', {'books': books,
                                              'title': 'Unordered books'})


