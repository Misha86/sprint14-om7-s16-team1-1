from django.shortcuts import render, get_object_or_404
from library.utils import search_books
from .models import Author


def author_books(request, id):
    author = get_object_or_404(Author, id=id)
    books = search_books(request, author.books.all())
    return render(request, 'book_list.html', {'books': books,
                                              'title': f'{author.get_full_name()} books'})


def author_list(request):
    return render(request, 'author_list.html', {'title': 'Authors',
                                                'authors': Author.get_all()})

