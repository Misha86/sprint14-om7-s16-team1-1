from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import CustomUser


class CustomUserForm(forms.ModelForm):
    """A form for creating new_profile users. Includes all the required
    fields, plus a repeated password."""
    error_css_class = "error"

    password1 = forms.CharField(label=_('Password'),
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': _('Enter password')}))
    password2 = forms.CharField(label=_('Password confirmation'),
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': _('Repeat password')}))

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': _('Input email')})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': _('Input first name')})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': _('Input last name')})
        self.fields['middle_name'].widget.attrs.update({'class': 'form-control', 'placeholder': _('Input middle name')})

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


class CustomUserLoginForm(forms.Form):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_css_class = "error"

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': _('Input email')}))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': _('Input password')}))

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_exists = CustomUser.objects.filter(email=email).exists()
        if not email_exists:
            raise forms.ValidationError(_("User does not exist!"), code='email_exists')
        else:
            return email

    def clean_password(self):
        password = self.cleaned_data.get("password")
        email = self.cleaned_data.get("email")
        user = CustomUser.objects.filter(email=email)
        if user.exists() and user[0].check_password(password):
            return password
        elif user.exists() and password is not None:
            raise forms.ValidationError(_("Invalid password!"))
