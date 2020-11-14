from django import forms
from .models import User

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=256, help_text='Это поле обязательно')
    password = forms.CharField(label='Enter password', widget=forms.PasswordInput)
