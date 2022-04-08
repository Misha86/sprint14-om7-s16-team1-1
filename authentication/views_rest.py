from rest_framework import generics
from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from order.models import Order
from order.serializers import OrderDetailSerializer
from .serializers import CustomUserSerializer, CustomUserDetailSerializer
from .models import CustomUser
from .permissions import IsAdmOrIsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class CustomUserViewSet(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['first_name', 'last_name', 'orders']
    ordering_fields = ['first_name', 'last_name', 'email']
    search_fields = ['orders__book__name']


class CustomUserDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserDetailSerializer

    permission_classes = [IsAdmOrIsOwnerOrReadOnly]


class UserOrderDetailViewSet(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        user_pk = self.kwargs['user_pk']
        order_pk = self.kwargs['order_pk']
        obj = get_object_or_404(queryset.filter(user_id=user_pk), id=order_pk)
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj


