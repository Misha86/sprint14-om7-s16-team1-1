from rest_framework import serializers
from authentication.serializers import CustomUserSerializer

from order.models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='order:order-detail', lookup_field='pk')
    user = serializers.SlugRelatedField(read_only=True, slug_field='email')

    class Meta:
        model = Order
        fields = ['url', 'id', 'user']


class OrderDetailSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(read_only=True, slug_field='email')
    user = CustomUserSerializer()
    book = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Order
        fields = ['id', 'user', 'book', 'created_at', 'end_at', 'plated_end_at']


