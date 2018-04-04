from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = (
            'email',
            'password1',
            'password2',
            'office',
            'position',
            'birth_date',
            'gender',
            'address',
            'zip',
            'city',
            'state_province',
            'country',
            'home_phone',
            'desk_phone',
            'cell_phone',
            'facebook',
            'linkedin',
            'twitter'
        )
