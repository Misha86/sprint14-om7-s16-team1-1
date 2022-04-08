from django.urls import path
from authentication.views_rest import CustomUserViewSet, CustomUserDetailViewSet

# user_list = CustomUserViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# #
# # snippet_detail = CustomUserViewSet.as_view({
# #     'get': 'retrieve',
# #     'put': 'update',
# #     'patch': 'partial_update',
# #     'delete': 'destroy'
# # })
# #
# # user_list = CustomUserViewSet.as_view({
# #     'get': 'list'
# # })
# #
# user_detail = CustomUserViewSet.as_view({
#     'get': 'retrieve'
# })

app_name = "authentication"

urlpatterns = [
    path('', CustomUserViewSet.as_view(), name='user-list'),
    path('<int:pk>/', CustomUserDetailViewSet.as_view(), name='user-detail')
]
