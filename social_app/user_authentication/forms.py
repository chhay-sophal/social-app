from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from .models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class RegistrationForm(UserCreationForm):
    name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'name', 'email')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'email', 'bio')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'email', 'bio')