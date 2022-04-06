from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.loader import render_to_string
from django.urls import reverse


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


def search_sort_paginate_books1(request, books, title, count_objects, html='book_list.html'):
    sorted_books = sort_by(request, search_books(request, books))
    books_pages = pagination_objects(request, sorted_books, count_objects)
    return render(request, html, {'books': books_pages, 'title': title})


def search_sort_paginate_books(request, books, count_objects):
    sorted_books = sort_by(request, search_books(request, books))
    books_pages = pagination_objects(request, sorted_books, count_objects)
    return books_pages


def ajax_form(request, app_model, app_form, title_ad, title_up,
              template='modal_form.html', url_name='book', url_arg=True, id=0):
    data = dict()
    if request.method == 'POST':
        if id == 0:
            form = app_form(request.POST)
        else:
            obj = get_object_or_404(app_model, id=id)
            form = app_form(request.POST, instance=obj)
        if form.is_valid():
            obj_saved = form.save()
            kwargs = {'id': obj_saved.id} if url_arg else None
            data['form_valid'] = True
            data['redirect_path'] = reverse(url_name, kwargs=kwargs)
    else:
        if id == 0:
            form = app_form()
        else:
            book = get_object_or_404(app_model, id=id)
            form = app_form(instance=book)
    title = title_ad if id == 0 else title_up
    data['form_html'] = render_to_string(template, {'form': form, "title": title}, request=request)
    return data
