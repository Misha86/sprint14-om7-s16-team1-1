from django.shortcuts import render, get_object_or_404
from .models import Order
from library.utils import sort_orders_by


def order_list(request):
    return render(request, 'order_list.html', {'title': 'Orders',
                                               'orders': sort_orders_by(request, Order.objects.all())})


def order_book(request, id):
    book = get_object_or_404(Order, id=id).books
    return render(request, 'book_list.html', {'title': 'Order Books',
                                              'book': book})
