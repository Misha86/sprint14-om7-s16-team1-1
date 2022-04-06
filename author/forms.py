from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Author


class AuthorForm(forms.ModelForm):
    error_css_class = "error"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')

        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': _('Input name')})
        self.fields['surname'].widget.attrs.update({'class': 'form-control', 'placeholder': _('Input surname')})
        self.fields['patronymic'].widget.attrs.update({'class': 'form-control', 'placeholder': _('Input surname')})

    class Meta:
        model = Author
        fields = '__all__'


