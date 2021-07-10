from django import forms
from django.forms.models import ModelForm
from htc.users.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=10)
    bio = forms.CharField(max_length=1000)
    password = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'bio',
            'password1',
            'password2'
        )