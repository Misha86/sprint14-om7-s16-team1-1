from django.contrib import auth
from django.db.models import F, Exists, OuterRef
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse

from order.models import Order
from .forms import CustomUserForm, CustomUserLoginForm
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
        data = dict()
        if request.method == 'POST':
            if id == 0:
                form = CustomUserForm(request.POST)
            else:
                obj = get_object_or_404(CustomUser, id=id)
                form = CustomUserForm(request.POST, instance=obj)
            if form.is_valid():
                password = form.cleaned_data['password2']
                user = form.save()
                new_user = auth.authenticate(username=user.email, password=password)
                auth.login(request, new_user)
                data['form_valid'] = True
                data['redirect_path'] = reverse('home-page')
        else:
            if id == 0:
                form = CustomUserForm()
            else:
                book = get_object_or_404(CustomUser, id=id)
                form = CustomUserForm(instance=book)
        title = "Registration" if id == 0 else "Update User"
        data['form_html'] = render_to_string('modal_form.html', {'form': form, "title": title}, request=request)
        return JsonResponse(data)
    return redirect('/')


def user_login(request):

    if request.is_ajax():
        data = dict()
        if request.method == 'POST':
            form = CustomUserLoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']

                user = auth.authenticate(username=email, password=password)

                if user is not None and user.is_active:
                    auth.login(request, user)
                    data['form_valid'] = True
                    data['redirect_path'] = reverse('home-page')
        else:
            form = CustomUserLoginForm()
        title = "Login"
        data['form_html'] = render_to_string('modal_form.html', {'form': form, "title": title}, request=request)

        return JsonResponse(data)

    return redirect('/')


def user_logout(request):
    auth.logout(request)
    return redirect('/')
