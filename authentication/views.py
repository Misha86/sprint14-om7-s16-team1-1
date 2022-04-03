from django.db.models import F, Exists, OuterRef
from django.shortcuts import render, get_object_or_404

from order.models import Order
from .models import CustomUser
from library.utils import search_books, sort_by, pagination_objects


def user_list(request):
    return render(request, 'user_list.html', {'title': 'Users',
                                              'users': CustomUser.objects.all()})


def user_books(request, id):
    user = get_object_or_404(CustomUser, id=id)
    sorted_books = sort_by(request, search_books(request, user.get_user_books()))
    books_pages = pagination_objects(request, sorted_books, 2)
    return render(request, 'book_list.html', {'title': f'{user.get_full_name()} Books',
                                              'books': books_pages})


def users_violators(request):
    # orders = Order.objects.filter(created_at__lt=F('end_at')).select_related('user')
    # users = set()
    # for order in orders:
    #     users.add(order.user)

    users = CustomUser.objects.filter(Exists(Order.objects.filter(user=OuterRef('pk'), created_at__lt=F('end_at'))))
    return render(request, 'user_list.html', {'users': users,
                                              'title': 'Users Violators'})
