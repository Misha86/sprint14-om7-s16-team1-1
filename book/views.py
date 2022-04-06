from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.template.loader import render_to_string

from .models import Book
from .forms import BookForm
from library.utils import search_sort_paginate_books, ajax_form


def home_page(request):
    return render(request, 'base.html')


def book_list(request):
    books = search_sort_paginate_books(request, Book.objects.all(), 12)
    context = {'title': 'Books',
               'books': books}
    return render(request, 'book_list.html', context)


def book(request, id):
    return render(request, 'book.html', {'book': get_object_or_404(Book, id=id)})


def unordered_books(request):
    books = search_sort_paginate_books(request, Book.objects.filter(orders=None), 12)
    context = {'title': 'Unordered books',
               'books': books}
    return render(request, 'book_list.html', context)


def book_form(request, id=0):
    if request.is_ajax():
        data = ajax_form(request, Book, BookForm, "Add Book", "Update Book", id=id)
        return JsonResponse(data)
    return redirect('/')

