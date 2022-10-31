from django import forms
from django.contrib.auth.forms import UserCreationForm
from lct4.models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput())
    first_name = forms.CharField(label='Имя', widget=forms.TextInput())

    class Meta:
        model = CustomUsers
        fields = {'username', 'password1', 'password2', 'last_name', 'first_name'}

    field_order = ['username', 'last_name', 'first_name', 'password1', 'password2']