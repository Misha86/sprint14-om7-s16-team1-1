from django.utils import timezone
from rest_framework import serializers
from authentication.models import CustomUser
from book.models import Book
from order.models import Order
from django.utils.translation import gettext_lazy as _


class UserRelatedField(serializers.PrimaryKeyRelatedField):
    def display_value(self, instance):
        return instance.get_full_name()


class BookRelatedField(serializers.PrimaryKeyRelatedField):
    def display_value(self, instance):
        return instance.name


class OrderDetailSerializer(serializers.ModelSerializer):
    user = UserRelatedField(queryset=CustomUser.objects.all())
    book = BookRelatedField(queryset=Book.objects.all())

    class Meta:
        model = Order
        fields = ['id', 'user', 'book', 'created_at', 'end_at', 'plated_end_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.get_full_name()
        representation['book'] = instance.book.name
        return representation

    def validate(self, data):
        created_at = data.get('created_at')
        end_at = data.get('end_at')
        plated_end_at = data.get('plated_end_at')
        date = timezone.now() if not created_at else created_at
        if date:
            if plated_end_at and plated_end_at < date:
                raise serializers.ValidationError(_("Plated end at date must be more as creation date!"))
            if end_at and end_at < date:
                raise serializers.ValidationError(_("End at date must be more as creation date!"))
        return super().validate(data)


class OrderSerializer(OrderDetailSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='order:order-detail', lookup_field='pk')

    class Meta(OrderDetailSerializer.Meta):
        fields = ['url', 'id', 'user', 'book', 'end_at', 'plated_end_at']
        write_only = ['end_at', 'plated_end_at']








