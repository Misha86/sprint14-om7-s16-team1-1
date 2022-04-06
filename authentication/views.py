from django.db.models import F, Exists, OuterRef
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from order.models import Order
from .forms import CustomUserForm
from .models import CustomUser
from library.utils import search_sort_paginate_books, ajax_form


def user_list(request):
    return render(request, 'user_list.html', {'title': 'Users',
                                              'users': CustomUser.objects.all()})


def user_books(request, id):
    user = get_object_or_404(CustomUser, id=id)
    books = user.get_user_books()
    if request.GET.get('violator') == str(id):
        books = user.get_user_violator_books()
    book_pages = search_sort_paginate_books(request, books, 2)
    context = {'title': f'{user.get_full_name()} Books',
               'books': book_pages}
    return render(request, 'book_list.html', context)


def users_violators(request):
    # orders = Order.objects.filter(created_at__lt=F('end_at')).select_related('user')
    # users = set()
    # for order in orders:
    #     users.add(order.user)

    users = CustomUser.objects.filter(Exists(Order.objects.filter(user=OuterRef('pk'), created_at__lt=F('end_at'))))
    return render(request, 'user_list.html', {'users': users, 'title': 'Users Violators'})


def user_form(request, id=0):
    if request.is_ajax():
        data = ajax_form(request, CustomUser, CustomUserForm, "Registration", "Update User",
                         url_name="authentication:user-list", url_arg=False, id=id)
        return JsonResponse(data)
    return redirect('/')
