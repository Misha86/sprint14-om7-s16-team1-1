from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [
    path('list/', views.authentication_list, name='user-list'),
]