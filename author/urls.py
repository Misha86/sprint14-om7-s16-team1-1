from django.urls import path
from author import views

app_name = 'author'

urlpatterns = [
    path('list/', views.author_list, name='author-list'),
    path('books/<int:id>/', views.author_books, name='author-books'),
]
