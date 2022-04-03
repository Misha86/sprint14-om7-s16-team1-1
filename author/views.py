from django.shortcuts import render, get_object_or_404
from library.utils import search_sort_paginate_books, pagination_objects, sort_by
from .models import Author


def author_books(request, id):
    author = get_object_or_404(Author, id=id)
    return search_sort_paginate_books(request, author.books.all(), f'{author.get_full_name()} books', 8)


def author_list(request):
    return render(request, 'author_list.html', {'title': 'Authors',
                                                'authors': Author.get_all()})

