from django.urls import path
from . import views

app_name = "Order"

urlpatterns = [
    path('list/', views.order_list, name='order-list'),
    path('<int:id>/', views.order_book, name='order-book'),
    path('add/', views.order_form, name='order-add'),
    path('<int:id>/update/', views.order_form, name='order-update'),
]
