from django.urls import path
from . import views

# Main Folder has its own Main URL Paths, This provides Site Path for the following VVV
urlpatterns = [
path("<int:uid>", views.index, name="index"),							# Unique User Login
path("v1/", views.v1, name="view 1"),									# Test Page for View
path("", views.home, name="home"),										# Home Page
path("privacy/", views.privacy, name="privacy"),						# Privacy Policy Page
path("thankyou/", views.thankyou, name="thankyou"),						# Thank You for Voting Splash Page
]