from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from library.utils import search_sort_paginate_books, ajax_form
from .forms import AuthorForm
from .models import Author


def author_books(request, id):
    author = get_object_or_404(Author, id=id)
    books = search_sort_paginate_books(request, author.books.all(), 8)
    context = {'title': f'{author.get_full_name()} books',
               'books': books}
    return render(request, 'book_list.html', context)


def author_list(request):
    return render(request, 'author_list.html', {'title': 'Authors',
                                                'authors': Author.get_all()})


def author_form(request, id=0):
    if request.is_ajax():
        data = ajax_form(request, Author, AuthorForm, "Add Author", "Update Author",
                         url_name="author:author-list", url_arg=False, id=id)
        return JsonResponse(data)
    return redirect('/')

