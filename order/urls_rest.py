from django.urls import path
import views_rest

app_name = "order"

urlpatterns = [
    path('', views_rest.OrderViewSet.as_view(), name='order-list'),
    path('<int:pk>/', views_rest.OrderDetailViewSet.as_view(), name='order-detail')
]
