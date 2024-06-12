from django.urls import path
from . import views

urlpatterns = [
	path('', views.login, name=''),
	path('view-tasks', views.get_tasks, name='view-tasks'),
	path('create-task', views.create_task, name='create-task'),
	path('update-task/<int:task_id>/', views.update_task, name='update-task'),
	path('delete-task/<int:task_id>/', views.delete_task, name='delete-task'),
	path('register', views.register, name='register'),
	path('logout', views.logout, name='logout')
]