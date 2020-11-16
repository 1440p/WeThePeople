from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
	username = forms.CharField(label='State Issued Government ID')
	first_name = forms.CharField()
	last_name = forms.CharField()
	ssn = forms.CharField(label='Social Security Number')

	class Meta:
		model = User
		fields = ["username", "first_name", "last_name", "ssn", "password1", "password2"]