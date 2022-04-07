from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.book_list, name='book-list'),
    path('list/form/', views.book_form, name='book-form'),
    path('list/unordered/', views.unordered_books, name='unordered-books'),
    path('<int:id>/', views.book, name='book'),
    path('add/', views.book_form, name='book-add'),
    path('<int:id>/update/', views.book_form, name='book-update'),
]
