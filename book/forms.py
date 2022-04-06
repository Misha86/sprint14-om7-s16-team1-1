from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django import forms
from .models import Book
from author.models import Author


class CustomSelectMultiple(forms.ModelMultipleChoiceField):
    def label_from_instance(self, member):
        return member.get_full_name().title()


class BookForm(forms.ModelForm):
    error_css_class = "error"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')

        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': _('Input name of book')})
        self.fields['description'].widget.attrs.update({'class': 'form-control',
                                                        'placeholder': _('Input description of book'), 'rows': 4})
        self.fields['count'].widget.attrs.update({'class': 'form-control'})
        self.fields['authors'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Book
        fields = ['name', 'description', 'count', 'authors']

    authors = CustomSelectMultiple(queryset=Author.objects.all(), widget=forms.SelectMultiple)

    def clean_count(self):
        count = self.cleaned_data.get('count')
        if count and count < 0:
            raise ValidationError(_("Count must be positive number!"))
        return count

