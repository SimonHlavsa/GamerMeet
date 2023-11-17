from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from register.models import UserProfile
from main.models import Likes, Matches
from django.urls import reverse
from django.http import HttpResponseRedirect

def home(response):
    if response.user.is_authenticated:
        return HttpResponseRedirect(reverse("discover"))  
    return render(response, "main/home.html", {})
    
@login_required
def discover(response):
    user = response.user
    likes = Likes.objects.all()
    all_users = User.objects.all()
    person_to_show = None

    for person in all_users:
        if user.id == person.id:
            continue
        
        if not likes:
            person_to_show = person
            break
        
        all_liked_persons = []
        for like in likes:
            if like.sender.id == user.id:
                all_liked_persons.append(like.receiver.id)
            
        if person.id in all_liked_persons:
            continue
        else:
            person_to_show = person
            break
            
    if person_to_show:
        person_to_show = UserProfile.objects.get(user = person_to_show)
    return render(response, "main/discover.html", {"person_to_show": person_to_show})
    
def DislikeView(request, pk):
    sender = request.user
    receiver = get_object_or_404(User, id=request.POST.get("person_id"))
    Likes.objects.create(sender=sender, receiver= receiver, like=False)
    return HttpResponseRedirect(reverse("discover"))   
    
def LikeView(request, pk):
    sender = request.user
    receiver = get_object_or_404(User, id=request.POST.get("person_id"))
    Likes.objects.create(sender=sender, receiver= receiver, like=True)
    return HttpResponseRedirect(reverse("discover"))

    
@login_required
def profile(response):  
    user = response.user
    user_profile = UserProfile.objects.get(user = user)
    return render(response, "main/profile.html", {"user_profile": user_profile})
    
@login_required
def contacts(response):
    matches = Matches.objects.all()
    return render(response, "main/contacts.html", {"matches":matches})

def contact_profile(request, pk):
    user = User.objects.get(id=pk)
    user_profile = UserProfile.objects.get(user=user)
    return render(request, "main/profile.html", {"user_profile": user_profile})

