from django.urls import path
from . import views_rest


app_name = "authentication"

urlpatterns = [
    path('', views_rest.CustomUserGenerics.as_view(), name='user-list'),
    path('<int:pk>/', views_rest.CustomUserDetailGenerics.as_view(), name='user-detail'),
    path('<int:user_id>/order/<int:id>', views_rest.UserOrderDetailGenerics.as_view(), name='user-order-detail')
]
