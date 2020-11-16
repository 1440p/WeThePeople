from django.urls import path
from . import views

urlpatterns = [
path("<int:uid>", views.index, name="index"),
path("v1/", views.v1, name="view 1"),
path("", views.home, name="home"),
path("privacy/", views.privacy, name="privacy"),
]