from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
# Create your models here.

class Likes(models.Model):
    sender = models.ForeignKey(User, related_name='sent_likes', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_likes', on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['sender', 'receiver']
    
    def clean(self):
        # Zkontrolujte, zda sender a receiver nejsou stejní
        if self.sender == self.receiver:
            raise ValidationError("Uživatel nemůže dát like sám sobě.")
        
    def is_match(self):
        # Zjisti, zda existuje vzájemný "like"
        reverse_like_exists = Likes.objects.filter(sender=self.receiver, receiver=self.sender, like=True).exists()

        if reverse_like_exists and self.like:
            # Vytvoř match, pokud existuje vzájemný "like"
            Matches.objects.create(user1=self.sender, user2=self.receiver)

    def save(self, *args, **kwargs):
        # Zavolejte metodu clean před uložením
        self.clean()
        super().save(*args, **kwargs)
        self.is_match()
    
        
class Matches(models.Model):
    user1 = models.ForeignKey(User, related_name='matches1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='matches2', on_delete=models.CASCADE)
    match = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
 


