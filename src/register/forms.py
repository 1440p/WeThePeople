from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Custom Form Class for registration for Voting

class RegisterForm(UserCreationForm):
	username = forms.CharField(label='State Issued Government ID')	# Labels and Variables for Data collected
	first_name = forms.CharField()
	last_name = forms.CharField()
	ssn = forms.CharField(label='Social Security Number')

	class Meta:
		model = User
		fields = ["username", "first_name", "last_name", "ssn", "password1", "password2"]  # Labeled Data for the User Model and Class