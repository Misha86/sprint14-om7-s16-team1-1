from rest_framework import serializers
from rest_framework.reverse import reverse
from django.contrib.auth.hashers import make_password

from order.models import Order
from .models import CustomUser


class CustomerHyperlink(serializers.HyperlinkedRelatedField):
    view_name = 'authentication:user-order-detail'
    queryset = Order.objects.all()

    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'user_id': obj.user.pk,
            'id': obj.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
           'user_id': view_kwargs['user_id'],
           'id': view_kwargs['id']
        }
        return self.get_queryset().get(**lookup_kwargs)


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='authentication:user-detail', lookup_field='pk')

    password = serializers.CharField(write_only=True, required=True, help_text='Leave empty if no change needed',
                                     style={'input_type': 'password', 'placeholder': 'Password'})

    class Meta:
        model = CustomUser
        fields = ['url', 'id', 'email', 'first_name', 'middle_name', 'last_name', 'role', 'is_active', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)


class CustomUserDetailSerializer(serializers.ModelSerializer):
    # orders = serializers.HyperlinkedRelatedField(many=True, view_name='authentication:user-order-detail', read_only=True)
    orders = CustomerHyperlink(many=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'middle_name', 'last_name', 'role', 'is_active', 'orders']


class UserOrderDetailSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Order
        fields = ['id', 'user', 'book', 'created_at', 'end_at', 'plated_end_at']


