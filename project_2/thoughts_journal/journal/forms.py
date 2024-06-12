from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from . models import Thought, Profile

class RegistrationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

class CredentialsForm(forms.ModelForm):
  password = None
  class Meta:
    model = User
    fields = ['username', 'email']
    exclude = ['password1', 'password2']          

class ProfilePicForm(forms.ModelForm):
  pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
  class Meta:
    model = Profile
    fields = ['pic']
    exclude = ['user']
    
class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=TextInput())
  password = forms.CharField(widget=PasswordInput())
  
class ThoughtForm(forms.ModelForm):
  class Meta:
    model = Thought
    fields = ['title', 'content']
    exclude = ['user']
    