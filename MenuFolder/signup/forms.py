from django.forms import BaseModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate
from .models import User


class LogInForm(forms.Form):

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        auth = authenticate(email=email, password=password) 
        if auth:
            return super(LogInForm, self).clean()


class CreateNewUserForm(forms.Form):

    def clean(self):
        email = self.cleaned_data.get('email')
        password_1 = self.cleaned_data.get("password_1")
        password_2 = self.cleaned_data.get("password_2")


# These are for the admin/django command line options
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email',)
    

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)

