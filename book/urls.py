from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.book_list, name='book-list'),
    path('list/unordered/', views.unordered_books, name='unordered-books'),
    path('<int:id>/', views.book, name='book'),
]
