from django.urls import path
from . import views

app_name = "Order"

urlpatterns = [
    path('list/', views.order_list, name='order-list'),
    path('<int:id>/', views.order_book, name='order-book'),
]