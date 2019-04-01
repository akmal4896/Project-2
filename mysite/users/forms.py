from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #the default is required equals to true

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
