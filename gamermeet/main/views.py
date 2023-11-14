from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from register.models import UserProfile

def home(response):
    return render(response, "main/home.html", {})
    
@login_required
def discover(response):
    return render(response, "main/discover.html", {})
    
@login_required
def profile(response):
    user = response.user
    user_profile = UserProfile.objects.get(user = user)
    return render(response, "main/profile.html", {"user_profile": user_profile})
    
@login_required
def contacts(response):
    return render(response, "main/contacts.html", {})

