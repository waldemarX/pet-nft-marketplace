from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UsernameField,
    UserCreationForm,
    UserChangeForm
)

from .models import User, Item


class UserLoginForm(AuthenticationForm):
    username = UsernameField(
        label="",
    )
    password = forms.CharField(
        label="",
    )

    # username = UsernameField(
    #     label="",
    #     widget=forms.TextInput(attrs={
    #         "autofocus": True,
    #         "class": "form-control",
    #         "placeholder": "username",
    #     })
    # )
    # password = forms.CharField(
    #     label="",
    #     widget=forms.PasswordInput(attrs={
    #         "autocomplete": "current-password",
    #         "class": "form-control",
    #         "placeholder": "password",
    #     }),
    # )
    error_messages = {
        "invalid_login": ("Please enter a correct username and password."),
        "inactive": ("This account is inactive."),
    }

    class Meta:
        model = User


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(required=False)
    username = UsernameField()
    email = forms.CharField()

    class Meta:
        model = User
        fields = ("first_name", "username", "email", "password2")


class UserEditProfile(UserChangeForm):
    avatar = forms.ImageField(required=False)
    banner = forms.ImageField(required=False)
    first_name = forms.CharField(required=False)
    username = UsernameField()
    email = forms.CharField()

    class Meta:
        model = User
        fields = (
            'avatar',
            'banner',
            'first_name',
            'username',
            'email',
        )


class SingleItemCreationForm(forms.ModelForm):
    image = forms.ImageField()
    title = forms.CharField()
    price = forms.DecimalField()

    class Meta:
        model = Item
        fields = ("image", "title", "price")
        exclude = ('creator', 'owner',)
