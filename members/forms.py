from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django import forms
from django.http import request
from .models import *
# Edit Form


class UserEditingForm(UserChangeForm):
    username = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_joined = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ( 'username', 'email', 'first_name', 'last_name', 'password','last_login', 'date_joined')


class PasswordUpdateForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control", "type": "password"}))
    new_password1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control", "type": "password"}))
    new_password2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control", "type": "password"}))

    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")


class UserProfileForm(forms.ModelForm):
    bio = forms.CharField(max_length=80, widget=forms.Textarea(attrs={"class":"form-control", "placeholder":  "Enter Your Bio Here"}))
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control"}))
    
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic')

