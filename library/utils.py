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


def sort_orders_by(request, orders):
    if request.method == 'GET' and request.GET.get('sort'):
        value = request.GET.get('sort')
        if value == 'created-high-low':
            orders = orders.order_by('-created_at')
        elif value == 'created-low-high':
            orders = orders.order_by('created_at')
        elif value == 'plated-at-high-low':
            orders = orders.order_by('-plated_end_at')
        elif value == 'plated-at-low-high':
            orders = orders.order_by('plated_end_at')
    return orders
