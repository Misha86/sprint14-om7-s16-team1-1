from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Book
from author.models import Author


class CustomSelectMultiple(forms.ModelMultipleChoiceField):
    def label_from_instance(self, member):
        return member.get_full_name().title()


class BookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': _('Input name of book')})
        self.fields['description'].widget.attrs.update({'class': 'form-control',
                                                        'placeholder': _('Input description of book'), 'rows': 4})
        self.fields['count'].widget.attrs.update({'class': 'form-control'})
        self.fields['authors'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Book
        fields = '__all__'

    authors = CustomSelectMultiple(queryset=Author.objects.all(), widget=forms.SelectMultiple)
