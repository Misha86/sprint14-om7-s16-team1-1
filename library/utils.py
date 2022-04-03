from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def search_books(request, books):
    if request.method == 'GET' and request.GET.get('q'):
        query = request.GET.get('q')
        match = books.filter(Q(name__contains=query) | Q(authors__patronymic__contains=query)
                             | Q(authors__name__contains=query)
                             | Q(authors__surname__contains=query)).distinct()
        if match:
            request.session['q'] = query
        return match
    elif 'q' in request.session.keys():
        del request.session['q']
    return books


def sort_by(request, query):
    sort_by = request.GET.get('sort', '')
    sort_by_session = request.session.get('sort')
    if sort_by != '' and sort_by != sort_by_session:
        request.session['sort'] = sort_by
        query = query.order_by(sort_by)
    elif sort_by_session == sort_by:
        query = query.order_by(sort_by)
    elif not sort_by and sort_by_session:
        del request.session['sort']
    return query


def pagination_objects(request, objects_all, count_objects=2):
    paginator = Paginator(objects_all, count_objects)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        books = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        books = paginator.page(1)
    return books


def search_sort_paginate_books(request, books, title, count_objects):
    sorted_books = sort_by(request, search_books(request, books))
    books_pages = pagination_objects(request, sorted_books, count_objects)
    return render(request, 'book_list.html', {'books': books_pages,
                                              'title': title})
