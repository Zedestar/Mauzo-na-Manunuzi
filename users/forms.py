from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django import forms
from .models import Profile

# - Creating user form

class NewUserForm(UserCreationForm):

    email = forms.EmailField(required=True, max_length=100)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
        

class UserProfile(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["user", "image", "contact"]

class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "contact"]

 