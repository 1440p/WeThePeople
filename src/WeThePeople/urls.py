"""WeThePeople URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register import views as r
from vote import views as v
urlpatterns = [
    path('admin/', admin.site.urls),                # Pointing to the path of Admin page
    path('register/', r.register, name="register"),  # Pointing to the registration page path
    path("vote/", v.vote, name="vote"),             # Pointing to the voting president page path
    path("voteSenate/", v.voteSenate, name="voteSenate"), # Pointing to the voting senator page path
    path("voteHouse/", v.voteHouse, name="voteHouse"),  # Pointing to the voting house of representative page path
    path('', include("main.urls")),                     # main URL path that holds other seperated pages, such as the privacy policy
    path('', include("django.contrib.auth.urls")),  # Page in use with authentication library 
]
