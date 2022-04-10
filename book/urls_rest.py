from django.urls import path
from . import views_rest


app_name = "book"

urlpatterns = [
    path('', views_rest.AuthorGenerics.as_view(), name='book-list'),
    path('<int:pk>/', views_rest.AuthorDetailGenerics.as_view(), name='book-detail'),
    # path('<int:user_id>/order/<int:id>', views_rest.UserOrderDetailGenerics.as_view(), name='user-order-detail')
]