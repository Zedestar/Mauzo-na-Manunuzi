from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    def __str__(self):
        return self.name
    seller_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    shortDesc = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField(max_length=200)
    image = models.ImageField(upload_to="my_pics", null=False, blank=False)
