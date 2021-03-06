from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from . models import Post,Comment,Profile


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class PostCreationForm(forms.ModelForm):
    body=forms.CharField(
        widget=forms.Textarea(attrs=({'rows':5,'class':'form-control'}))
    )
    class Meta:
        model=Post
        fields=['body',]

class PostEditForm(forms.ModelForm):
    body=forms.CharField(
        widget=forms.Textarea(attrs=({'rows':5,'class':'form-control'}))
    )
    class Meta:
        model=Post
        fields=['body',]


class CommentForm(forms.ModelForm):
    body=forms.CharField(
        widget=forms.Textarea(attrs=({'rows':5}))
    )
    class Meta:
        model=Comment
        fields=['body']

class ProfileCreationForm(forms.ModelForm):
    bio=forms.CharField(
        widget=forms.Textarea(attrs=({'rows':5,'class':'form-group'}))
    )
    class Meta:
        model=Profile
        fields=['profile_pic','bio']
