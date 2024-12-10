from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings

class CustomUser(AbstractUser):
  email = models.EmailField(unique=True)
  
  class Meta:
      swappable = 'AUTH_USER_MODEL'

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

  brand_preferences = models.JSONField(default=list)  # to store multiple brand preferences as a list
  
  price_range = models.IntegerField(default=500)  # stores the selected price range
  
  measurements = models.JSONField(default=dict)  # to store measurements with keys such as 'chest', 'waist', 'hips', 'shoulders', 'legs'
  
  preference = models.IntegerField(default=3)  # stores preference as an integer from 1 (tight) to 5 (oversized)

  def __str__(self):
    return f"{self.user.username}'s Profile"