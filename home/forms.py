from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    username = forms.CharField(max_length= 300,  help_text=u"Username")

    class Meta:
        model= User
        fields = ['username','email','password']
