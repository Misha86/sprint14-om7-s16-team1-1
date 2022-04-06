from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.template.loader import render_to_string

from .models import Book
from .forms import BookForm
from library.utils import search_sort_paginate_books, search_sort_paginate_books1


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
        data = dict()
        if request.method == 'POST':
            if id == 0:
                form = BookForm(request.POST)
            else:
                book = get_object_or_404(Book, id=id)
                form = BookForm(request.POST, instance=book)
            if form.is_valid():
                book_saved = form.save()
                data['form_valid'] = True
                data['redirect_path'] = reverse('book', kwargs={'id': book_saved.id})
        else:
            if id == 0:
                form = BookForm()
            else:
                book = get_object_or_404(Book, id=id)
                form = BookForm(instance=book)
        title = "Add Book" if id == 0 else "Update Book"
        data['form_html'] = render_to_string('book_modal_form.html', {'form': form, "title": title}, request=request)
        return JsonResponse(data)
    return redirect('/')


# def book_form(request, id=0):
#     context = {}
#     if request.method == "GET":
#         if id == 0:
#             form = BookForm()
#         else:
#             book = get_object_or_404(Book, id=id)
#             form = BookForm(instance=book)
#     else:
#         if id == 0:
#             form = BookForm(request.POST)
#         else:
#             book = get_object_or_404(Book, id=id)
#             form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             book_saved = form.save()
#             return redirect('book', book_saved.id)
#         context['restart_form'] = "True"
#     context['form'] = form
#     return render(request, 'book_list.html', context)
