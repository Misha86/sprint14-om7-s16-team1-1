from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='authentication:user-detail', lookup_field='pk')

    class Meta:
        model = CustomUser
        fields = ['url', 'id', 'email', 'first_name']


class CustomUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'middle_name', 'last_name', 'role', 'is_active']


