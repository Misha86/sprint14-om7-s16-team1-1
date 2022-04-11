from django.urls import path
from . import views_rest


app_name = "book"

urlpatterns = [
    path('', views_rest.BookGenerics.as_view(), name='book-list'),
    path('<int:pk>/', views_rest.BookDetailGenerics.as_view(), name='book-detail'),
]