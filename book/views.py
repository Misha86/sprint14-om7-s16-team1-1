from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from django.db.models import Q
from .models import Book


def home_page(request):
    return TemplateResponse(request, 'base.html')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books_filter(request, books),
                                              'title': 'Books'})


def book(request, id):
    return render(request, 'book.html', {'book': get_object_or_404(Book, id=id)})


def unordered_books(request):
    books = Book.objects.filter(orders=None)
    return render(request, 'book_list.html', {'books': books_filter(request, books),
                                              'title': 'Unordered books'})


def books_filter(request, books):
    if request.method == 'GET' and request.GET.get('q'):
        query = request.GET.get('q')
        return books.filter(Q(name__contains=query) | Q(authors__patronymic=query) | Q(authors__name=query)
                            | Q(authors__surname=query)).distinct()
    else:
        return books
