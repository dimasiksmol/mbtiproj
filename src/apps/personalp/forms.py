from .models import Personal_info
from django import forms

class PersonalPImg(forms.ModelForm):
    #pers_img = forms.ImageField()
    class Meta:
        model = Personal_info
        fields = ['img_pers']