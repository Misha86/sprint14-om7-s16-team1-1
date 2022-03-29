from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('book-list/', views.book_list, name='book-list'),
]
