from django.db.models import F, Exists, OuterRef
from django.shortcuts import render, get_object_or_404

from book.models import Book
from order.models import Order
from .models import CustomUser
from library.utils import search_sort_paginate_books


def user_list(request):
    return render(request, 'user_list.html', {'title': 'Users',
                                              'users': CustomUser.objects.all()})


def user_books(request, id):
    user = get_object_or_404(CustomUser, id=id)
    books = user.get_user_books()
    if request.GET.get('violator') == str(id):
        books = user.get_user_violator_books()
    return search_sort_paginate_books(request, books, f'{user.get_full_name()} Books', 2)


def users_violators(request):
    # orders = Order.objects.filter(created_at__lt=F('end_at')).select_related('user')
    # users = set()
    # for order in orders:
    #     users.add(order.user)

    users = CustomUser.objects.filter(Exists(Order.objects.filter(user=OuterRef('pk'), created_at__lt=F('end_at'))))
    return render(request, 'user_list.html', {'users': users, 'title': 'Users Violators'})
