from django import forms
from django.forms.widgets import PasswordInput


class LoginForm(forms.Form):
    title = forms.CharField(max_length=50, label='계정')
    content = forms.CharField(
        max_length=12, widget=PasswordInput, required=True, label='패스워드')
