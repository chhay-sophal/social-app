from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from apps.user_authentication.models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'bio']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']