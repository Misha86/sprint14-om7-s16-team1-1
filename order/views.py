from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import OrderForm
from .models import Order
from library.utils import sort_by, ajax_form


def order_list(request):
    return render(request, 'order_list.html', {'title': 'Orders',
                                               'orders': sort_by(request, Order.objects.all())})


def order_book(request, id):
    book = get_object_or_404(Order, id=id).books
    return render(request, 'book_list.html', {'title': 'Order Books', 'book': book})


def order_form(request, id=0):
    if request.is_ajax():
        data = ajax_form(request, Order, OrderForm, "Add Order", "Update Order",
                         url_name="order:order-list", url_arg=False, id=id)
        return JsonResponse(data)
    return redirect('/')
