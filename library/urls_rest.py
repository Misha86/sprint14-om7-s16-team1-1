from django.urls import include, path

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('authentication:user-list', request=request, format=format),
        # 'snippets': reverse('snippet-list', request=request, format=format)
    })


urlpatterns = [
    path('', api_root),
    path('api/v1/user/', include('authentication.urls_rest', namespace="authentication")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
