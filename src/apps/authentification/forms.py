from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from src.apps.personalp.models import Personal_info

class AuthentificationForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

#class AuthentificationForm(AuthenticationForm):
#    form = AuthenticationForm

    #def clean_data(self):
    #    cleaned_data = super(AuthentificationForm, self).clean()
    #    username = cleaned_data.get('username')
    #    password = cleaned_data.get('password')

