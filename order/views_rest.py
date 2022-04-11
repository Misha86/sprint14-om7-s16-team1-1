from rest_framework import generics

from .serializers import OrderSerializer, OrderDetailSerializer
from order.models import Order


class OrderViewSet(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer



