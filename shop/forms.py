from django import forms
from .models import Product
from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):

    class Meta:
        model=User
        fields=(
            'username',
            'email',
            'password1',
            'password2',
        )

class Productform(forms.ModelForm):
    class Meta:
        model = Product
        fields=('__all__')
