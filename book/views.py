from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Book


def home_page(request):
    return TemplateResponse(request, 'base.html')


def book_list(request):
    return render(request, 'book_list.html', {'books': Book.get_all()})

