from django import forms
from django.forms.models import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=10)
    bio = forms.CharField(max_length=1000)

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

class UserAuthenticationForm(ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "password"]
    
    def clean(self):
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid login")

