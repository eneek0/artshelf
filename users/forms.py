from dataclasses import fields
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField()
    password = forms.CharField()


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "password1",
            "password2",
        )
    
    email = forms.CharField()
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "username",
            "description",
            "city")

    image = forms.ImageField(required=False)
    username = forms.CharField()
    description = forms.CharField()
    city = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['class'] = 'form__input'
        self.fields['username'].widget.attrs['class'] = 'form__input'
        self.fields['description'].widget.attrs['class'] = 'form__input'
        self.fields['city'].widget.attrs['class'] = 'form__input'