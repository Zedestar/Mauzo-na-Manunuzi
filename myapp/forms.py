from django import forms
from .models import Product
from django.db import models

# - Creating Form recording new Product items
class FillingForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ["name", "price", "shortDesc", "desc", "image"]

