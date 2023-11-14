from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    fav_games = models.CharField(max_length=200, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    
    def __str__(self):
        return str(self.user)
    
