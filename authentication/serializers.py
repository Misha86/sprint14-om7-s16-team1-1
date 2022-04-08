from rest_framework import serializers
from .models import CustomUser


# class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['url', 'email']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email']