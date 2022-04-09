from django.urls import path
from . import views_rest


app_name = "authentication"

urlpatterns = [
    path('', views_rest.CustomUserViewSet.as_view(), name='user-list'),
    path('<int:pk>/', views_rest.CustomUserDetailViewSet.as_view(), name='user-detail'),
    path('<int:user_pk>/order/<int:order_pk>', views_rest.UserOrderDetailViewSet.as_view(), name='user-order-detail')
]
