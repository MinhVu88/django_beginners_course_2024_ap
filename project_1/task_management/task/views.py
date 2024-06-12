from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm, RegistrationForm, LoginForm

def register(request):
	form = RegistrationForm()
	if request.method == 'POST':
		form = RegistrationForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('')
	context = {'form': form}  
	return render(request, 'task/register.html', context)

def login(request):
	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(request, data=request.POST)
		if form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(
				request,
				username=username,
				password=password
			)
			if user is not None:
				auth.login(request, user)
				return redirect('view-tasks')
	
	context = {'form': form}
	return render(request, 'task/login.html', context)

@login_required(login_url='')
def get_tasks(request):
	tasks = Task.objects.all()
	context = {'tasks': tasks}
	return render(request, 'task/view-tasks.html', context)

@login_required(login_url='')
def create_task(request):
	form = TaskForm()
	if request.method == 'POST':
		form = TaskForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('view-tasks')
	context = {'form': form}
	return render(request, 'task/create-task.html', context)

@login_required(login_url='')
def update_task(request, task_id):
	task = Task.objects.get(id=task_id)
	
	if request.method != 'POST':
		form = TaskForm(instance=task)
	else:
		form = TaskForm(instance=task, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('view-tasks')
		
	context = {'form': form, 'task': task}
	return render(request, 'task/update-task.html', context)    

@login_required(login_url='')
def delete_task(request, task_id):
	if request.method == 'POST':
		Task.objects.filter(id=task_id).delete()
		return redirect('view-tasks')
	
	return render(request, 'task/delete-task.html')      

@login_required(login_url='')
def logout(request):
	auth.logout(request=request)
	return redirect('')