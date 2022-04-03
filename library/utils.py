from django.db.models import Q


def search_books(request, books):
    if request.method == 'GET' and request.GET.get('q'):
        query = request.GET.get('q')
        return books.filter(Q(name__contains=query) | Q(authors__patronymic__contains=query)
                            | Q(authors__name__contains=query)
                            | Q(authors__surname__contains=query)).distinct()
    else:
        return books


def sort_by(request, books):
    if request.method == 'GET' and request.GET.get('sort'):
        value = request.GET.get('sort')
        if value == 'name-a-z':
            books = books.order_by('name')
        elif value == 'name-z-a':
            books = books.order_by('-name')
        elif value == 'count-low-high':
            books = books.order_by('count')
        elif value == 'count-high-low':
            books = books.order_by('-count')
    return books
