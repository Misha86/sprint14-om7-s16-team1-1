from django.shortcuts import render
from .models import CustomUser


def authentication_list(request):
    return render(request, 'user_list.html', {'title': 'Users',
                                        'users': CustomUser.objects.all()})
