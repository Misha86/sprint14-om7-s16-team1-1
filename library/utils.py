from django.db.models import Q


def search_books(request, books):
    if request.method == 'GET' and request.GET.get('q'):
        query = request.GET.get('q')
        return books.filter(Q(name__contains=query) | Q(authors__patronymic__contains=query)
                            | Q(authors__name__contains=query)
                            | Q(authors__surname__contains=query)).distinct()
    else:
        return books


def sort_by(request, query):
    sort_by = request.GET.get('sort', '')
    sort_by_session = request.session.get('sort')
    if sort_by != '' and sort_by != request.session.get('sort'):
        request.session['sort'] = sort_by
        query = query.order_by(sort_by)
    elif sort_by_session == sort_by:
        query = query.order_by(sort_by)
    elif not sort_by and sort_by_session:
        del request.session['sort']
    return query
