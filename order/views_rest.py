from rest_framework import generics

from .serializers import OrderSerializer, OrderDetailSerializer
from order.models import Order


class OrderViewSet(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    # filterset_fields = ['first_name', 'last_name', 'orders']
    # ordering_fields = ['first_name', 'last_name', 'email']
    # search_fields = ['orders__book__name']


class OrderDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer



