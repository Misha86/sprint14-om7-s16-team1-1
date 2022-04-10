from django.urls import path, include
from . import views_rest
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('authors', views_rest.AuthorView)
#
# urlpatterns = [
#     path('', include(router.urls))
# ]


app_name = "author"

urlpatterns = [
    # path('', views_rest.AuthorView.as_view({'get': 'list'}), name='author-list'),
    path('', views_rest.AuthorGenerics.as_view(), name='author-list'),
    path('<int:pk>/', views_rest.AuthorDetailGenerics.as_view(), name='user-detail'),
    # path('<int:user_id>/order/<int:id>', views_rest.UserOrderDetailGenerics.as_view(), name='user-order-detail')
]