from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserModel
from django.contrib.auth.models import User
from .models import UserProfile

class RegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta: 
		model = User
		fields = ["username", "email", "password1", "password2"]
  

class EditUserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name", "age", "fav_games"]
    
