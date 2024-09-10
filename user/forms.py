from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class RegisterUser(UserCreationForm):
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-5', 'placeholder':'••••••••••••'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-5', 'placeholder':'••••••••••••'}))

    class Meta:
        model = User
        fields = ['username','email','first_name','first_name']

    def clean(self) -> dict[str, Any]:
        cleaned_data = super(RegisterUser, self).clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise ValidationError("Passwords are not match!")


class LoginUser(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-5', 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-5', 'placeholder':'••••••••••••'}))
