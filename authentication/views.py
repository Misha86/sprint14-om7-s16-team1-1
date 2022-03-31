from django.shortcuts import render, get_object_or_404
from .models import CustomUser
from order.models import Order


def user_list(request):
    return render(request, 'user_list.html', {'title': 'Users',
                                              'users': CustomUser.objects.all()})


def user_books(request, id):
    user = get_object_or_404(CustomUser, id=id)
    orders = Order.objects.filter(user=user).select_related('book')
    books = [order.book for order in orders]
    return render(request, 'book_list.html', {'title': 'User Books',
                                              'books': books})
