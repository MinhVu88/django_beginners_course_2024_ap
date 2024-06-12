from django import forms
from django.forms import ModelForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Task

class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = '__all__'
	
class RegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = [
			'username', 
			'password1', 
			'password2', 
			'email'
		]
	
class LoginForm(AuthenticationForm):
	username = forms.CharField(widget=TextInput())
	password = forms.CharField(widget=PasswordInput())    