from rest_framework import generics
from rest_framework import permissions

from .serializers import CustomUserSerializer, CustomUserDetailSerializer
from .models import CustomUser
from .permissions import IsAdmOrIsOwnerOrReadOnly


class CustomUserViewSet(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserDetailSerializer
    permission_classes = [IsAdmOrIsOwnerOrReadOnly]


