from django.shortcuts import render
from django.http import HttpResponse
from .models import Users
# Create your views here.


def index(response, uid):
	user = Users.objects.get(uid=uid)
	return render(response, "main/name.html", {"user" : user})			# Http Response of current Logged In user
	#return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(user.name, user.ssn))

def home(response):
	return render(response, "main/home.html", {})						# Http Response for Home Page

def v1(response):
	return render(response, "main/base.html", {})						# Http Response for Base.html
	#return HttpResponse("<h1>This is anotrhher View! function v1 or View 1</h1>")

def privacy(response):
	return render(response, "main/privacy.html", {})					# Http Response for Privacy Policy Page

def thankyou(response):
	return render(response, "main/thankyou.html", {})					# Http Response for Thank You Splash Page