from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django import forms
from .models import CustomUser


# class CustomSelectMultiple(forms.ModelMultipleChoiceField):
#     def label_from_instance(self, member):
#         return member.get_full_name().title()

#
# class BookForm(forms.ModelForm):
#     error_css_class = "error"
#
#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault('label_suffix', '')
#
#         super().__init__(*args, **kwargs)
#
#         self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': _('Input name of book')})
#         self.fields['description'].widget.attrs.update({'class': 'form-control',
#                                                         'placeholder': _('Input description of book'), 'rows': 4})
#         self.fields['count'].widget.attrs.update({'class': 'form-control'})
#         self.fields['authors'].widget.attrs.update({'class': 'form-control'})
#
#     class Meta:
#         model = Book
#         fields = ['name', 'description', 'count', 'authors']
#
#     authors = CustomSelectMultiple(queryset=Author.objects.all(), widget=forms.SelectMultiple)
#
#     def clean_count(self):
#         count = self.cleaned_data.get('count')
#         if count and count < 0:
#             raise ValidationError(_("Count must be positive number!"))
#         return count


class CustomUserForm(forms.ModelForm):
    """A form for creating new_profile users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label=_('Password'),
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': _('Enter password')}))
    password2 = forms.CharField(label=_('Password confirmation'),
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': _('Repeat password')}))

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'middle_name']

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        valid_password = validate_password(password1)
        if valid_password is not None:
            raise valid_password.ValidationError()
        return password1

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Passwords no match"))
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# class BuyerRegisterForm(forms.ModelForm):
#     """
#     A form that creates a user, with no privileges, from the given username and
#     password.
#     """
#     # sex = forms.ChoiceField(label="Пол", choices=(('Man', 'Мужчина'), ('Woman', 'Женщина')),
#     #                         widget=RadioSelectWidget(attrs={'class': 'option-input radio'}))
#
#     class Meta:
#         model = CustomUser
#
#         widgets = {'email': forms.EmailInput(attrs={'class': 'form-control', 'rows': 4,
#                                                     'placeholder': 'введите E-mail'}),
#                    'first_name': forms.TextInput(attrs={'class': 'form-control', 'rows': 4,
#                                                         'placeholder': "введите имя"}),
#                    'last_name': forms.TextInput(attrs={'class': 'form-control', 'rows': 4,
#                                                        'placeholder': "введите фамилию"}),
#                    'date_of_birth': CalendarWidget(format='%Y-%m-%d',
#                                                    attrs={'class': 'form-control',
#                                                           'id': 'id_date_of_birth',
#                                                           'placeholder': 'дата рождения',
#                                                           'autocomplete': 'off'}),
#                    'phone_number': forms.TextInput(attrs={'class': 'form-control', 'rows': 4,
#                                                           'placeholder': "введите номер телефона"}),
#                    # 'sex': RadioSelectWidget(attrs={'class': 'option-input radio'})
# }
#
#         labels = {'email': "E-mail",
#                   'first_name': "Имя",
#                   'last_name': "Фамилия",
#                   'date_of_birth': "Дата рождения",
#                   # 'sex': "Пол",
#                   'phone_number': "Номер телефона"}
#
#         help_texts = {'phone_number': 'формат ввода номера телефона +380967578910'}
