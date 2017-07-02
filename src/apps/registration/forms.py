from django import forms
from src.apps.personalp.models import Personal_info
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

class UserForm(UserCreationForm):
    #error_messages = {
    #    'password_mismatch': ("The two password fields didn't match."),
    #}
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, error_messages={'required': 'Set the password'})
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput,
                                help_text=("Enter the same password as above, for verification."),
                                error_messages = {'required': 'Please again'})

    def clean(self):
        if (self.cleaned_data.get("password2") != self.cleaned_data.get("password1") or len((self.cleaned_data.get("password2")))<=6):
            raise forms.ValidationError("Passwords are not match and please use only latin letters no less than 6 characters")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

class Personal_info_form(forms.ModelForm):
    class Meta:
        model = Personal_info
        fields = ("gender", "location","img_pers","birth_date","nick_name")

        # class UserForm( forms.ModelForm ):
        #    username = forms.CharField( max_length = 30 )
        #    firstname = forms.CharField( max_length = 30, required = False )
        #    lastname = forms.CharField( max_length = 30, required = False )
        #    email = forms.CharField( max_length = 30 )
        #    pass1 = forms.CharField( widget = forms.PasswordInput, label = "Пароль", min_length = 6, max_length = 30 )
        #    pass2 = forms.CharField( widget = forms.PasswordInput, label = "Пароль ещё раз" )

