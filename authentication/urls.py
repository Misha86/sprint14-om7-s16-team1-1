from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [
    path('list/', views.user_list, name='user-list'),
    path('<int:id>/', views.user_books, name='user-books'),
    path('list/violator/', views.users_violators, name='users-violators'),
    path('registration/', views.user_form, name='user-registration'),
    path('logout/', views.user_logout, name='user-logout')
]
