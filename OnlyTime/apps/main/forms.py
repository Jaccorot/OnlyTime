from django.contrib.auth.models import User
from django import forms


class CreateUserForm(froms.ModelForm):
    class Meta:
        model = User
        fields = ('usernamne', 'email', 'password')