from django.shortcuts import render
from django.http import HttpResponse
from .models import Users
# Create your views here.


def index(response, uid):
	user = Users.objects.get(uid=uid)
	return render(response, "main/name.html", {"user" : user})
	#return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(user.name, user.ssn))

def home(response):
	return render(response, "main/home.html", {})

def v1(response):
	return render(response, "main/base.html", {})
	#return HttpResponse("<h1>This is anotrhher View! function v1 or View 1</h1>")