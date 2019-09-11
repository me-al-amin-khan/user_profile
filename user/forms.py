from django import forms
from django.forms import ModelForm
from .models import UserProfile
from django.contrib.auth.models import User

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['portfolio_site', 'profile_pic']
