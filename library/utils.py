from django.db.models import Q


def search_books(request, books):
    if request.method == 'GET' and request.GET.get('q'):
        query = request.GET.get('q')
        return books.filter(Q(name__contains=query) | Q(authors__patronymic__contains=query)
                            | Q(authors__name__contains=query)
                            | Q(authors__surname__contains=query)).distinct()
    else:
        return books