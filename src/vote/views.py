from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def vote(response):
	return render(response, "vote/vote.html", {})

def voteSenate(response):
	return render(response, "vote/voteSenate.html", {})

def voteHouse(response):
	return render(response, "vote/voteHouse.html", {})