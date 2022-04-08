from rest_framework import serializers

from order.models import Order
from .models import CustomUser


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='authentication:user-detail', lookup_field='pk')

    class Meta:
        model = CustomUser
        fields = ['url', 'id', 'email', 'first_name']


class CustomUserDetailSerializer(serializers.ModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all()) # view_name='snippet-detail' change queryset=Order.objects.all()

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'middle_name', 'last_name', 'role', 'is_active', 'orders']


