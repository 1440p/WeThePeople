from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.

# Viewable Pages for the Registration Page

def register(response):
	if response.method == "POST":			# Integeral for the Authentication
		form = RegisterForm(response.POST)	# WSGI Application works with this
		if form.is_valid():
			form.save()

		return redirect("/")
	else:
		form = RegisterForm()

	form = RegisterForm()
	return render(response, "register/register.html", {"form":form})  # Register Page path and Http Response