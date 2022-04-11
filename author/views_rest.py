from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Author
from .serializers import AuthorSerializer


class AuthorGenerics(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
