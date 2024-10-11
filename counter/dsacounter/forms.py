from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password1',]


class ResultForm(forms.ModelForm):
    class Meta:
        model=progress
        fields = ['easy', 'medium', 'hard','takentime','date','submittime','username']
class room(forms.ModelForm):
    class Meta:
        model=rooms
        fields=['roomid','teacherid','roomname','description']
class joinclass(forms.ModelForm):
    class Meta:
        model=studying
        fields=['student','room']
