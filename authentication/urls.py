from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [
    path('list/', views.user_list, name='user-list'),
    path('<int:id>/', views.user_books, name='user-books'),
]