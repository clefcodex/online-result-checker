from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Account, Complain


class RegistrationForm(UserCreationForm):
    matric_number = forms.CharField(max_length=30)

    class Meta:
        model = Account
        fields = ('username', 'password1', 'password2', 'email', 'matric_number', 'first_name',
                  'last_name', 'department', 'study_level', 'academic_session')


class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('matric_number', 'password')

    def clean(self):
        matric_number = self.cleaned_data['matric_number']
        password = self.cleaned_data['password']
        if not authenticate(matric_number=matric_number, password=password):
            raise forms.ValidationError("Invalid login")


class ComplainForm(forms.ModelForm):

    class Meta:
        model = Complain
        fields = ('description',)