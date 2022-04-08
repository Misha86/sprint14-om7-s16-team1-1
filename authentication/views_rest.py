from rest_framework import generics
from rest_framework import permissions

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
    ordering_fields = ['first_name', 'email']
    search_fields = ['orders__book__name']

    #
    # def get_queryset(self):
    #     """
    #     This view should return a list of all the purchases
    #     for the currently authenticated user.
    #     """
    #     user = self.request.user
    #     return queryset = CustomUser.objects.all().filter(purchaser=user)


class CustomUserDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserDetailSerializer
    permission_classes = [IsAdmOrIsOwnerOrReadOnly]


