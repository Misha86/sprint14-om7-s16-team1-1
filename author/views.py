from django.shortcuts import render, get_object_or_404
from .models import Author


def author_books(request, id):
    author = get_object_or_404(Author, id=id)
    return render(request, 'book_list.html', {'books': author.books.all(),
                                              'title': f'{author.get_full_name()} books'})


def author_list(request):
    return render(request, 'author_list.html', {'title': 'Author',
                                                'authors': Author.get_all()})

