from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.template.loader import render_to_string

from .models import Book
from .forms import BookForm
from library.utils import search_sort_paginate_books, ajax_form


def home_page(request):
    return render(request, 'base.html')


def book_list(request):
    books = search_sort_paginate_books(request, Book.objects.all(), 12)
    context = {'title': 'Books',
               'books': books}
    return render(request, 'book_list.html', context)


def book(request, id):
    return render(request, 'book.html', {'book': get_object_or_404(Book, id=id)})


def unordered_books(request):
    books = search_sort_paginate_books(request, Book.objects.filter(orders=None), 12)
    context = {'title': 'Unordered books',
               'books': books}
    return render(request, 'book_list.html', context)


def book_form(request, id=0):
    if request.is_ajax():
        data = ajax_form(request, Book, BookForm, "Add Book", "Update Book", id=id)
        return JsonResponse(data)
    return redirect('/')


def ajax_form(request, app_model, app_form, title_ad, title_up, template='book_modal_form.html', id=0):
    data = dict()
    if request.method == 'POST':
        if id == 0:
            form = app_form(request.POST)
        else:
            book = get_object_or_404(app_model, id=id)
            form = app_form(request.POST, instance=book)
        if form.is_valid():
            book_saved = form.save()
            data['form_valid'] = True
            data['redirect_path'] = reverse('book', kwargs={'id': book_saved.id})
    else:
        if id == 0:
            form = app_form()
        else:
            book = get_object_or_404(app_model, id=id)
            form = app_form(instance=book)
    title = title_ad if id == 0 else title_up
    data['form_html'] = render_to_string(template, {'form': form, "title": title}, request=request)
    return data
