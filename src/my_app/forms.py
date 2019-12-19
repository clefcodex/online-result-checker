from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Account


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30)

    class Meta:
        model = Account
        fields = ('username', 'password1', 'password2', 'email', 'matric_number', 'first_name',
                  'last_name', 'department', 'study_level', 'academic_session')


class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username', 'password')

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Invalid login")
