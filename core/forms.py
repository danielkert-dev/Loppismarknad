from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Din användarnamn',
        'class': 'form-control my-2'
    }))
        
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Din lösenord',
        'class': 'form-control my-2'
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Din användarnamn',
        'class': 'form-control my-2'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Din e-postadress',
        'class': 'form-control my-2'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Din lösenord',
        'class': 'form-control my-2'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Bekräfta lösenord',
        'class': 'form-control my-2'
    }))