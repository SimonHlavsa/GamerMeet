from django.contrib.auth import login, logout
from django.shortcuts import render
from django.views import generic 
from django.urls import reverse_lazy
from .models import UserProfile
from .forms import RegisterForm, EditUserProfileForm

class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")
    
    def form_valid(self, form):
        # Create the User instance
        user = form.save()
        # Create a UserProfile instance associated with the user
        UserProfile.objects.create(user=user)
        # Log the user in
        login(self.request, user)
        return super().form_valid(form)
    

class Settings(generic.UpdateView):
    form_class = RegisterForm
    template_name = "registration/settings.html"
    success_url = reverse_lazy("login")

    def get_object(self):
        return self.request.user
    
class EditUserProfile(generic.UpdateView):
    form_class = EditUserProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("login")
    
    def get_object(self, quertyser=None):
        return UserProfile.objects.get(user=self.request.user)


def Logout(response):
    logout(response)
    return render(response, "registration/logout.html", {})

# def register(response):
    
#     if response.method == "POST":
#         form = RegisterForm(response.POST)
#         if form.is_valid():
#             form.save()
        
#         return redirect("/home")
    
#     else:
#         form = RegisterForm()
#     return render(response, "registration/register.html", {"form":form})

# def edit_profile(response):
    
#     if response.method == "POST":
#         form = RegisterForm(response.POST)
#         if form.is_valid():
#             form.save()
        
#         return redirect("/home")
    
#     else:
#         form = RegisterForm()
#     return render(response, "registration/edit_profile.html", {"form":form})
