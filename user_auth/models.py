from django.db import models
from django.contrib.auth.models import AbstractUser, User

class CustomUser(AbstractUser):
  email = models.EmailField(unique=True)
  
  class Meta:
      swappable = 'AUTH_USER_MODEL'

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  brand_preferences = models.TextField(blank=True, null=True)  # Example: "Nike, Adidas"
  price_range = models.CharField(max_length=100, blank=True, null=True)  # Example: "$50-$100"
  measurements = models.JSONField(blank=True, null=True)  # Example: {'chest': 38, 'waist': 32}

  def __str__(self):
      return f"{self.user.username}'s Profile"