import datetime
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django import forms
from .models import Order
from book.models import Book
from authentication.models import CustomUser


class UserSelect(forms.ModelChoiceField):
    def label_from_instance(self, member):
        return member.get_full_name().title()


class BookSelect(forms.ModelChoiceField):
    def label_from_instance(self, member):
        return member.name.title()


class OrderForm(forms.ModelForm):
    error_css_class = "error"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')

        super().__init__(*args, **kwargs)

        self.fields['user'].widget.attrs.update({'class': 'form-control'})
        self.fields['book'].widget.attrs.update({'class': 'form-control'})
        self.fields['end_at'].widget.attrs.update({'class': 'form-control datepicker', 'autocomplete': 'off'})
        self.fields['plated_end_at'].widget.attrs.update({'class': 'form-control datepicker', 'autocomplete': 'off'})

    class Meta:
        model = Order
        fields = '__all__'

    user = UserSelect(queryset=CustomUser.objects.all(), widget=forms.Select)
    book = BookSelect(queryset=Book.objects.all(), widget=forms.Select)

    def clean_plated_end_at(self):
        created_at = self.cleaned_data.get('created_at')
        plated_end_at = self.cleaned_data['plated_end_at']
        date = created_at if created_at else timezone.now()
        if plated_end_at < date:
            raise ValidationError(_("Plated end at date must be more as creation date !"))
        return plated_end_at

    def clean_end_at(self):
        created_at = self.cleaned_data.get('created_at')
        end_at = self.cleaned_data['end_at']
        date = created_at if created_at else timezone.now()
        if end_at and end_at < date:
            raise ValidationError(_("End at date must be more as creation date !"))
        return end_at
