from django.shortcuts import render, get_object_or_404
from .models import CustomUser
from library.utils import search_books, sort_by


def user_list(request):
    return render(request, 'user_list.html', {'title': 'Users',
                                              'users': CustomUser.objects.all()})


def user_books(request, id):
    books = get_object_or_404(CustomUser, id=id).get_user_books()
    return render(request, 'book_list.html', {'title': 'User Books',
                                              'books': sort_by(request, search_books(request, books))})
