from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Q



username_regex_field = forms.RegexField(
    label='Username',
    max_length=30,
    regex=r'^[a-z0-9-_]+$',
    error_messages={
        'required': 'Please enter your name',
        'invalid': 'Lowercase alphanumeric characters and underscores and dashes only (a-z, 0-9, _, -)'
    },
)

password_char_field = forms.CharField(
    label='Password',
    max_length=30,
    widget=forms.PasswordInput,
)

confirm_password_char_field = forms.CharField(
    label='Confirm Password',
    max_length=30,
    widget=forms.PasswordInput,
)



class LoginForm(forms.Form):
    username_email = forms.CharField(
        label='Username or Email',
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username or Email',
                'autofocus': 'autofocus',
            },
        ),
        error_messages={'required': 'Please enter your username or email', 'invalid': 'Please enter your username or email'},
    )
    password = password_char_field
    password.widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            },
    )
    next = forms.CharField(
        widget=forms.HiddenInput,
    )

    def clean(self):
        # try to get with email first (user may submit username or email)
        try:
            user = User.objects.get(
                Q(username=self.cleaned_data.get('username_email')) |
                Q(email=self.cleaned_data.get('username_email'))
            )
        except User.DoesNotExist:
            raise forms.ValidationError(
                "No username or email found matching \"%s\"." % self.cleaned_data.get('username_email')
            )
        return self.cleaned_data



class RegisterForm(forms.Form):
    username = username_regex_field
    password = password_char_field
    confirm_password = confirm_password_char_field

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords don't match")

        return self.cleaned_data



class ProfileForm(forms.Form):
    username = username_regex_field
    first_name = forms.RegexField(
        label='First Name',
        max_length=30,
        regex=r'^[a-zA-Z-_]+$',
        error_messages={'invalid': 'Alphabetical, underscores, and dashes only (a-z, A-Z, _, -)'},
        required=False,
    )
    last_name = forms.RegexField(
        label='First Name',
        max_length=30,
        regex=r'^[a-zA-Z-_]+$',
        error_messages={'invalid': 'Alphabetical, underscores, and dashes only (a-z, A-Z, _, -)'},
        required=False,
    )
    email = forms.EmailField(
        label='First Name',
        max_length=50,
        required=False,
    )
    password = password_char_field
    confirm_password = confirm_password_char_field

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")

        return self.cleaned_data
