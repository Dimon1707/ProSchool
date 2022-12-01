
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, PasswordInput




class UserRegistrationForm(ModelForm):
    password_1 = CharField(
        max_length=20,
        min_length=6,
        widget=PasswordInput
    )

    password_2 = CharField(
        max_length=20,
        min_length=6,
        widget=PasswordInput
    )

