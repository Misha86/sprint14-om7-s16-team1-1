from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, exceptions
from rest_framework.reverse import reverse
from django.contrib.auth.hashers import make_password

from order.models import Order
from .models import CustomUser


def validator_password(password):
    errors = dict()
    try:
        validate_password(password)
    except exceptions.ValidationError as e:
        errors['new_password'] = list(e.messages)

    if errors:
        raise serializers.ValidationError(errors)


class CustomerHyperlink(serializers.HyperlinkedRelatedField):
    view_name = 'authentication:user-order-detail'

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


class CustomUserFullNameField(serializers.RelatedField):
    def to_representation(self, value):
        return value.get_full_name()


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='authentication:user-detail', lookup_field='pk')

    password = serializers.CharField(write_only=True, required=True, help_text='Leave empty if no change needed',
                                     style={'input_type': 'password', 'placeholder': 'Password'},
                                     validators=[validator_password])

    class Meta:
        model = CustomUser
        fields = ['url', 'id', 'email', 'first_name', 'middle_name', 'last_name', 'role', 'is_active', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)


class CustomUserDetailSerializer(serializers.ModelSerializer):

    orders = CustomerHyperlink(many=True, read_only=True)

    new_password = serializers.CharField(write_only=True, allow_blank=True,
                                         style={'input_type': 'password', 'placeholder': 'New Password'})

    confirm_new_password = serializers.CharField(write_only=True, allow_blank=True,
                                                 help_text='Leave empty if no change needed',
                                                 style={'input_type': 'password',
                                                        'placeholder': 'Confirmation Password'})

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'middle_name', 'last_name', 'role', 'is_active',
                  'orders', 'new_password', 'confirm_new_password']

    def validate(self, data):
        new_password = data.get('new_password')
        confirm_new_password = data.get('confirm_new_password')
        if new_password and confirm_new_password:
            if new_password != confirm_new_password:
                raise serializers.ValidationError("Password confirmation does not match.")
            else:
                validator_password(new_password)
        elif any([new_password, confirm_new_password]):
            raise serializers.ValidationError("Didn`t enter the password confirmation.")

        return super().validate(data)

    def update(self, instance, validated_data):
        confirm_new_password = validated_data.pop('confirm_new_password')
        if confirm_new_password:
            validated_data['password'] = make_password(confirm_new_password)
        return super().update(instance, validated_data)


class UserOrderDetailSerializer(serializers.HyperlinkedModelSerializer):
    book = serializers.SlugRelatedField(read_only=True, slug_field='name')
    user = CustomUserFullNameField(read_only=True)

    # url = serializers.HyperlinkedIdentityField(view_name='order:order-detail', lookup_field='pk')

    class Meta:
        model = Order
        fields = ['id', 'user', 'book', 'created_at', 'end_at', 'plated_end_at']
