from django.urls import path
from authentication.views_rest import CustomUserViewSet

user_list = CustomUserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
#
# snippet_detail = CustomUserViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# user_list = CustomUserViewSet.as_view({
#     'get': 'list'
# })
#
user_detail = CustomUserViewSet.as_view({
    'get': 'retrieve'
})

app_name = "authentication"

urlpatterns = [
    path('', user_list, name='user-list'),
    path('<int:pk>/', user_detail, name='user-detail')
]
