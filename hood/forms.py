from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Profile

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'pub_date']

class UpdateUser(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username', 'email']
        
class UpdateProfile(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ['neighborhood',]
