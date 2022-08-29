from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

from django.contrib.auth.models import User
from django.http import request

from member.models import *

from cloudinary.forms import CloudinaryInput, CloudinaryFileField

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
# FORMS FOR PROFILE

class USEREDITFORM(UserChangeForm):
    username = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}))
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}))
    last_login = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}))
    date_joined = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}))

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, label=None, required=True)

    class Meta:
        model = User
        fields = ( 'username', 'email', 'first_name', 'last_name', 'password','last_login', 'date_joined', 'captcha')



class PASSWORDUPDATINGFORM(PasswordChangeForm):
    old_password = forms.CharField(max_length=100,label="Enter the old password", widget=forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', "type": "password"}))
    new_password1 = forms.CharField(max_length=100, label='Enter the new password', widget=forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', "type": "password"}))
    new_password2 = forms.CharField(max_length=100,label='Enter the new password again' , widget=forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', "type": "password"}))

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, label=None, required=True)

    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2", 'captcha')

