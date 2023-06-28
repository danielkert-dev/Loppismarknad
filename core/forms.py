from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from core.models import EmailNotification


from django.contrib.auth import update_session_auth_hash


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Din användarnamn',
            'class': 'form-control my-2'
        }),
        error_messages={
            'required': 'Användarnamn är obligatoriskt.',
            'invalid': 'Ogiltigt användarnamn eller lösenord.',
        }
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Din lösenord',
            'class': 'form-control my-2'
        }),
        error_messages={
            'required': 'Lösenord är obligatoriskt.',
            'invalid': 'Ogiltigt användarnamn eller lösenord.',
        }
    )

    error_messages = {
        'invalid_login': 'Felaktigt användarnamn eller lösenord. Var god försök igen.',
    }
    def form_invalid(self, form):
        form.add_error(None, self.error_messages['invalid_login'])
        return super().form_invalid(form)

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Din användarnamn',
            'class': 'form-control my-2'
        }),
        error_messages={
            'required': 'Användarnamn är obligatoriskt.',
            'unique': 'Det användarnamnet är redan taget.',
        }
    )

    email = forms.CharField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Din e-postadress',
            'class': 'form-control my-2'
        }),
        error_messages={
            'required': 'E-postadress är obligatorisk.',
            'invalid': 'Ogiltig e-postadress.',
        }
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Din lösenord',
            'class': 'form-control my-2'
        }),
        error_messages={
            'required': 'Lösenord är obligatoriskt.',
        }
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Bekräfta lösenord',
            'class': 'form-control my-2'
        }),
        error_messages={
            'required': 'Bekräfta lösenord är obligatoriskt.',
            'password_mismatch': 'Lösenorden matchar inte.',
        }
    )



class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control my-2'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class EmailNotificationForm(forms.ModelForm):

    class Meta:
        model = EmailNotification
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-check-input', 'type': 'checkbox'}),
        }