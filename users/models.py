from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    def __str__(self):
        return self.user.username
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="profile.jpg", upload_to="profile_pictures")
    contact = models.CharField(default="999999999", max_length=100)
