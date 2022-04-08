from django.urls import path
from authentication import views_rest

# user_list = views_rest.CustomUserViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# #
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
# user_detail = views_rest.CustomUserDetailViewSet.as_view({
#     'get': 'retrieve'
# })

app_name = "authentication"

urlpatterns = [
    path('', views_rest.CustomUserViewSet.as_view(), name='user-list'),
    path('<int:pk>/', views_rest.CustomUserDetailViewSet.as_view(), name='user-detail')
]
