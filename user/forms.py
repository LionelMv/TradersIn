from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class SignUpForm(UserCreationForm):
    """Form for creating new users"""
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)

    class Meta:
        """Form metadata"""
        model = User
        fields = ["username", "first_name", "last_name",
                  "email", "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
    """Form to update user details"""
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)

    class Meta:
        """Form metadata"""
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class ProfileUpdateForm(forms.ModelForm):
    """Form to update profile picture and bio"""
    bio = forms.CharField(label="Bio", required=False, widget=forms.Textarea)
    image = forms.ImageField(label="Profile Picture", required=False)

    class Meta:
        """Form metadata"""
        model = Profile
        fields = ["bio", "image"]
