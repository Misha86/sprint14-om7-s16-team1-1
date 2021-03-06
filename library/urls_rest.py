from django.urls import include, path

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('authentication:user-list', request=request, format=format),
        'orders': reverse('order:order-list', request=request, format=format),
        'authors': reverse('author:author-list', request=request, format=format),
        'books': reverse('book:book-list', request=request, format=format),
    })


urlpatterns = [
    path('', api_root),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth_token/', include('djoser.urls.authtoken')),
    path('api/v1/user/', include('authentication.urls_rest', namespace="authentication")),
    path('api/v1/order/', include('order.urls_rest', namespace="order")),
    path('api/v1/author/', include('author.urls_rest', namespace="author")),
    path('api/v1/book/', include('book.urls_rest', namespace="book")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
