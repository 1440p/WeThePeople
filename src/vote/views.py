from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

# These are Views that are made for the Vote Page Application
# Three Seperate Vote pages for Each Running pair of Candidates

def vote(response):
	return render(response, "vote/vote.html", {})

def voteSenate(response):
	return render(response, "vote/voteSenate.html", {})

def voteHouse(response):
	return render(response, "vote/voteHouse.html", {})