from rest_framework import serializers
from rest_framework.reverse import reverse

from order.models import Order
from .models import CustomUser


class CustomerHyperlink(serializers.HyperlinkedRelatedField):
    # We define these as class attributes, so we don't need to pass them as arguments.
    view_name = 'authentication:user-order-detail'
    queryset = Order.objects.all()

    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'user_pk': obj.user.pk,
            'order_pk': obj.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
           'user__pk': view_kwargs['user_pk'],
           'pk': view_kwargs['order_pk']
        }
        return self.get_queryset().get(**lookup_kwargs)


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='authentication:user-detail', lookup_field='pk')

    class Meta:
        model = CustomUser
        fields = ['url', 'id', 'email', 'first_name', 'last_name']


class CustomUserDetailSerializer(serializers.ModelSerializer):
    # orders = serializers.HyperlinkedRelatedField(many=True, view_name='order:order-detail', read_only=True)
    orders = CustomerHyperlink(many=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'middle_name', 'last_name', 'role', 'is_active', 'orders']


